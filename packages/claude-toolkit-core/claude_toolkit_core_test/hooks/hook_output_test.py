from claude_toolkit_core.hooks.hook_output import HookOutput, HookSpecificOutput


class TestHookOutput:
    def test_empty_output(self) -> None:
        output = HookOutput()
        assert output.model_dump(by_alias=True, exclude_none=True) == {}

    def test_block_decision(self) -> None:
        output = HookOutput(decision="block", reason="not allowed")
        result = output.model_dump(by_alias=True, exclude_none=True)
        assert result["decision"] == "block"
        assert result["reason"] == "not allowed"

    def test_with_hook_specific_output(self) -> None:
        output = HookOutput(
            hook_specific_output=HookSpecificOutput(
                hook_event_name="PreToolUse",
                permission_decision="deny",
                permission_decision_reason="blocked by policy",
            ),
        )
        result = output.model_dump(by_alias=True, exclude_none=True)
        hook_specific_output = result["hookSpecificOutput"]
        assert hook_specific_output["hookEventName"] == "PreToolUse"
        assert hook_specific_output["permissionDecision"] == "deny"
        assert hook_specific_output["permissionDecisionReason"] == "blocked by policy"
