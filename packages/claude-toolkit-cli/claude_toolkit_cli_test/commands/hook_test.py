from click.testing import CliRunner

from claude_toolkit_cli.main import cli
from claude_toolkit_cli_test.fixtures import SAMPLE_HOOK_JSON


class TestHookCommand:
    def test_run_with_valid_input(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["hook"], input=SAMPLE_HOOK_JSON)
        assert result.exit_code == 0

    def test_run_with_empty_input(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["hook"], input="")
        assert result.exit_code != 0
        assert "No input received on stdin" in result.output

    def test_run_with_invalid_json(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["hook"], input="not json")
        assert result.exit_code != 0
        assert "Invalid JSON on stdin" in result.output

    def test_run_with_explicit_event_name(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["hook", "PostToolUse"], input=SAMPLE_HOOK_JSON)
        assert result.exit_code == 0
