from fastapi import FastAPI, Body, HTTPException

from utils import get_build_dependencies, BuildDependenciesNotFound

app = FastAPI()


@app.post("/get_tasks")
async def get_tasks(build: str = Body(embed=True)):
    try:
        tasks = get_build_dependencies(build)
    except BuildDependenciesNotFound:
        raise HTTPException(
            status_code=404,
            detail="Build dependencies not found"
        )
    return tasks
