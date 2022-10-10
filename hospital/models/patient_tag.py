import string
from odoo import models,fields, _

class HospitalAppointment(models.Model):
    _name ="patient.tag"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Patient Tag"
    _rec_name = 'name'

    name = fields.Char(string="Tag",tracking=True)
    active = fields.Boolean(string="Active",default=True)
    color = fields.Integer(string="color")