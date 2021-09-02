# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_comptable_ref_courriel = fields.Char('Comptable Réf Courriel')

