"""Main module for docs_genius.

Use this module to import and gather multiple CLI commands
and command subgroups under a common CLI interface.
"""
import click


@click.command(name="hello-world")
@click.option("--name", default="world", help="Whom to greet")
def hello_world(name):
    click.echo(f"Hello {name}")

@click.group()
def entry_point():
    pass


entry_point.add_command(hello_world)


if __name__ == "__main__":
    entry_point()
