from sqlalchemy import Column, Integer, String
from flask_marshmallow import Marshmallow
from marshmallow import fields

from app import ma
from flask import current_app
from sqlalchemy_utils import EncryptedType

from net_inventory.shared.database import db, ma
from net_inventory.shared.config import get_config

config = get_config()
_key = config["SECRET_KEY"]


class Device(db.Model):

    __tablename__ = "device"

    hostname = Column(String, nullable=False, primary_key=True)
    ip_address = Column(String, nullable=False, unique=True)
    site = Column(String, nullable=False)
    role = Column(String, nullable=False)
    device_type = Column(String, nullable=False)
    os = Column(String, nullable=False)
    username = Column(String, nullable=False)
    password = Column(EncryptedType(String, _key), nullable=False)

    def __init__(self, hostname, ip_address, site, role, device_type, os, username, password):
        self.hostname = hostname
        self.ip_address = ip_address
        self.site = site
        self.role = role
        self.device_type = device_type
        self.os = os
        self.username = username
        self.password = password

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class DeviceSchema(ma.Schema):
    hostname = fields.Str(required=True)
    ip_address = fields.Str(required=True)
    site = fields.Str(required=True)
    role = fields.Str(required=True)
    device_type = fields.Str(required=True)
    os = fields.Str(required=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)
