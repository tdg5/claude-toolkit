from typing import Any

SAMPLE_HOOK_INPUT: dict[str, Any] = {
    "session_id": "test-session-123",
    "hook_event_name": "PreToolUse",
    "transcript_path": "/tmp/transcript.jsonl",
    "cwd": "/tmp/test",
    "permission_mode": "default",
    "tool_name": "Bash",
    "tool_input": {"command": "echo hello"},
}
