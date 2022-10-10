# _*_ coding: utf-8 _*_
{
    'name': "Hospital Management",

    'summary': """
        Hospital Application
        """ ,

    'description':""" """,

    'author': "",
    'website':"",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':'Hospital',
    'version': '0.1',
    'application': True,
    'sequence': 30,

    # any module necessary for this one to work correctly
    'depends':['base','mail','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'views/patient_views.xml',
        'views/female_patient_views.xml',
        'views/appointment_views.xml',
        'views/message_views.xml',
        'views/patient_tag_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}