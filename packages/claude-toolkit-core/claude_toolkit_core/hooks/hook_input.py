from typing import Any, Optional

from pydantic import BaseModel

from claude_toolkit_core.hooks.hook_event import HookEvent


class HookInput(BaseModel):
    """Represents the JSON input passed to a hook command via stdin."""

    agent_id: Optional[str] = None
    agent_type: Optional[str] = None
    cwd: str = ""
    hook_event_name: HookEvent
    permission_mode: str = ""
    prompt: Optional[str] = None
    session_id: str
    source: Optional[str] = None
    tool_execution_time_ms: Optional[int] = None
    tool_input: Optional[dict[str, Any]] = None
    tool_name: Optional[str] = None
    tool_output: Optional[str] = None
    transcript_path: str = ""
