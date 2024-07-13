import click
from tabulate import tabulate

from cli.client import Client


@click.command()
@click.option(
    "--running",
    "-r",
    is_flag=True,
    default=False,
    help="Show only running jobs.",
)
@click.option(
    "--completed",
    "-c",
    is_flag=True,
    default=False,
    help="Show only completed jobs.",
)
def ls(running, completed):
    """List jobs."""
    client = Client()
    jobs = client.get_jobs()

    rows = []

    for job in jobs:
        rows.append([job.get("uuid"), job.get("success")])

    table = tabulate(rows, headers=["ID", "Success"])
    click.echo(table)
