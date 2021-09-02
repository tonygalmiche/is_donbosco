# -*- coding: utf-8 -*-
from odoo import _, api, fields, models, SUPERUSER_ID, tools
from odoo.tools.safe_eval import safe_eval


class MailComposer(models.TransientModel):
    _inherit = 'mail.compose.message'

    is_copy = fields.Char('Copie')


    @api.model
    def default_get(self, fields):
        result = super(MailComposer, self).default_get(fields)
        if self._context.get("active_id"):
            if self._context.get("default_model")==u'account.invoice':
                invoices = self.env['account.invoice'].search([('id','=',self._context.get("active_id"))])
                for invoice in invoices:
                    result['is_copy'] = invoice.partner_id.is_comptable_ref_courriel
        return result


    @api.multi
    def get_mail_values(self, res_ids):
        self.ensure_one()
        res = super(MailComposer, self).get_mail_values(res_ids)
        for key, value in res.iteritems():
            value['is_copy'] = self.is_copy
        return res


class Message(models.Model):
    _inherit = 'mail.message'

    is_copy = fields.Char('Copie')


class Partner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _notify_prepare_email_values(self, message):
        mail_values = super(Partner, self)._notify_prepare_email_values(message)
        vals = {
            'email_cc': message.is_copy,
        }
        mail_values.update(vals)
        return mail_values

