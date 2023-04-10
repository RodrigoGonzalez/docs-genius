"""Main module for docs_genius.

Use this module to import and gather multiple CLI commands and command
subgroups under a common CLI interface.
"""

import click


@click.command(name="hello-world")
@click.option("--name", default="world", help="Whom to greet", type=str)
def hello_world(name: str) -> None:
    """Simple CLI command that greets the user.

    Parameters
    ----------
    name : str
        The name of the person to greet.
    """
    greet(name)


def greet(name: str) -> None:
    """Greet the person with the given name.

    Parameters
    ----------
    name : str
        The name of the person to greet.
    """
    click.echo(f"Hello {name}")


@click.group()
def entry_point() -> None:
    """Main entry point for docs_genius CLI."""


def main() -> None:
    """Execute the main entry point."""
    entry_point()


entry_point.add_command(hello_world)

if __name__ == "__main__":
    main()
