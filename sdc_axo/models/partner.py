# -*- coding: utf-8 -*-
from odoo import models, fields, api,_
from odoo.exceptions import UserError, AccessError, ValidationError
from odoo.addons import decimal_precision as dp
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, float_compare
    

class Partner(models.Model):
    _inherit = 'res.partner'

    ref = fields.Char(string='Internal Reference')

    @api.model
    @api.depends('customer','supplier')
    def create(self, vals):
        if vals.get('company_type')=='company' and vals.get('customer')== False and vals.get('supplier')== False:
            vals['ref'] = ''
        elif vals.get('company_type')=='company' and vals.get('customer')== True:
            vals['ref'] = self.env['ir.sequence'].get('res.partner.c')
        elif vals.get('company_type')=='company' and vals.get('supplier')== True:
            vals['ref'] = self.env['ir.sequence'].get('res.partner.f')
        else:
            pass
        return super(Partner, self).create(vals) 
    
        
