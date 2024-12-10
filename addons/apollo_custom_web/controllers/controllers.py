# -*- coding: utf-8 -*-
# from odoo import http


# class ApolloCustomWeb(http.Controller):
#     @http.route('/apollo_custom_web/apollo_custom_web', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apollo_custom_web/apollo_custom_web/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('apollo_custom_web.listing', {
#             'root': '/apollo_custom_web/apollo_custom_web',
#             'objects': http.request.env['apollo_custom_web.apollo_custom_web'].search([]),
#         })

#     @http.route('/apollo_custom_web/apollo_custom_web/objects/<model("apollo_custom_web.apollo_custom_web"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apollo_custom_web.object', {
#             'object': obj
#         })
