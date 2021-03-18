import requests
import click
from AutoApiTestRunner.config import config


@click.group()
def cli():
    """Command Line tool to access Drone.io API."""
    pass


@cli.command()
@click.argument('username')
def user(username):
    r = requests.get('https://api.github.com/users/{}'.format(username)).json()
    print('Name: {}, Repos: {}, Bio: {}'.format(r['name'], r['public_repos'], r['bio']))


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


@cli.command()
@click.option(
    "--repo-name",
    prompt=True,
    help="Enter repo name",
)
@click.option(
    "--branch",
    prompt=True,
    help="Enter branch name",
)
def runner(repo_name, branch):
    print("repo_name:" + repo_name)
    print("branch:" + branch)
    r = requests.post(config.drone_host + 'api/repos/' + config.github_org + '/{}/builds?branch={}'.format(repo_name, branch),
                      auth=BearerAuth(config.drone_token)).json()
    print(r)


@cli.command()
@click.option(
    "--drone-token",
    prompt=True,
    help="Drone server token. Leave empty to use existing token",
)
@click.option(
    "--drone-host",
    prompt=True,
    help="Drone server URL. Leave empty to use existing URL",
)
@click.option(
    "--full-name",
    prompt=True,
    help="Your full name.",
)
@click.option(
    "--github-org",
    prompt=True,
    default="Shuttl-Tech",
    help="Name of default github organization. Leave empty to use existing name",
)
def init(
    drone_token,
    drone_host,
    full_name,
    github_org,
):
    click.echo(
        "Saving config"
    )

    confirmed = click.confirm(
        "Do you want to store new configuration", prompt_suffix="? "
    )
    if confirmed:
        config.update(
            drone_host=drone_host,
            drone_token=drone_token,
            full_name=full_name,
            github_org=github_org,
        )
    else:
        click.echo("Discarding new changes. Old configuration is left intact")
