from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def prepare_line(self, product, order_id):
        line = {
            'layout_category_id': False,
            'product_uom': product.uom_id.id,
            'name': 'combito',
            'route_id': False,
            'product_uom_qty': 1,
            'tax_id': [[6, False, [2]]],
            'order_id': order_id,
            'product_id': product.id,
            'price_unit': 0,
            'combo_line': True
        }
        return line

    def create_order_lines(self, order_line):
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
