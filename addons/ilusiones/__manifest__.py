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
    'version': '0.2',
    'license': 'LGPL-3',
    'installable': True,
    'category': 'Test',
    'data': [
        'views/combo_menu.xml',
        'views/product_template_views.xml',
        'views/res_partner_view.xml',
        'views/combo_products_view.xml',
        'views/sale_order_view.xml',
        'data/res_partner.xml',
    ],
}
