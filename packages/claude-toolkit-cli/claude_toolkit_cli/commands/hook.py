import json
import sys
from typing import Optional

import click

from claude_toolkit_core.hooks.hook_input import HookInput


@click.command()
@click.argument("event", required=False, default=None)
def hook(event: Optional[str]) -> None:
    """Handle a Claude hook event.

    Reads hook input JSON from stdin and dispatches to the
    appropriate handler. EVENT is the hook event name
    (e.g. PreToolUse); if omitted, it is read from the stdin JSON.
    """
    raw_input = sys.stdin.read()
    if not raw_input.strip():
        raise click.ClickException("No input received on stdin")

    try:
        data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        raise click.ClickException(f"Invalid JSON on stdin: {e}")

    hook_input = HookInput(**data)
    event_name = event or hook_input.hook_event_name
    dispatch(event_name, hook_input)


def dispatch(event: str, hook_input: HookInput) -> None:
    """Dispatch a hook event to its handler."""
    # Default: allow everything, no output needed
    pass
