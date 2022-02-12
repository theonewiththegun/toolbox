import os
import shutil

import settings
import utils

MODULE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))
DEFAULT_ROOT_DIR_PATH = os.path.join(MODULE_DIR_PATH, '../..')
DEFAULT_TEMPLATES_DIR_PATH = os.path.join(MODULE_DIR_PATH, 'templates')

# if possible use PROJECTS_ROOT var from settings, otherwise use the parent dir of `toolbox` instead
ROOT_DIR = utils.Folder(
    settings.get_settings_prop('PROJECTS_ROOT', default_value=DEFAULT_ROOT_DIR_PATH)
)
TEMPLATES_DIR = utils.Folder(DEFAULT_TEMPLATES_DIR_PATH)


def init_project(name):
    paths = {'root': ROOT_DIR.abs_path}
    paths['project_folder'] = os.path.join(paths['root'], name)

    if os.path.exists(paths['project_folder']):
        print(f'Project {name} already exists! Doing nothing.')
        return False
    os.mkdir(paths['project_folder'])

    for subfolder in ['data', 'output']:
        paths[subfolder] = os.path.join(paths['project_folder'], subfolder)
        os.mkdir(paths[subfolder])
    for i, file_name in enumerate(TEMPLATES_DIR.file_names()):
        paths[file_name] = os.path.join(paths['project_folder'], file_name)
        shutil.copyfile(TEMPLATES_DIR.file_paths(i), paths[file_name])

    return True
