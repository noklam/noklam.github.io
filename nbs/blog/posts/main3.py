import typer

def hello(name:str):
    typer.echo(f"Hello {name}")
    
def main():
    typer.run(hello)
    
