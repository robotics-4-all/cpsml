import click
import json
from pprint import pprint

from thingml.utils import build_model


@click.group("thingml")
@click.pass_context
def cli(ctx):
   """An example CLI for interfacing with a document"""
   # pprint(ctx.obj)
   pass


@cli.command("validate")
@click.argument("model_filepath")
@click.pass_context
def validate(ctx, model_filepath):
   model = build_model(model_filepath)
   for thing in model.things:
       print()
       print(f'[*] Found model for Thing: {thing.name}')
       print('---------------------------------------')
       for attr, val in thing.__dict__.items():
           if attr not in ('_tx_position', '_tx_position_end', 'parent'):
               print(f'- {attr}: {val}')


def main():
   cli(prog_name="thingml")


if __name__ == '__main__':
   main()
