import click

from cli.cmd import jobs, connect, version


@click.group()
def cli():
    pass


cli.add_command(jobs)
cli.add_command(connect)
cli.add_command(version)

if __name__ == "__main__":
    cli()
