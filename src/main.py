from platform import python_version

from fastapi import FastAPI
from starlette.responses import FileResponse

from src.routes import challenge, crud, search, upload

app = FastAPI()
favicon_path = "assets/favicon.ico"


@app.get("/favicon.ico", tags=["Padrões"])
async def favicon():
    return FileResponse(favicon_path)  # pragma: no cover


@app.get("/", tags=["Padrões"])
async def root():
    return {"python_version": python_version()}


app.include_router(
    challenge.router, tags=["Soupilar Challenge"], prefix="/soupilar"
)
app.include_router(crud.router, tags=["Crud Parceiros"], prefix="/partners")
app.include_router(
    search.router, tags=["Pesquisa Parceiros"], prefix="/search"
)
app.include_router(upload.router, tags=["Upload Parceiros"], prefix="/upload")
