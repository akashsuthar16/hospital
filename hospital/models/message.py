# from datetime import datetime
from email.policy import default
import time
from odoo import api,models,fields, _

class Message_data(models.Model):
    _name ="res.message"
    # _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Message"
    _rec_name = 'message_type'  

    message_type = fields.Selection([('item_master_data','ITEM MASTER DATA'),
                                    ('delivery_address_master_data','DELIVERY ADDRESS MASTER DATA'),
                                    ('supplier_master_data','SUPPLIER MASTER DATA'),
                                    ('inbound_order','INBOUND ORDER'),
                                    ('pre_notification','PRE-NOTIFICATION'),
                                    ('receipt_confirmation','RECEIPT CONFIRMATION'),
                                    ('outvound_order','OUTBOUND ORDER'),
                                    ('packing_confirmation','PACKING CONFIRMATION'),
                                    ('outbound_order_confirmation','OUTBOUND ORDER CONFIRMATION'),
                                    ('stock_mutation','STOCK MUTATION'),
                                    ('stock_update','STOCK UPDATE'),
                                    ('stock_level','STOCK LEVEL'),
                                    ('return_confirmation','RETURN CONFIRMATION')],string="Message Type")
    message_ids = fields.Char(string='Delivary Reference',required=True,
                          readonly=True, default=lambda self: _('Message'))
    message_date = fields.Date(string="Message Date",default=fields.Date.context_today)#,default=fields.Date.context_today
    massage_time = fields.Float(string="Massage Time",default= time.time())

    @api.model
    def create(self, vals):
        if vals.get('message_ids', _('Message')) == _('Message'):
            vals['message_ids'] = self.env['ir.sequence'].next_by_code(
                'res.message') or _('Message')
        res = super(Message_data, self).create(vals)
        return res

    # @api.model
    # def create_message_details(self,data=None):
    #     if self.message_type == self.message_type:
    #         data={
    #             'message_date':self.message_date.today()
    #         }
    #         print()
    #     else:
    #         pass
    #     res_msg = super(Message_data,self).create(data)
    #     return res_msg