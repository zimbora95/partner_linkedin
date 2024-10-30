{
    'name': 'Partner LinkedIn',
    'version': '18.0.1.0.0',
    'category': 'Sales/CRM',
    'summary': 'Add LinkedIn field to partners',
    'description': """
        This module adds a LinkedIn field to partner records,
        allowing you to store and manage LinkedIn profile URLs.
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}