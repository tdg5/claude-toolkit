from claude_toolkit_core.hooks.hook_event import HookEvent


class TestHookEvent:
    def test_pre_tool_use_value(self) -> None:
        assert HookEvent.PRE_TOOL_USE == "PreToolUse"

    def test_post_tool_use_value(self) -> None:
        assert HookEvent.POST_TOOL_USE == "PostToolUse"

    def test_session_start_value(self) -> None:
        assert HookEvent.SESSION_START == "SessionStart"

    def test_from_string(self) -> None:
        event = HookEvent("PreToolUse")
        assert event == HookEvent.PRE_TOOL_USE
