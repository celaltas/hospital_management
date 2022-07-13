
from odoo import api, fields, models


class Doctor(models.Model):
    _name = "hospital.doctor"
    _description = "Hospital Doctor"


    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email', )