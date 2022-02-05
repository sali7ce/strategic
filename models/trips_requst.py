# -*- coding: utf-8 -*-

from odoo import models,fields, api , _ 
import pytz

class TripsRequist(models.Model):
    _name = 'trips.request'
    _description= 'Trips Requst'

    
    partner_id =fields.Many2one("res.partner", required=True)  
    phone =fields.Char(string='Phone' ,related='partner_id.phone')  
    whatsapp =fields.Char(string='Whatsapp' ,related='partner_id.mobile')  
    email =fields.Char(string='Email' ,related='partner_id.email')  
    goods_type = fields.Char(string="Goods Type")
    goods_weight = fields.Float(string="Goods Weight")
    shipping_location = fields.Char(string="Shipping Location", required=True)
    delivery_location = fields.Char(string="Delivery Location", required=True)
    image = fields.Binary(string="Image")
    responsible = fields.Many2one('res.users',string="Responsible",readonly="1",default=lambda self:self.env.user)
    state = fields.Selection([
        ('draft','Draft'),
        ('confirmed','Confirm'),
        ('under_consideration','Under Consideration'),
        ('done','Done'),
        ('canceled','Cancel'),

    ], string='Status', readonly=True, default='draft')

    def draft(self):    
        self.state = 'confirmed'
        
    def confirmed(self):    
        self.state = 'under_consideration'

    def under_consideration(self):    
        self.state = 'done'   

    def done(self):
        for rec in self:
            rec.state = 'canceled'
        return {
                'effect': {
                    'fadeout': 'slow',
                    'message': 'Trips Confirmed... Thanks You',
                    'type': 'rainbow_man',
                }
            }
    def delete_lines(self):
        for rec in self:
            rec.trips_linse = [(5, 0, 0)]

#     name_seq = fields.Char(string="Main ID", reversed=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))

#     @api.model
#     def create(self,vals):
#           if vals.get('name_seq', _('New')) == _('New'):
#                vals['name_seq'] = self.env['ir.sequence'].next_by_code('confine.main_it.sequence')or _('New')
#           result = super(TripsRequist, self).create(vals)
#           return result  
    
   