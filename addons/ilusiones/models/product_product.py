from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_in_combo = fields.Many2many(
        comodel_name='ilusiones.product.sale.type',
        string='Productos en el combo'
    )

    service_in_combo = fields.Many2many(
        comodel_name='ilusiones.product.sale.type',
        string='Servicios en el combo'
    )

    insurance_in_combo = fields.One2many(
        comodel_name='ilusiones.product.sale.type',
        inverse_name='insurance',
        string='Seguro en el combo'
    )
