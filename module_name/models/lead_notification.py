# -*- coding: utf-8 -*-

import base64
import datetime
import logging

from odoo import api, models, fields


class Lead(models.Model):
    _inherit = "crm.lead"
    _description = "Lead/Opportunity"

    @api.model
    def create(Lead, self, work_email):
        rec = super(work_email, self).create(fields)
        return rec

    @api.onchange()
    def send_acknowledgment_email(self, _logger):
        for record in self:
            email_to = []
            email_cc = []
            # email_cc += self._get_sales_coordinator_head()
            if record.target_group == 'employee':
                template_id = self.env.ref('sales_target.email_template_target_parent_acknowledgment')
                email_to += [record.res.users.emp_id.work_email]

            email_to = self.list_to_comma_seperated(email_to)
            email_cc = self.list_to_comma_seperated(email_cc)
            template_id.sudo().send_mail(record.id, force_send=True,
                                         email_values={'email_to': email_to, 'email_cc': email_cc})
            _logger.info('Sending Email for accepting the lead for salesperson.')
            record.is_email_sent = True
            record.email_sent_datetime = datetime.datetime.now()
        return super(Lead, self).send_acknowledgment_email()
