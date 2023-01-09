# -*- coding: utf-8 -*-
# Copyright 2019 Shurshilov Artem
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Masar Corrections',
    'summary': '''Masar Corrections''',
    'version': '14.1.0.1.1',
    'category': 'Tools',
    'website': "",
    'author': 'Mounika',
    'application': False,
    "auto_install": False,
    'installable': True,
    'depends': ['base','sale','stock','account','l10n_gcc_invoice','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale.xml',
    ],
    "external_dependencies": {"python": [], "bin": []},
}
