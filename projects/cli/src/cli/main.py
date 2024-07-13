import click

from cli.cmd import jobs, version


@click.group()
def cli():
    pass


cli.add_command(jobs)
cli.add_command(version)

if __name__ == "__main__":
    cli()
