import click
import json
from pprint import pprint
from os.path import basename

from cpsml.lang import build_model
from cpsml.lang import get_thing_mm, get_resource_mm, get_synthesis_mm

from cpsml.transformations.thing2resources import thing_to_resources_m2m
from cpsml.transformations.resources2api import resources_to_api_m2m
from cpsml.transformations.thing2api import thing_to_api_m2m
from cpsml.transformations.system2apis import system_to_apis_m2m
from cpsml.transformations.thing2vcode import thing_to_vcode
from cpsml.transformations.openapi_2_eservices import openapi_2_eservices_mm
from cpsml.transformations.thing2entity import thing_to_entity_m2m


@click.group("cpsml")
@click.pass_context
def cli(ctx):
   """An example CLI for interfacing with a document"""
   # pprint(ctx.obj)
   pass


@cli.command("validate")
@click.argument("model_filepath")
@click.pass_context
def validate(ctx, model_filepath):
    print(f'[*] Running validation for model {model_filepath}')
    model = build_model(model_filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("t2r")
@click.argument("model_file")
@click.pass_context
def t2r(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.thing'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    mm = get_thing_mm()
    model = mm.model_from_file(model_file)
    thing = model.thing
    resources_model = thing_to_resources_m2m(thing)
    filepath = f'{thing.name}.resource'
    with open(filepath, 'w') as fp:
        fp.write(resources_model)
    print(f'[*] Stored Resources model in file: {filepath}')
    print(f'[*] Validating {thing.name} Resource model...')
    model = build_model(filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("r2a")
@click.argument("model_file")
@click.pass_context
def r2api(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.resource'):
        print(f'[X] Not a resource model.')
        raise ValueError()
    mm = get_resource_mm()
    model = mm.model_from_file(model_file)
    resources = model.resources
    print(f'[*] Found {len(resources)} Resources')
    for r in resources:
        print(f'- {r.name}: {r.__class__.__name__}')
    api_model = r2api_m2m(resources)
    filepath = f'myapi.api'
    with open(filepath, 'w') as fp:
        fp.write(api_model)
    print(f'[*] Stored API model in file: {filepath}')
    print(f'[*] Validating API model...')
    model = build_model(filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("t2a")
@click.argument("model_file")
@click.pass_context
def t2api(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.thing'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    thing_mm = get_thing_mm()
    tmodel = thing_mm.model_from_file(model_file)
    thing = tmodel.thing
    api_model = thing_to_api_m2m(thing)
    filepath = f'{thing.name}.api'
    with open(filepath, 'w') as fp:
        fp.write(api_model)
    print(f'[*] Validating API model...')
    model = build_model(filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("t2e")
@click.argument("model_file")
@click.pass_context
def t2e(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.thing'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    thing_mm = get_thing_mm()
    tmodel = thing_mm.model_from_file(model_file)
    thing = tmodel.thing
    entity_model = thing_to_entity_m2m(thing)
    filepath = f'{thing.name}.ent'
    with open(filepath, 'w') as fp:
        fp.write(entity_model)
    print(f'[*] Validating Generated Entity Model...')
    model = build_model(filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("s2a")
@click.argument("model_file")
@click.pass_context
def s2apis(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.system'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    thing_mm = get_thing_mm()
    synth_mm = get_synthesis_mm()
    smodel = synth_mm.model_from_file(model_file)
    system = smodel.system
    for thing in system.things:
        api_model = thing_to_api_m2m(thing)
        filepath = f'{thing.name}.api'
        with open(filepath, 'w') as fp:
            fp.write(api_model)
        print(f'[*] Validating API model...')
        model = build_model(filepath)
        if model:
            print(f'[*] Validation passed!')


@cli.command("t2vc")
@click.argument("model_file")
@click.pass_context
def t2vc(ctx, model_file):
    model_filename = basename(model_file)
    if not model_filename.endswith('.thing'):
        print(f'[X] Not a thing model.')
        raise ValueError()
    thing_mm = get_thing_mm()
    tmodel = thing_mm.model_from_file(model_file)
    thing = tmodel.thing
    a = thing_to_vcode(thing)
    return

    api_model = thing_to_api_m2m(thing)
    filepath = f'{thing.name}.api'
    with open(filepath, 'w') as fp:
        fp.write(api_model)
    print(f'[*] Validating API model...')
    model = build_model(filepath)
    if model:
        print(f'[*] Validation passed!')


@cli.command("oas2esvc")
@click.argument("swagger_file")
@click.pass_context
def openapi2eservices(ctx, swagger_file):
    model = openapi_2_eservices_mm(swagger_file)
    filepath = f'eservices.esvc'
    with open(filepath, 'w') as fp:
        fp.write(model)


def main():
   cli(prog_name="cpsml")


if __name__ == '__main__':
   main()
