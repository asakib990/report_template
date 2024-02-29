# -*- coding: utf-8 -*-
{
    'name': "report_template",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Utils',
    'version': '17.1',

    'depends': ['base',
                'app_name',
                ],

    # always loaded
    'data': [
        ## Security
        'security/ir.model.access.csv',

        ## Report
        # 'reports/report_template_sample.xml',
        'views/report_template_sample.xml',

        ## Wizards
        'wizards/report_template_wizard_view.xml',

        ## Menus
        'views/menus.xml',
    ],

}

