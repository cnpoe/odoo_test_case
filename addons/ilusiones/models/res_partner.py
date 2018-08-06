from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    combos = fields.One2many(
        comodel_name='ilusiones.product.sale.type',
        inverse_name='user_id',
        string='Combos'
    )
