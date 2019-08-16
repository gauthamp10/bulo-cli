import click

@click.command()
#@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--path', default='', help='To specify the path to traverse')
def cli(path):
    click.echo("Hello World")
    click.echo('Bye {0}'.format(path))

cli()