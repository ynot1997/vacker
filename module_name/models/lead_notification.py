# -*- coding: utf-8 -*-

import base64
import datetime
import logging

import logging

from odoo import api, models, fields

_logger = logging.getLogger(__name__)


class Lead(models.Model):
    _inherit = "crm.lead"

    # create method is used for getting function into this group
    @api.model
    def create(self, vals):
        user = super(Lead, self).create(vals)
        print(user)
        user.send_acknowledgment_email()
        return user

    # this function is to send email for the sales person which is assigned
    @api.onchange()
    def send_acknowledgment_email(self):
        for record in self:
            email_to = []

            if record.user_id:
                template_id = self.env.ref('module_name.crm_lead_mail_template')
                email_to += [record.user_id.work_email]
                # in template the basic format of mail is set there
                template_id.sudo().send_mail(record.id, force_send=True, email_values={'email_to': email_to})
                _logger.info('Sending Email for accepting the lead for salesperson.')
#                 logger info for seeing the messing in the log file
