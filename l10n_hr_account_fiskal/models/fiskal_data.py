from odoo import fields, models


class FiskalProstor(models.Model):
    _inherit = "l10n.hr.fiskal.prostor"


class FiskalUredjaj(models.Model):
    _inherit = "l10n.hr.fiskal.uredjaj"

    fiskalisation_active = fields.Boolean()
