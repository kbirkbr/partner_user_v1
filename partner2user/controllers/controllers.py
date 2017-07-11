# -*- coding: utf-8 -*-
from odoo import http

# class PartnerUser(http.Controller):
#     @http.route('/partner_user/partner_user/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/partner_user/partner_user/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('partner_user.listing', {
#             'root': '/partner_user/partner_user',
#             'objects': http.request.env['partner_user.partner_user'].search([]),
#         })

#     @http.route('/partner_user/partner_user/objects/<model("partner_user.partner_user"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('partner_user.object', {
#             'object': obj
#         })