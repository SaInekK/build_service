import os
from typing import TypedDict

import yaml

BUILDS_PATH = 'builds/builds.yaml'
TASKS_PATH = 'builds/tasks.yaml'


if not os.path.isfile(BUILDS_PATH):
    raise FileNotFoundError('builds.yaml not found')

if not os.path.isfile(TASKS_PATH):
    raise FileNotFoundError('tasks.yaml not found')


class YamlReaderService:
    def __init__(self, file_path: str):
        self.file_content = self.load_yaml_file(file_path)

    def get_by_root_name(self, name: str) -> list[dict]:
        return self.file_content.get(name)

    @staticmethod
    def load_yaml_file(file_name: str) -> dict:
        print('in load_yaml_file')
        with open(file_name, 'r') as file:
            yaml_data = yaml.safe_load(file)
        return yaml_data


class Build(TypedDict):
    name: str
    tasks: list[str]


class Task(TypedDict):
    name: str
    dependencies: list[str]


builds_list: list[Build] = YamlReaderService(
    file_path=BUILDS_PATH,
).get_by_root_name('builds')

tasks_list: list[Task] = YamlReaderService(
    file_path=TASKS_PATH,
).get_by_root_name('tasks')


