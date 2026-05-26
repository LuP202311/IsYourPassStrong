import typer

app = typer.Typer()

@app.command()
def help():
    typer.echo(typer.style("1. `python main.py verifier mdp 'mot_de_passe'`         Vérifier si un mot de passe est robuste directement en commande",fg=typer.colors.CYAN))
    typer.echo(typer.style("2. `python main.py verifier interactif`                 Vérifier si un mot de passe est robuste de manière interactive",fg=typer.colors.CYAN))
    typer.echo(typer.style("3. `python main.py generate`                            Générer un mot de passe robuste",fg=typer.colors.CYAN))