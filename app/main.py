import uvicorn
import asyncio
import typer

from app.base import init_models

cli = typer.Typer()


@cli.command()
def db_init_models():
    asyncio.run(init_models())
    print("Done")


if __name__ == "__main__":
    uvicorn.run("controllers:app", host="0.0.0.0", port=8000, reload=True)
    cli()