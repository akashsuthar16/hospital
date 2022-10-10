import json
from odoo import http
from odoo.http import request
import json
# from odoo.addons.Prescription.controllers.login_controller import validate_token


class Patient(http.Controller):
    # @validate_token
    @http.route('/hospitalpatient',type='http',method=['GET'], csrf=False)
    def patient_hospital(self):
        try:
            patient_data = http.request.env['res.hospital.patient'].search([])
            patient_list = []
            for patients in patient_data:
                vals = {
                    'id':patients.id,
                    'name':patients.patient_name,
                    'gendar':patients.patient_gendar
                }
                patient_list.append(vals)
            data = {'Code':0,'Message':'Retrieve All Patient Record', 'Result':patient_list}
            return json.dumps(data)
        except Exception as e:
            return {"Code":1,"Message":"Failed Retrieve All Patient Record"}

    @http.route('/patient',type='json',method=['POST'],csrf=False)
    def patient_hospital_post(self,**rec):
        try:
            if request.jsonrequest:
                rec = request.jsonrequest
                if rec['patient_name']:
                    vals ={
                        'patient_name': rec['patient_name'],
                        'patient_ref': rec['patient_ref'],
                        'patient_gendar': rec['patient_gendar'],
                        'patient_age': rec['patient_age'] 
                    }
                new_patient = http.request.env['res.hospital.patient'].sudo().create(vals)
                data = {'Code':0,'Message':'Successfully Create Record', 'Result':new_patient.patient_name}
            return data
        except Exception as e:
            return {'Code':'1','Message':'New Record Is Not Created Because Method is bad','error':e}

    # @http.route('/update_schedules',type='http', csrf=False)
    # def update_schedule(self, **rec):
    #     try:
    #         if request.httprequest:
    #             if rec['id']:
    #                 schdules = request.env['res.hospital.patient'].sudo().search([('id', '=', rec['id'])])
    #                 if schdules:
    #                     schdules.sudo().write(rec)
    #                 args = {"Code":"0", "Message":"Bulk update schedule record","Result":rec['id']}
    #         return json.dumps(args)
    #     except Exception as e:
    #         return {"Code":"1",'Message':"record not updated","error":e}

    @http.route('/update_hospitalpatient',type='http',method=['PUT'],csrf=False)
    def update_patient(self,**rec):
        try:
            if request.httprequest:
                if rec['id']:
                    print("**********id*********",rec)
                    patients = http.request.env['res.hospital.patient'].sudo().search([('id','=',rec['id'])])
                    print("============patient_id search=============",patients)
                    if patients:
                        patients.sudo().write(rec)
                        print("********",patients)
                    data = {'Code':0,'Message':'Update Patient Record', 'Result':rec['id']}
                    print("+++++++++++++Data show the message++++++++++++",data)
            return json.dumps(data)
        except Exception as e:
            return {'Code':'1','Message':'Record is Not Update','error':e}

    @http.route('/delete_patient/<int:rec_id>',type='http',method=['DELETE'],csrf=False)
    def delete_hospital(self,rec_id):
        try:
            patient_del = request.env['res.hospital.patient'].sudo().browse(rec_id)
            id = patient_del.id
            patient_del.unlink()
            data = data = {"Code":"0", "Message":"Remove record", "Result":id}
            return json.dumps(data)
        except Exception as e:
            return {"Code":"1",'Message':"id is wrong"}