# -*- coding: utf-8 -*-
{
    'name': "Partner to User",
    'version':'1.0',
    'summary': """
        Create a Login/User from a partner""",

    'description': """
        Long description of module's purpose
    """,
    'license': 'AGPL-3',
    'author': "KABEER KB",
    'website': "",
    'category': 'base',
    'version': '0.1',
    #'price':8,
    #'currency':'EUR',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [

        'wizard/user_view.xml',
        'views/partner_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
