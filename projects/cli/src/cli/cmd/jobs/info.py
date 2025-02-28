import json

import click

from cli.client import Client
from cli.utils import get_status


ALLOWED_SCHEMAS = (
    "qcschema",
    "json",
)


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
@click.option(
    "--schema",
    default="json",
    help="Set output schema.",
)
def info(job_id, output_data, input_data, schema):
    """Retrieve job information."""
    if schema.lower() not in ALLOWED_SCHEMAS:
        raise click.BadOptionUsage("--schema", "Invalid schema.")

    client = Client()
    job = client.get_job(job_id)

    if output_data and input_data:
        raise click.UsageError("Cannot display output and input data at the same time.")

    if output_data:
        match schema:
            case "json":
                click.echo(json.dumps(job.get("output_data"), indent=2))
            case "qcschema":
                click.echo(
                    json.dumps(job.get("input_data") | job.get("output_data"), indent=2)
                )
    elif input_data:
        click.echo(json.dumps(job.get("input_data"), indent=2))
    else:
        click.echo(f"Job ID: {job_id}")
        click.echo(f"Status: {get_status(job.get("status"))}")
