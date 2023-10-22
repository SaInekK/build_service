from yaml_loader import builds_list, tasks_list, Task


class BuildException(Exception):
    ...


class BuildDependenciesNotFound(BuildException):
    ...


def get_build_tasks(build_name: str) -> list[Task]:
    return next(
        (
            build['tasks'] for build in builds_list
            if build['name'] == build_name
        ),
        []
    )


def get_task_dependencies(task_name: str | Task) -> list[Task]:
    return next(
        (
            task['dependencies'] for task in tasks_list
            if task['name'] == task_name
        ),
        []
    )


def sort_tasks_by_dependencies(
        tasks: list[Task | str],
        result: list[str] | None = None,
) -> list[Task | str]:
    if result is None:
        result = []

    for task in tasks:
        if task["name"] in result:
            continue
        if task["dependencies"]:
            sort_tasks_by_dependencies(task["dependencies"], result)
        result.append(task["name"])
    return result


def get_build_task_graphs(build_name: str) -> list[dict]:
    task_names = get_build_tasks(build_name)
    if not task_names:
        raise BuildDependenciesNotFound()
    res = []
    for name in task_names:
        res.append(
            {'name': name, 'dependencies': get_task_tree(name)}
        )
    return res


def get_task_tree(task_name: str | Task) -> list[dict]:
    deps_graph = []
    if len(get_task_dependencies(task_name)) == 0:
        return []
    for dep in get_task_dependencies(task_name):
        d = {'name': dep, 'dependencies': get_task_tree(dep)}
        deps_graph.append(d)

    return deps_graph


def get_build_dependencies(build_name: str) -> list[str]:
    task_graphs = get_build_task_graphs(build_name)
    return sort_tasks_by_dependencies(task_graphs)
