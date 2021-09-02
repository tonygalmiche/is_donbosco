# -*- coding: utf-8 -*-
{
    'name': 'Don-Bosco',
    'summary': "Module Odoo-10 InfoSaone pour Don-Bosco",
    'description': "Module Odoo-10 InfoSaone pour Don-Bosco",
    'version': '10.0.0.0.1',
    'author': "Tony Galmiche / InfoSaone",
    'license': "AGPL-3",
    'maintainer': "Tony Galmiche / InfoSaone",
    'category': 'InfoSaone',
    'website': 'https://infosaone.com',
    'depends': [
        "mail",
    ],
    'data': [
        "views/res_partner_view.xml",
        "wizard/mail_compose_message_view.xml",
    ],
    'auto_install': False,
    'installable': True,
    'application': True,
}
