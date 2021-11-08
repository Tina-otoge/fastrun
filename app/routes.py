import json
import os
from flask import request

from . import app, config


def check_secret_key():
    got = request.headers.get('X-API-KEY')
    assert got == config.SECRET_KEY

@app.post('/')
def run_task():
    check_secret_key()
    name = request.args.get('task')
    with open(config.TASKS_PATH) as f:
        tasks = json.load(f)
    assert name in tasks
    task = tasks[name]
    app.logger.info(f'Selected task "{name}"')
    cmds = (x.format(**request.form) for x in task)
    for i, cmd in enumerate(cmds):
        app.logger.info(f'Running command {i}: {cmd}')
        exit_code = os.system(cmd)
        assert exit_code == 0
    return "OK"
