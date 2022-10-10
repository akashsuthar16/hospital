from odoo import api,models,fields, _
# this pakage help in dic to xml convent.
# from dict2xml import dict2xml
# from dicttoxml import dicttoxml
# import sys
# from xml.dom.minidom import parseString

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(1500)
class HospitalAppointment(models.Model):
    _name ="hospital.appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"
    _rec_name = 'patient_ids'    

    patient_ids = fields.Many2one(string="Patient Name",comodel_name='res.hospital.patient',track_visibility='always')
    reference_no = fields.Char(string='Appointment Reference',required=True,
                          readonly=True, default=lambda self: _('New'),tracking=True)
    appointment_time = fields.Datetime(String="Appointment Date Time",default=fields.Datetime.now,tracking=True)
    patient_gendar = fields.Selection([('male','Male'),('female','Female'),('other','Other')], string='Gendar Type',related='patient_ids.patient_gendar',track_visibility='always')
    ref_patient = fields.Char(string ='Reference',tracking=True)
    patient_Prescription = fields.Html(string ='Prescription')
    priority = fields.Selection([('0','Normal'),('1','Low'),('2','Midiyam'),('3','High'),('4','Very High')],string="Priority",tracking=True)
    state = fields.Selection([('draft','Draft'),('in_consultation','In Consultation'),('done','Done'),('cancel','Cancel')],default='draft',string="state",required=True,track_visibility='always')
    doctor_id = fields.Many2one('res.users',string="Doctor",track_visibility='always')
    pharmacy_line_ids = fields.One2many('appointment.pharmacy.line','appointment_id', string="Pharmacy Lines",track_visibility='always')
    hide_sales_price = fields.Boolean(string="Hide Sales Price")
    

    @api.onchange('patient_ids')
    def _onchange_patient_ids(self):
        self.ref_patient = self.patient_ids.patient_ref

    
    def action_object_test(self,data=None):
        print("Button Test Sussefuly!!!!!!!!!!")
        # data = {
        #     'patient_ids':'patient_ids',
        #     'appointment_time':'appointment_time',
        #     'patient_gendar':'patient_gendar',
        #     'list':{'ref_patient':'ref_patient',
        #             'list2':{'patient_Prescription':'patient_Prescription'}},
        #     'priority':'priority',
        #     'state':'state'
        # }
        # print('data-*-*-*-*-',data)
        # # xml = list(dict2xml(data))
        # # print("----------------file of data convent---------------",xml)
        # xml = dicttoxml(data, attr_type = False)
        # print(parseString(xml).toprettyxml())
        # return xml
            


        # rainbow show with status Chanage
        # for rec in self:
        #     rec.write({'state':'done'})
        return {
            'effect':{
                'fadeout':'slow',
                'message': 'Click Successfull',
                'type':'rainbow_man',
            }
        }

    def action_in_consultation(self):
        for res in self:
            res.state = "in_consultation"

    def action_done(self):
        for res in self:
            res.state = "done"

    def action_cancel(self):
        for res in self:
            res.state = "cancel"

    def action_draft(self):
        for res in self:
            res.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code(
                'hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res


class AppointmentPharmacyLines(models.Model):
    _name ="appointment.pharmacy.line"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one('product.product',required=True)
    price_unit = fields.Float(related='product_id.list_price')
    qty = fields.Integer(string='Quantity', default=1)
    appointment_id = fields.Many2one('hospital.appointment',string="Appointment")