# -*- coding: utf-8 -*-
#from odoo import models, api, fields
import logging

from openerp import api, fields, models, _ 
from openerp.exceptions import UserError, ValidationError
from openerp.tools import DEFAULT_SERVER_DATE_FORMAT as DF


_logger = logging.getLogger(__name__)

class SaleOrderLine(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    partner_id = fields.Many2one('res.partner',string="Customer",required=True)