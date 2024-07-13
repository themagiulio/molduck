import importlib.metadata

import click

from cli.client import Client


@click.command()
def version():
    """Display current version."""

    version = Client().get_version()
    version = f"v{version}" if version is not None else "not connected"

    click.echo(f"""
%%%%%%%%%%%%%%%%%%%%%            CLI: v{importlib.metadata.version("cli")}   
%%%###############%%%            Server: {version}
%%%+++============%%%         
%%%+++@@@===%%%%%%%%%%%%%%%%%%   Repository: https://github.com/themagiulio/molduck
%%%+++@@@===%%%%%%%%%%%%%%%%%%
%%%+++======%%%******++++++%%%
%%%+++======%%%%%%%%%%%%%%%%%%
%%%+++======%%%%%%%%%%%%%%%%%%
%%%+++============%%%         
%%%+++============%%%         
%%%+++============%%%         
%%%++++++++++++===%%%         
%%%+++%%%%%%%%%+++%%%         
%%%***%%%+++%%%***%%%         
%%%%%%%%%   %%%%%%%%%         
    """)
