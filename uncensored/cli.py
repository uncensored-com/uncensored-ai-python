import click
import webbrowser
from typing import Optional

from .api_config import set_api_key, get_api_key
from .utils import check_balance
from .models import list_models
from .exceptions import UncensoredError

@click.group()
def cli():
    """Uncensored AI command line interface."""
    pass

@cli.command()
def login():
    """Login and set up your API key."""
    click.echo("Opening browser to retrieve your API key...")
    webbrowser.open("https://api.uncensored.com/login")
    
    api_key = click.prompt("Please paste your API key", type=str)
    try:
        set_api_key(api_key)
        click.echo("API key saved successfully!")
    except Exception as e:
        click.echo(f"Error saving API key: {str(e)}", err=True)
        raise click.Abort()

@cli.command("list-models")
def list_models_cmd():
    """List available models."""
    try:
        models = list_models()
        for model in models:
            click.echo(f"Model: {model['id']}")
            click.echo(f"Status: {model['status']}")
            if 'message' in model:
                click.echo(f"Message: {model['message']}")
            click.echo("---")
    except UncensoredError as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

@cli.command()
def balance():
    """Check your usage and balance."""
    try:
        result = check_balance()
        click.echo(result['message'])
    except UncensoredError as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise click.Abort()

def main():
    """Main entry point for the CLI."""
    cli()

if __name__ == '__main__':
    main()
