from flask import render_template, url_for, request, current_app, jsonify

from net_inventory.frontend import view as blueprint
from net_inventory.shared.utils import api_call


@blueprint.route("/devices", methods=["GET"])
def devices():
    headers = ["Hostname", "IP", "Role", "Site", "OS", "Username", "Password"]
    resp, status_code = api_call("/inventory/devices", "get")
    inventory = resp["data"]
    return render_template("index.html", headers=headers, inventory=inventory)
