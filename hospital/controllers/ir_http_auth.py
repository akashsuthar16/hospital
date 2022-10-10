from odoo import fields,models
from odoo.http import request

class IrHttp(models.AbstractModel):
    _inherit = "ir.http"

    @classmethod
    def _auth_method_validate_token(cls):
        print('_auth_method_validate_token-----------------------')
        access_token = request.httprequest.headers.get("Authorization")
        
        print ('--------call---------call-----------',access_token)
        if not access_token:
            return invalid_response("access_token_not_found", "missing access token in request header", 401)
        
        access_token = access_token.replace('Bearer ','')
        print("=====================access_token===============",access_token)
        access_token_data = request.env["api.access_token"].sudo().search([("token", "=", access_token)],
                                                                          order="id DESC", limit=1)
        print("=====================access_token_data===============",access_token_data)

        if access_token_data.find_or_create_token(user_id=access_token_data.user_id.id) != access_token:
            return invalid_response("access_token", "token seems to have expired or invalid", 401)

        request.session.uid = access_token_data.user_id.id
        request.uid = access_token_data.user_id.id
    