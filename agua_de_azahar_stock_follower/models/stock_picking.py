from odoo import models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    @api.model
    def create(self, vals):
        picking = super(StockPicking, self).create(vals)
        # Buscar contactos que tienen marcado el campo 'add_as_follower'
        default_followers = self.env['res.partner'].search([('add_as_follower', '=', True)])
        if default_followers:
            # Se suscribe la lista de contactos al albarán
            picking.message_subscribe(partner_ids=default_followers.ids)
        return picking
