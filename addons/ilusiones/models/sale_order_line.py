from odoo import models, fields, api


class SaleOderLine(models.Model):
    _inherit = 'sale.order.line'

    combo_line = fields.Boolean(
        string='Is product consumible in combo',
        default=False
    )

    @api.model
    def create(self, vals):
        result = super(SaleOderLine, self).create(vals)
        return result
