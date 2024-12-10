# # -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
{
    'name': "apollo_custom_web",
    'summary': "Enhances Odoo login page with custom functionality.",
    'description': "Adds a toggle password functionality to the login page.",
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Customization',
    'version': '0.1',
    'depends': ['base', 'web'],  # Required modules
    'data': [
        'views/webclient_templates.xml',  # Template file for inheriting the login page
    ],
    'assets': {
        'web.assets_frontend': [
            'apollo_custom_web/static/src/js/toggle_password.js',  # JS file for functionality
            'apollo_custom_web/static/src/css/style.css',          # Optional CSS for styling
        ],
    },
}



# {
#     'name': "apollo_custom_web",
#
#     'summary': """
#         Short (1 phrase/line) summary of the module's purpose, used as
#         subtitle on modules listing or apps.openerp.com""",
#
#     'description': """
#         Long description of module's purpose
#     """,
#
#     'author': "My Company",
#     'website': "http://www.yourcompany.com",
#
#     # Categories can be used to filter modules in modules listing
#     # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
#     # for the full list
#     'category': 'Uncategorized',
#     'version': '0.1',
#
#     # any module necessary for this one to work correctly
#     'depends': ['base', 'web'],
#
#     # always loaded
#     'data': [
#         # 'security/ir.model.access.csv',
#         'views/views.xml',
#         'views/templates.xml',
#         'views/webclient_templates.xml',
#     ],
#     # only loaded in demonstration mode
#     'demo': [
#         'demo/demo.xml',
#     ],
#     'assets': {
#         'web.assets_frontend': [
#             'apollo_custom_web/static/src/js/toggle_password.js',
#         ],
#     },
# }
