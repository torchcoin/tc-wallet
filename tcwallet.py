import click
import emoji
import numpy as np

@click.command()
@click.option('--recipient', prompt='Wallet address of recipient')
@click.option('--amount', prompt='Amount to send')
def cli(recipient, amount):
    """TorchCoin Wallet software.
    """

    click.echo(
        emoji.emojize(
            "Sending :fire:{1}:fire: to {0}...".format(recipient, amount)))
    click.echo(emoji.emojize("Request processed. :+1:"))
