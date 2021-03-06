# -*- coding: utf-8 -*-
"""
    __init__

    Test Suite

    :copyright: (c) 2014 by Openlabs Technologies & Consulting (P) Limited
    :license: BSD, see LICENSE for more details.
"""
import unittest

import trytond.tests.test_tryton

from tests.test_incoterm import IncotermTestCase
from tests.test_sale import TestSale


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(IncotermTestCase),
        unittest.TestLoader().loadTestsFromTestCase(TestSale),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
