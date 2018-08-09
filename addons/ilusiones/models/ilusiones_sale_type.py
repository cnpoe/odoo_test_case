from odoo import models, fields, api


class ProductSaleType(models.Model):
    _name = 'ilusiones.product.sale.type'

    # TODO: add fubnctionality for pay day recurrent invoices
    # TODO: validate integers
    pay_day = fields.Integer(string='Dia de cobro')
    # TODO: create catalog for custom sale types
    sale_type = fields.Selection(
        selection=[
            ('Prepago', 'Prepago'),
            ('Plan', 'Plan'),
            ('Activación', 'Activación')
        ],
        string='Tipo de venta'
    )

    # TODO: Organize products depends on service, insurance, stockable
    sale_products = fields.Many2many(
        comodel_name='product.product',
        string='Productos almacenables en esta venta',
        relation='combo_almacenables'
    )

    services = fields.Many2many(
        comodel_name='product.product',
        string='Servicios en esta venta',
        relation='combo_services'
    )

    insurance = fields.Many2one(
        comodel_name='product.product',
        string='Seguro en esta venta'
    )

    product_id = fields.Many2one(
        comodel_name='product.template',
        string='Combo relacionado'
    )

    user_id = fields.Many2one(
        comodel_name='res.partner',
        string='Cliente'
    )

    description = fields.Char(string="Descripción", required=True)
    serial_number = fields.Char(string='Número de serie', default="")
    contract = fields.Char(string='Número de contrato', default="")
    active = fields.Boolean(string='Is active?', default=True)
