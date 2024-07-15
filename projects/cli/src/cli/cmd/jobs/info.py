import json

import click

from cli.client import Client
from cli.utils import get_status


@click.command()
@click.argument("job-id", type=str)
@click.option(
    "--output-data",
    "-out",
    is_flag=True,
    default=False,
    help="Display output data.",
)
@click.option(
    "--input-data",
    "-in",
    is_flag=True,
    default=False,
    help="Display output data.",
)
def info(job_id, output_data, input_data):
    """Retrieve job information."""
    client = Client()
    job = client.get_job(job_id)

    if output_data and input_data:
        raise click.UsageError("Cannot display output and input data at the same time.")

    if output_data:
        click.echo(json.dumps(job.get("output_data"), indent=2))
    elif input_data:
        click.echo(json.dumps(job.get("input_data"), indent=2))
    else:
        click.echo(f"Job ID: {job_id}")
        click.echo(f"Status: {get_status(job.get("status"))}")
