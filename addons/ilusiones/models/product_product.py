from odoo import models, fields, api


class ProductProduct(models.Model):
    _inherit = 'product.product'

    product_in_combo = fields.Many2many(
        comodel_name='ilusiones.product.sale.type',
        string='Productos en combo'
    )
