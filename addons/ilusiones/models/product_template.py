from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    insurance = fields.Boolean(string='Is insurance?')
    type = fields.Selection(selection_add=[('Combo', 'Combo')])

    product_combo = fields.One2many(
        comodel_name='ilusiones.product.sale.type',
        inverse_name='product_id',
        string='Combos'
    )
