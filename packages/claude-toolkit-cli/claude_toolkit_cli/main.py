import click

from claude_toolkit_cli.commands.hook import hook


@click.group(invoke_without_command=True)
@click.pass_context
def cli(context: click.Context) -> None:
    """CLI toolkit for Claude hooks and plugins."""
    if context.invoked_subcommand is None:
        click.echo(context.get_help())


cli.add_command(hook)


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
