# -*- coding: utf-8 -*-
"""

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta
from incoterm import Incoterm

__all__ = ['Sale', 'SaleIncoterm']
__metaclass__ = PoolMeta


class Sale:
    'Sale'
    __name__ = 'sale.sale'

    incoterms = fields.One2Many('sale.incoterm', 'sale', 'Sales Incoterm')


class SaleIncoterm(Incoterm, ModelSQL, ModelView):
    'Sale Incoterm'
    __name__ = 'sale.incoterm'

    sale = fields.Many2One('sale.sale', 'Sale', required=True)
