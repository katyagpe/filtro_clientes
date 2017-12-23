# -*- coding: utf-8 -*-
from odoo import http

# class FiltroClientes(http.Controller):
#     @http.route('/filtro_clientes/filtro_clientes/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/filtro_clientes/filtro_clientes/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('filtro_clientes.listing', {
#             'root': '/filtro_clientes/filtro_clientes',
#             'objects': http.request.env['filtro_clientes.filtro_clientes'].search([]),
#         })

#     @http.route('/filtro_clientes/filtro_clientes/objects/<model("filtro_clientes.filtro_clientes"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('filtro_clientes.object', {
#             'object': obj
#         })