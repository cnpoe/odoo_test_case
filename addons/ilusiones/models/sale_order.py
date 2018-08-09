from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        return result

    @api.multi
    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        order_line_env = self.env['sale.order.line']
        for order in self:
            lines = order_line_env.with_context(active_test=False).search([
                ('order_id', '=', order.id)
            ])
            print('**************************+')
            print(lines)
            lines._action_launch_procurement_rule()
