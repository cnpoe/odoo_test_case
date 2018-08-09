from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def prepare_line(self, product, order_id):
        """Generates a order line with the required parameters.

        Arguments:
            product {product.product} -- Product of the order line
            order_id {int} -- Order id

        Returns:
            dict -- Order line dictionary with required parameters
        """
        line = {
            'layout_category_id': False,
            'product_uom': product.uom_id.id,
            'name': product.name,
            'route_id': False,
            'product_uom_qty': 1,
            'tax_id': [[6, False, [2]]],
            'order_id': order_id,
            'product_id': product.id,
            'price_unit': 0,
            'active': False,
            'in_combo': True,
        }
        return line

    def create_order_lines(self, order_line):
        """Writes order lines for each order line with a product combo.

        Arguments:
            order_line {sale.order.line} -- Order lines of sale order.
        """
        order_line_env = self.env['sale.order.line']
        if (order_line.product_id.type == 'combo' or
                order_line.product_id.type == 'Combo'):
            for product in order_line.product_id.product_combo.sale_products:
                if product.type == 'product':
                    values = self.prepare_line(product, order_line.order_id.id)
                    order_line_env.create(values)

    @api.model
    def create(self, vals):
        result = super(SaleOrder, self).create(vals)
        for order_line in result.order_line:
            self.create_order_lines(order_line)
        return result

    @api.multi
    def _action_confirm(self):
        super(SaleOrder, self)._action_confirm()
        order_line_env = self.env['sale.order.line']
        for order in self:
            lines = order_line_env.with_context(active_test=False).search([
                ('order_id', '=', order.id)
            ])
            lines._action_launch_procurement_rule()
