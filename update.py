from logging import FileHandler, StreamHandler, INFO, basicConfig, error as log_error, info as log_info
from os import path as ospath, environ, execl as osexecl
from subprocess import run as srun
from dotenv import load_dotenv
from sys import executable

if ospath.exists('log.txt'):
    with open('log.txt', 'r+') as f:
        f.truncate(0)

basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[FileHandler('log.txt'), StreamHandler()],
                    level=INFO)

UPSTREAM_REPO = environ.get('UPSTREAM_REPO', '')
if len(UPSTREAM_REPO) == 0:
   UPSTREAM_REPO = 'https://github.com/askeladd654/jmdkh-nais'

UPSTREAM_BRANCH = environ.get('UPSTREAM_BRANCH', '')
if len(UPSTREAM_BRANCH) == 0:
    UPSTREAM_BRANCH = 'master'

if UPSTREAM_REPO is not None:
    if ospath.exists('.git'):
        srun(["rm", "-rf", ".git"])

    update = srun([f"git init -q \
                     && git config --global user.email jmdkh007@gmail.com \
                     && git config --global user.name jmdkh \
                     && git add . \
                     && git commit -sm update -q \
                     && git remote add origin {UPSTREAM_REPO} \
                     && git fetch origin -q \
                     && git reset --hard origin/{UPSTREAM_BRANCH} -q"], shell=True)

    if update.returncode == 0:
        log_info('Successfully updated with latest commit from UPSTREAM_REPO')
    else:
        log_error('Something went wrong while updating, check UPSTREAM_REPO if valid or not!')
