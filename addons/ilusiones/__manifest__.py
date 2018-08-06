{
    'name': 'Ilusiones Application',
    'description':
    '''
        Custom store application.
        3 types of sale for Ilusiones S.A. de C.V.
    ''',
    'author': 'Luis Morales',
    'website': 'https://www.github.com/cnpoe/',
    'depends': [
        'base',
        'stock',
        'sale_management',
    ],
    'application': True,
    'summary': 'Custom application for Ilusiones S.A de C.V. odoo 11',
    'version': '0.1',
    'license': 'LGPL-3',
    'installable': True,
    'category': 'Test',
    'data': [
        'views/product_template_views.xml',
    ],
}
