# -*- coding: utf-8 -*-

from odoo import models,fields, api , _ 
import pytz

class ConfineMain(models.Model):
    _name = 'confine.main_it'
    _description= 'Main'
    _rec_name ='main_name'
    
    



    main_name = fields.Char(string="Main Name")
    name_seq = fields.Char(string="Main ID", reversed=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

    @api.model
    def create(self,vals):
          if vals.get('name_seq', _('New')) == _('New'):
               vals['name_seq'] = self.env['ir.sequence'].next_by_code('confine.main_it.sequence')or _('New')
          result = super(ConfineMain, self).create(vals)
          return result  
    
   