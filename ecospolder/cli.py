"""Command-line interface."""
import click


@click.command()
@click.version_option()
def run() -> None:
    """ecospolder."""
    pass


if __name__ == "__main__":
    run(prog_name="ecospolder")  # pragma: no cover
