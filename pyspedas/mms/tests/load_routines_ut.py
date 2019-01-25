#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from ...mms import mms_load_fgm, mms_load_scm, mms_load_fpi, mms_load_hpca, mms_load_eis, mms_load_feeps, mms_load_edp, mms_load_aspoc
from ...utilities.data_exists import data_exists

class FGMLoadTestCases(unittest.TestCase):
    def test_load_default_data(self):
        data = mms_load_fgm()
        self.assertTrue(data_exists('mms1_fgm_b_gse_srvy_l2'))

    def test_load_multiple_sc(self):
        data = mms_load_fgm(probe=['1', '2', '3', '4'])
        self.assertTrue(data_exists('mms1_fgm_b_gse_srvy_l2'))
        self.assertTrue(data_exists('mms2_fgm_b_gse_srvy_l2'))
        self.assertTrue(data_exists('mms3_fgm_b_gse_srvy_l2'))
        self.assertTrue(data_exists('mms4_fgm_b_gse_srvy_l2'))

    def test_load_brst_data(self):
        data = mms_load_fgm(data_rate='brst', trange=['2015-10-16/13:00', '2015-10-16/13:10'])
        self.assertTrue(data_exists('mms1_fgm_b_gse_brst_l2'))

class SCMLoadTestCases(unittest.TestCase):
    def test_load_default_data(self):
        data = mms_load_scm()
        self.assertTrue(data_exists('mms1_scm_acb_gse_scsrvy_srvy_l2'))

    def test_load_multiple_sc(self):
        data = mms_load_scm(probe=['1', '2', '3', '4'])
        self.assertTrue(data_exists('mms1_scm_acb_gse_scsrvy_srvy_l2'))
        self.assertTrue(data_exists('mms2_scm_acb_gse_scsrvy_srvy_l2'))
        self.assertTrue(data_exists('mms3_scm_acb_gse_scsrvy_srvy_l2'))
        self.assertTrue(data_exists('mms4_scm_acb_gse_scsrvy_srvy_l2'))

    def test_load_brst_data(self):
        data = mms_load_scm(data_rate='brst', trange=['2015-10-16/13:00', '2015-10-16/13:10'])
        self.assertTrue(data_exists('mms1_scm_acb_gse_scb_brst_l2'))

if __name__ == '__main__':
    unittest.main()