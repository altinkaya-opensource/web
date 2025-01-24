# Copyright 2022 Yiğit Budak (https://github.com/yibudak)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResCurrency(models.Model):
    _inherit = "res.currency"

    def _get_default_precision(self):
        return self.env["decimal.precision"].precision_get("Account")

    view_precision = fields.Integer(
        "View Precision",
        default=_get_default_precision,
        help="Number of digits after the decimal"
        " separator when displaying the value"
        " for monetary field. Default is"
        " account decimal precision.",
    )
    # toFixed() digits argument must be between 0 and 100
    _sql_constraints = [
        (
            "check_currency_view_precision_range",
            "CHECK(view_precision >= 0 AND view_precision < 100)",
            "View precision must be between 0 and 100",
        ),
    ]
