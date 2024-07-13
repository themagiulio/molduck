import json

import click
import requests

from cli.client import Client


@click.command()
@click.argument("file")
def run(file: str):
    """Execute a job on the server."""
    try:
        with open(file, "r") as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        raise click.FileError(file, "no such file or directory")

    client = Client()

    job = client.run_job(json.loads(content))

    print(f"Started job with id: {job.get("uuid")}.")
