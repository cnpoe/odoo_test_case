from odoo import models, fields, api


class ProductSaleType(models.Model):
    _name = 'ilusiones.product.sale.type'

    # TODO add fubnctionality for pay day recurrent invoices
    pay_day = fields.Integer(string='Dia de cobro')
    # TODO create catalog for custom sale types
    sale_type = fields.Selection(
        selection=[
            ('Prepago', 'prepago'),
            ('Plan', 'plan'),
            ('Activacion', 'activacion')
        ],
        string='Tipo de venta'
    )
    fields.Many2many(
        comodel_name='product.template',
        string='Productos en esta venta'
    )

    product_id = fields.Many2one(
        comodel_name='product.product',
        string='Combo relacionado'
    )

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='Cliente'
    )

    manual_price = fields.Monetary(string='Price')
    serial_number = fields.Char(string='Número de serie')
    contract = fields.Char(string='Numero de contrato')
