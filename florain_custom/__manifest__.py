# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Florain customization',
    'version': '16.0.1.0.0',
    'category': '',
    'description': "Florain : custom fields and views",
    'depends': ['base','lcc_members'],
    'data': [
        'views/res_partner_views.xml'
    ],
    'license': 'LGPL-3',
    'installable': True,
    "auto_install": False,
    "application": False,
}
