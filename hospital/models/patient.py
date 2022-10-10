from datetime import date
import string
from odoo import models,fields,api, _

class PatientDetails(models.Model):
    _name = 'res.hospital.patient'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'patient_name'

    patient_sequence = fields.Char(string="Patient sequence",required=True,
                          readonly=True, default=lambda self: _('New Patient'))
    patient_name = fields.Char(string = 'Full Name', copy= False,required=True,track_visibility='always',tracking=True)
    patient_ref = fields.Char(string ='Reference',tracking=True)
    patient_date_of_birth = fields.Date(string="Date Of Birth",tracking=True)
    patient_gendar = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string='Gendar Type',tracking=True)
    patient_age = fields.Integer(string = 'Age',compute='_compute_age',store=True,tracking=True)
    patient_create = fields.Boolean(string = 'Create a New Patient ?')
    active = fields.Boolean(string="Active",default=True)
    image = fields.Image(string="Image")

    @api.depends('patient_date_of_birth')
    def _compute_age(self):
        for rec in self:
            today = date.today()
            if rec.patient_date_of_birth:
                rec.patient_age = today.year - rec.patient_date_of_birth.year
            else:
                rec.patient_age = 0

    @api.model
    def create(self, vals):
        if vals.get('patient_sequence', _('New Patient')) == _('New Patient'):
            vals['patient_sequence'] = self.env['ir.sequence'].next_by_code(
                'res.hospital.patient') or _('New Patient')
        res = super(PatientDetails, self).create(vals)
        return res
    # @api.model
    # def patient_create(self,vals):
    #     if vals.get('patient_sequence', _('New Patient')) == _('New Patient'):
    #         vals['patient_sequence'] = self.env['ir.sequence'].next_by_code(
    #             'res.hospital.patient') or _('New Patient')
    #     res = super(PatientDetails, self).create(vals)
    #     return res
