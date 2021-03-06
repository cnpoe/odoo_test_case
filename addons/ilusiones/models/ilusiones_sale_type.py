from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ProductSaleType(models.Model):
    """ProductSaleType is a bundle of products.
    Products on bundle depends of sale type.

    Arguments:
        models {Model} -- [Odoo Model]

    Raises:
        ValidationError -- [On fields constraints]
    """
    _name = 'ilusiones.product.sale.type'

    # TODO: add fubnctionality for pay day recurrent invoices
    # TODO: validate integers
    pay_day = fields.Integer(string='Dia de cobro')
    sale_type = fields.Selection(
        selection=[
            ('Prepago', 'Prepago'),
            ('Plan', 'Plan'),
            ('Activación', 'Activación')
        ],
        string='Tipo de venta'
    )

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

    _sql_constraints = [
        ('contract_unique', 'unique(contract)', '¡El contrato ya existe!'),
        ('serial_number_unique', 'unique(serial_number)', '¡El número de serie ya existe!')
    ]

    @api.constrains('pay_day')
    def _check_pay_day(self):
        """Validates range of pay day

        Raises:
            ValidationError -- Pay day must be lower than 31 and greater than 0
        """
        for record in self:
            if record.pay_day <= 0 or record.pay_day > 31:
                raise ValidationError(
                    'Día de cobro fuera de rango(1-31): %s' % record.pay_day
                )
