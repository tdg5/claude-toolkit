from click.testing import CliRunner

from claude_toolkit_cli.main import cli


class TestCli:
    def test_no_command_shows_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, [])
        assert result.exit_code == 0
        assert "Usage" in result.output

    def test_hook_subcommand_exists(self) -> None:
        runner = CliRunner()
        result = runner.invoke(cli, ["hook", "--help"])
        assert result.exit_code == 0
        assert "Handle a Claude hook event" in result.output
