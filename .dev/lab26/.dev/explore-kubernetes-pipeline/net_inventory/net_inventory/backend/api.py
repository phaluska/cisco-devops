from flask import jsonify, request, abort
from flasgger import swag_from

from net_inventory.backend import api as blueprint
from net_inventory.backend.models import Device, DeviceSchema
from net_inventory.shared.utils import get_parent_root
from net_inventory.shared.database import db

swag_dir = get_parent_root(__file__) + "/spec/"

devices_schema = DeviceSchema(many=True)


@blueprint.route("/inventory/devices", methods=["GET"])
@swag_from(swag_dir + "get_devices.yml")
def get_devices():
    """
    Update a list of devices

    Returns:
        JSON object
    """
    devices = Device.query.all()
    return jsonify(data=devices_schema.dump(devices)[0]), 200


@blueprint.route("/inventory/devices/<hostname>", methods=["GET"])
@swag_from(swag_dir + "get_device.yml")
def get_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = Device.query.get_or_404(hostname)
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 200


@blueprint.route("/inventory/devices", methods=["POST"])
@swag_from(swag_dir + "create_device.yml")
def create_device():
    """
    Get a single device's information

    Body Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    DeviceSchema().load(request.json)

    device = Device(**request.json)
    db.session.add(device)
    db.session.commit()
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 201


@blueprint.route("/inventory/devices/<hostname>", methods=["PATCH"])
@swag_from(swag_dir + "update_device.yml")
def update_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = db.session.query(Device).filter(Device.hostname == hostname).first()
    if not device:
        abort(404, {"message": "{} not found".format(hostname)})
    for k, v in request.json.items():
        setattr(device, k, v)
    db.session.commit()
    data, errors = DeviceSchema().dump(device)
    return jsonify(data=data, errors=errors), 200


@blueprint.route("/inventory/devices/<hostname>", methods=["DELETE"])
@swag_from(swag_dir + "delete_device.yml")
def delete_device(hostname):
    """
    Get a single device's information

    Path Parameters:
        hostname (str): hostname
    Returns:
        JSON object
    """
    device = db.session.query(Device).filter(Device.hostname == hostname).first()
    if not device:
        abort(404, {"message": "{} not found".format(hostname)})
    db.session.delete(device)
    db.session.commit()
    return jsonify(), 200
