from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_organization = fields.Boolean(string="est une association")
    orga_choice = fields.Many2one(
        'res.partner',
        string="Choix de l'association",
        domain="[('is_organization', '=', 'True')]"
    )
    account_cyclos = fields.Boolean(
        string="Compte Cyclos",
        required=False,
        translate=False,
        readonly=False
    )
    commercial_name = fields.Text(string="Nom commercial")
    accept_newsletter = fields.Boolean(string="Accepte Newsletter")
    changeeuros = fields.Text(string="Change euros mensuel")
    contact_email = fields.Text("Email Cyclos")
    prvlt_sepa = fields.Boolean(
        string=("Prélèvement SEPA"),
        required=False, 
        translate=False, 
        readonly=False
    )
