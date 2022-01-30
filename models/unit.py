# -*- coding: utf-8 -*-

from odoo import models,fields, api , _ 
import pytz

class ConfineUnit(models.Model):
    _name = 'confine.unit'
    _description= 'Unit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    



    un_name = fields.Char(string="Unit Name")
    name_seq = fields.Char(string="Unit ID", reversed=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self,vals):
          if vals.get('name_seq', _('New')) == _('New'):
               vals['name_seq'] = self.env['ir.sequence'].next_by_code('confine.unit.sequence')or _('New')
          result = super(ConfineUnit, self).create(vals)
          return result  
    
   