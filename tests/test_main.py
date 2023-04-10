import pytest
from click.testing import CliRunner

from docs_genius.main import entry_point
from docs_genius.main import greet


@pytest.fixture
def runner():
    return CliRunner()


def test_hello_world_default(runner):
    """
    This test checks if the hello-world command returns the correct output
    when no name is provided, using the default value 'world'.
    """
    result = runner.invoke(entry_point, ["hello-world"])
    assert result.exit_code == 0
    assert result.output == "Hello world\n"


def test_hello_world_with_name(runner):
    """
    This test checks if the hello-world command returns the correct output when
    a name is provided.
    """
    result = runner.invoke(entry_point, ["hello-world", "--name", "Alice"])
    assert result.exit_code == 0
    assert result.output == "Hello Alice\n"


def test_greet(capsys):
    """This test checks if the greet function prints the correct output."""
    greet("John")
    captured = capsys.readouterr()
    assert captured.out == "Hello John\n"
