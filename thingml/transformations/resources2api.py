from os.path import basename

from thingml.utils import get_resource_mm, build_model


def r2api_m2m(resource_model_path: str, output_model=''):
    model_filename = basename(resource_model_path)
    if not model_filename.endswith('.resource'):
        print(f'[X] Not a resource model.')
        raise ValueError()
    mm = get_resource_mm()
    model = mm.model_from_file(resource_model_path)
    resources = model.resources
    print(f'[*] Found {len(resources)} Resources')
    print(f'[*] {resources}')
