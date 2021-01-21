import sys
from os import path, mkdir, getcwd
from textx import GeneratorDesc
import jinja2

from thing_dsl.utils import build_model

_THIS_DIR = path.abspath(path.dirname(__file__))

# Initialize template engine.
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(path.join(_THIS_DIR, 'templates')),
    trim_blocks=True,
    lstrip_blocks=True)
sensor_tpl = jinja_env.get_template('sensor.tpl')


class GeneratorCommlibPy:
    srcgen_folder = path.realpath(getcwd())

    @staticmethod
    def generate(model_fpath: str,
                 gen_imports: bool = False,
                 out_dir: str = None):
        # Create output folder
        if out_dir is None:
            out_dir = GeneratorCommlibPy.srcgen_folder
        model, imports = build_model(model_fpath)


def _generator_commlib_py_impl(metamodel, model, output_path, overwrite,
                               debug, **custom_args):
    # Some code that perform generation
    gen_imports = custom_args['gen_imports'] if 'gen_imports' in custom_args \
        else True
    GeneratorCommlibPy.generate(model._tx_filename, gen_imports=gen_imports)


generator_commlib = GeneratorDesc(
    language='thing_dsl',
    target='python',
    description='Generates python source code for Things',
    generator=_generator_commlib_py_impl)
