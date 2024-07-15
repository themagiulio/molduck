import click
import requests
from requests.exceptions import ConnectionError

from cli.client import Client
from cli.config import Config


@click.command()
def connect():
    """Connect to webserver"""
    config = Config()

    webserver_url = click.prompt("Enter webserver url")

    # Check connection
    try:
        response = requests.get(webserver_url)
    except ConnectionError:
        raise click.ClickException("Cannot connect to the server")

    config.set_config("server", webserver_url)

    click.echo("Connected to webserver.")
