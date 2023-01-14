from odoo import fields, models


class AccountJournal(models.Model):
    _inherit = "account.journal"

    # l10n_hr_fiscalisation_active = fields.Boolean(
    #     string="Fiscalization active",
    #     help="Fiscalisation active gor this journal, if not, only transaction account invoice can be posted",
    # )
    l10n_hr_default_nacin_placanja = fields.Selection(
        selection_add=[
            ("G", "Cash (bills and coins)"),
            ("K", "Credit or debit cards"),
            ("C", "Bank Cheque"),
            ("O", "Other payment means"),
        ],
    )
