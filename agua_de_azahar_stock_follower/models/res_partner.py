from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    add_as_follower = fields.Boolean(
        string='Añadir como seguidor automático',
        help="Marque este campo para que este contacto se añada automáticamente como seguidor en los albaranes."
    )
