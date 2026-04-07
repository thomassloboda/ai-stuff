#!/usr/bin/env python3
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_DIR = REPO_ROOT / "agents"
SKILLS_DIR = REPO_ROOT / "skills"

LANGUAGE_PATTERNS = [
    re.compile(r"always use the user's language", re.IGNORECASE),
    re.compile(r"always use the user language", re.IGNORECASE),
    re.compile(r"always answer in the user's language", re.IGNORECASE),
    re.compile(r"always answer in the language of the user", re.IGNORECASE),
    re.compile(r"always use the user language to answer", re.IGNORECASE),
]

DELEGATION_PATTERNS = [
    re.compile(r"\bsubagent\b", re.IGNORECASE),
    re.compile(r"\bdelegate\b", re.IGNORECASE),
    re.compile(r"\bdelegation\b", re.IGNORECASE),
]

LEGACY_TOOL_ALIASES = {
    "manage_todo_list",
    "list_dir",
    "read_file",
    "replace_string_in_file",
    "multi_replace_string_in_file",
    "grep_search",
    "semantic_search",
    "list_code_usages",
    "get_errors",
    "run_in_terminal",
    "get_terminal_output",
    "create_and_run_task",
    "get_changed_files",
    "runCommands",
    "fetch_webpage",
}

REQUIRED_AGENT_KEYS = {"description", "model", "title"}
REQUIRED_NAMED_AGENT_KEYS = REQUIRED_AGENT_KEYS | {"name"}
REQUIRED_SKILL_KEYS = {"name", "description"}


@dataclass
class Issue:
    level: str
    path: Path
    message: str


def parse_frontmatter(text: str) -> tuple[dict[str, str], str, str | None]:
    if not text.startswith("---\n"):
        return {}, text, "missing opening frontmatter delimiter"

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text, "missing closing frontmatter delimiter"

    raw = text[4:end]
    body = text[end + 5 :]
    data: dict[str, str] = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith("[") and not value.rstrip().endswith("]"):
            block = [value]
            i += 1
            while i < len(lines):
                block.append(lines[i].strip())
                if lines[i].strip().endswith("]"):
                    break
                i += 1
            data[key] = " ".join(block)
        else:
            data[key] = value
        i += 1
    return data, body, None


def parse_tool_list(frontmatter: dict[str, str]) -> set[str]:
    raw = frontmatter.get("tools")
    if not raw:
        return set()
    return set(re.findall(r"[A-Za-z0-9._/-]+", raw))


def collect_skill_names() -> set[str]:
    names = set()
    for skill_file in SKILLS_DIR.glob("*/SKILL.md"):
        names.add(skill_file.parent.name)
    return names


def collect_skill_refs(text: str) -> set[str]:
    refs = set()
    for line in text.splitlines():
        if not re.search(r"\b(skill|skills|use|apply|works best|recommend)\b", line, re.IGNORECASE):
            continue
        for match in re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", line):
            refs.add(match)
    return refs


def has_language_directive(text: str) -> bool:
    return any(pattern.search(text) for pattern in LANGUAGE_PATTERNS)


def has_delegation_directive(text: str) -> bool:
    return any(pattern.search(text) for pattern in DELEGATION_PATTERNS)


def find_legacy_aliases(text: str) -> set[str]:
    found = set()
    for alias in LEGACY_TOOL_ALIASES:
        if re.search(rf"\b{re.escape(alias)}\b", text):
            found.add(alias)
    return found


def lint_agent_file(path: Path, skill_names: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    text = path.read_text()
    frontmatter, body, frontmatter_error = parse_frontmatter(text)
    if frontmatter_error:
        issues.append(Issue("ERROR", path, frontmatter_error))
        return issues

    required = REQUIRED_NAMED_AGENT_KEYS if path.name.endswith(".agent.md") else REQUIRED_AGENT_KEYS
    missing = sorted(required - frontmatter.keys())
    if missing:
        issues.append(Issue("ERROR", path, f"missing frontmatter keys: {', '.join(missing)}"))

    if path.name.endswith(".agent.md"):
        expected_name = path.name.removesuffix(".agent.md")
        actual_name = frontmatter.get("name", "").strip("'\"")
        if actual_name and actual_name != expected_name:
            issues.append(Issue("WARN", path, f"frontmatter name `{actual_name}` does not match file stem `{expected_name}`"))

    for ref in sorted(collect_skill_refs(body)):
        if ref not in skill_names:
            issues.append(Issue("ERROR", path, f"references missing skill `{ref}`"))

    if not has_language_directive(body):
        issues.append(Issue("ERROR", path, "missing explicit user-language directive"))

    tools = parse_tool_list(frontmatter)
    if "agent/runSubagent" in tools and not has_delegation_directive(body):
        issues.append(Issue("ERROR", path, "declares `agent/runSubagent` but has no delegation policy"))

    for alias in sorted(find_legacy_aliases(body)):
        issues.append(Issue("ERROR", path, f"mentions legacy or undeclared tool alias `{alias}`"))

    return issues


def lint_skill_file(path: Path, skill_names: set[str]) -> list[Issue]:
    issues: list[Issue] = []
    text = path.read_text()
    frontmatter, body, frontmatter_error = parse_frontmatter(text)
    if frontmatter_error:
        issues.append(Issue("ERROR", path, frontmatter_error))
        return issues

    missing = sorted(REQUIRED_SKILL_KEYS - frontmatter.keys())
    if missing:
        issues.append(Issue("ERROR", path, f"missing frontmatter keys: {', '.join(missing)}"))

    declared_name = frontmatter.get("name", "").strip("'\"")
    expected_name = path.parent.name
    if declared_name and declared_name != expected_name:
        issues.append(Issue("ERROR", path, f"frontmatter name `{declared_name}` does not match skill directory `{expected_name}`"))

    for ref in sorted(collect_skill_refs(body)):
        if ref not in skill_names:
            issues.append(Issue("ERROR", path, f"references missing skill `{ref}`"))

    return issues


def main() -> int:
    skill_names = collect_skill_names()
    issues: list[Issue] = []

    for path in sorted(AGENTS_DIR.glob("*.md")):
        issues.extend(lint_agent_file(path, skill_names))

    for path in sorted(SKILLS_DIR.glob("*/SKILL.md")):
        issues.extend(lint_skill_file(path, skill_names))

    if not issues:
        print("Prompt lint passed.")
        return 0

    errors = 0
    for issue in issues:
        if issue.level == "ERROR":
            errors += 1
        rel_path = issue.path.relative_to(REPO_ROOT)
        print(f"{issue.level} {rel_path}: {issue.message}")

    print(f"\n{len(issues)} issue(s), {errors} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
