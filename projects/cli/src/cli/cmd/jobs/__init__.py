import click

from cli.cmd.jobs.info import info
from cli.cmd.jobs.ls import ls
from cli.cmd.jobs.run import run


@click.group()
def jobs():
    """Manage jobs on the webserver."""
    pass


jobs.add_command(ls)
jobs.add_command(info)
jobs.add_command(run)
