# -*- coding: utf-8 -*-
from odoo import http

# class Confine(http.Controller):
#     @http.route('/confine/confine/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/confine/confine/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('confine.listing', {
#             'root': '/confine/confine',
#             'objects': http.request.env['confine.confine'].search([]),
#         })

#     @http.route('/confine/confine/objects/<model("confine.confine"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('confine.object', {
#             'object': obj
#         })