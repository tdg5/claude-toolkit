from claude_toolkit_core.hooks.hook_event import HookEvent
from claude_toolkit_core.hooks.hook_input import HookInput
from claude_toolkit_core_test.fixtures import SAMPLE_HOOK_INPUT


class TestHookInput:
    def test_parses_minimal_input(self) -> None:
        hook_input = HookInput(
            session_id="abc",
            hook_event_name=HookEvent.PRE_TOOL_USE,
        )
        assert hook_input.session_id == "abc"
        assert hook_input.tool_name is None

    def test_parses_full_input(self) -> None:
        hook_input = HookInput(**SAMPLE_HOOK_INPUT)
        assert hook_input.session_id == "test-session-123"
        assert hook_input.hook_event_name == "PreToolUse"
        assert hook_input.tool_name == "Bash"
        assert hook_input.tool_input == {"command": "echo hello"}
        assert hook_input.cwd == "/tmp/test"
