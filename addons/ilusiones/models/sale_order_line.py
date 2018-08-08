from odoo import models, fields, api


class SaleOderLine(models.Model):
    _inherit = 'sale.order.line'

    active = fields.Boolean(default=True)

    @api.model
    def create(self, vals):
        result = super(SaleOderLine, self).create(vals)
        return result
