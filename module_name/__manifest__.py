# -*- coding: utf-8 -*-
{
    'name': "sales_notification",

    'summary': """
        In this module we are using the base code and give notification to the employee while he is assigned to new task,
        Used for lead notification""",

    'description': """
        Here when the lead is assigned to the salesperson a pop-up will be displayed and notify to the salesperson 
    """,

    'author': "Tony",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
