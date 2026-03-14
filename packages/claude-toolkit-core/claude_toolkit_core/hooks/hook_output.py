from typing import Optional

from pydantic import BaseModel, ConfigDict

from claude_toolkit_core.text import TextTransformation


class HookSpecificOutput(BaseModel):
    """Event-specific output fields."""

    model_config = ConfigDict(
        alias_generator=TextTransformation.to_camel_case,
        populate_by_name=True,
    )

    additional_context: Optional[str] = None
    hook_event_name: Optional[str] = None
    permission_decision: Optional[str] = None
    permission_decision_reason: Optional[str] = None


class HookOutput(BaseModel):
    """Represents the JSON output a hook command can return via stdout."""

    model_config = ConfigDict(
        alias_generator=TextTransformation.to_camel_case,
        populate_by_name=True,
    )

    decision: Optional[str] = None
    hook_specific_output: Optional[HookSpecificOutput] = None
    reason: Optional[str] = None
    suppress_output: Optional[bool] = None
