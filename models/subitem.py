# -*- coding: utf-8 -*-

from odoo import models,fields, api , _ 
import pytz

class ConfineSubitem(models.Model):
   _name = 'confine.subitem'
   _description= 'Subitem'
   _inherit = ['mail.thread', 'mail.activity.mixin']
  



   name_sen = fields.Char(string="Subitem ID", reversed=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
   subitem_name = fields.Char(string="Subitem Name")
   main_it_id = fields.Many2one('confine.main_it', string='Main Item',required=True )

   @api.model
   def create(self,vals):
          if vals.get('name_sen', _('New')) == _('New'):
               vals['name_sen'] = self.env['ir.sequence'].next_by_code('confine.subitem.sequence')or _('New')
          result = super(ConfineSubitem, self).create(vals)
          return result  
    
   