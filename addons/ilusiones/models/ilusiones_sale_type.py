from odoo import models, fields, api


class ProductSaleType(models.Model):
    _name = 'ilusiones.product.sale.type'

    # TODO: add fubnctionality for pay day recurrent invoices
    # TODO: validate integers
    pay_day = fields.Integer(string='Dia de cobro')
    # TODO: create catalog for custom sale types
    sale_type = fields.Selection(
        selection=[
            ('prepago', 'Prepago'),
            ('plan', 'Plan'),
            ('activacion', 'Activacion')
        ],
        string='Tipo de venta'
    )

    sale_products = fields.Many2many(
        comodel_name='product.product',
        string='Productos en esta venta'
    )

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Combo relacionado'
    )

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='Cliente'
    )

    combo_price = fields.Float(string='Precio de combo', digits=(16, 4))
    serial_number = fields.Char(string='Número de serie')
    contract = fields.Char(string='Numero de contrato')
    active = fields.Boolean(string='Is active?')
