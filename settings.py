import os
import json


PATH_TO_SETTINGS = os.path.join(os.path.expanduser('~'), 'settings.json')


def check_settings_file():
    """Creates settings.json if not created yet"""
    if not os.path.exists(PATH_TO_SETTINGS):
        with open(PATH_TO_SETTINGS, 'w', encoding='utf-8') as settings_file:
            settings_file.write('{}')


def read_settings() -> dict:
    check_settings_file()
    with open(PATH_TO_SETTINGS, 'r', encoding='utf-8') as settings_file:
        data = json.load(settings_file)
    return data


def write_settings(dict_to_write: dict):
    check_settings_file()
    with open(PATH_TO_SETTINGS, 'w', encoding='utf-8') as settings_file:
        json.dump(dict_to_write, settings_file)


def get_settings_prop(prop_name: str):
    check_settings_file()
    settings = read_settings()
    return settings[prop_name]


def get_settings_prop_deep(*json_path):
    """Use this to traverse deep settings structures."""
    check_settings_file()
    settings = read_settings()
    cursor = settings
    for element_id in json_path:
        cursor = cursor[element_id]
    return cursor


def set_settings_prop(prop_name: str, prop_value):
    check_settings_file()
    settings = read_settings()
    prev_prop_value = settings.get(prop_name, '<empty_value>')
    settings[prop_name] = prop_value
    write_settings(settings)
    print(f'Property `{prop_name}` had value `{prev_prop_value}`, '
          f'which has been changed to `{prop_value}`.')


def del_settings_prop(prop_name: str):
    check_settings_file()
    settings = read_settings()
    prev_prop_value = settings.get(prop_name, '<empty_value>')
    del settings[prop_name]
    write_settings(settings)
    print(f'Property `{prop_name}` which had value `{prev_prop_value}` '
          f'has been deleted.')

