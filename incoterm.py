# -*- coding: utf-8 -*-
"""
    incoterm

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
from trytond.pool import Pool
from trytond.model import fields
from trytond.pyson import Eval
from trytond.transaction import Transaction

__all__ = ['Incoterm']


class Incoterm(object):
    'Incoterm Mixin'

    year = fields.Selection([
            ('2000', '2000'),
            ('2010', '2010'),
        ], 'Year', required=True, select=True
    )
    abbrevation = fields.Selection([
            ('EXW', 'Ex Works'),
            ('CPT', 'Carriage Paid To'),
            ('CIP', 'Carrier and Insurance Paid to'),
            ('DAT', 'Delivered at Terminal'),
            ('DAP', 'Delivered at Place'),
            ('FAS', 'Free Alongside Ship'),
            ('FOB', 'Free on Board'),
            ('CFR', 'Cost and Freight'),
            ('CIF', 'Cost, Insurance and Freight'),
            ('DAF', 'Delivered at Frontier'),
            ('DES', 'Delivered Ex Ship'),
            ('DEQ', 'Delievered Ex Quay'),
            ('DDU', 'Delivered Duty Unpaid'),
        ], 'Abbrevation'
    )
    value = fields.Numeric(
        'Value', digits=(16, Eval('currency_digits', 2)),
        depends=['currency_digits']
    )
    currency = fields.Many2One('currency.currency', 'Currency')
    currency_digits = fields.Function(
        fields.Integer('Value', on_change_with=['currency'],
            depends=['currency']
        ), 'on_change_with_currency'
    )

    def get_rec_name(self, name):
        return "%s -(Incoterm %s)" % (self.abbrevation, self.year)

    @staticmethod
    def default_year():
        return '2010'

    @staticmethod
    def default_currency():
        Company = Pool().get('company.company')

        company_id = Transaction().context.get('company')
        if company_id:
            return Company(company_id).currency.id
        return None

    def on_change_with_currency_digits(self, name=None):
        if self.currency:
            return self.currency.digits
        return 2
