import requests
import yaml
import inspect
from os.path import dirname, abspath, join

from flask import session, current_app


def api_call(url, method, params={}, json={}):

    API_BASE_URL = current_app.config["URL"] + "/api/v1"

    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        r = getattr(requests, method.lower())(API_BASE_URL + url, params=params, json=json, headers=headers)
    except requests.exceptions.ConnectionError:
        return {"message": "ConnectionError"}

    if r.status_code == 401:
        session.clear()
    return r.json(), r.status_code


def get_parent_root(file):
    return dirname(abspath(file))


def load_yaml(filename):
    frame = inspect.stack()[1]
    module = inspect.getmodule(frame[0])
    caller_dir = dirname(module.__file__)
    file_path = join(caller_dir, filename)
    with open(file_path, "r") as stream:
        data = yaml.load(stream, Loader=yaml.FullLoader)
    return data
