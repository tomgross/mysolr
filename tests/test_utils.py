#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from mysolr import mysolr


class AddXmlTestCase(unittest.TestCase):

    def test_add_xml(self):
        self.assertEqual(mysolr._get_add_xml([{'id':5, 'foo':'bar'}]),
                         ('<add overwrite="true"><doc><field name="foo">bar'
                          '</field><field name="id">5</field></doc></add>'))

    def test_add_xml_nooverwrite(self):
        self.assertEqual(mysolr._get_add_xml([{'id':5, 'foo':'bar'}],
                         overwrite=False),
                         ('<add overwrite="false"><doc><field name="foo">bar'
                          '</field><field name="id">5</field></doc></add>'))

    def test_add_xml_commit_within(self):
        self.assertEqual(mysolr._get_add_xml([{'id':5, 'foo':'bar'}],
                         commit_within=2.0),
                         ('<add overwrite="true" commitWithin="2.0"><doc>'
                          '<field name="foo">bar</field><field name="id">5'
                          '</field></doc></add>'))

    def test_add_xml_commit_doc_boost(self):
        self.assertEqual(mysolr._get_add_xml([{'id':7, 'foo':'bar'}],
                         boost_values={'':2.3}),
                         ('<add overwrite="true"><doc boost="2.3">'
                          '<field name="foo">bar</field><field name="id">7'
                          '</field></doc></add>'))

    def test_add_xml_commit_field_boost(self):
        self.assertEqual(mysolr._get_add_xml([{'id':7, 'foo':'bar'}],
                         boost_values={'foo':4.2}),
                         ('<add overwrite="true"><doc>'
                          '<field name="foo" boost="4.2">bar</field>'
                          '<field name="id">7</field></doc></add>'))

if __name__ == '__main__':
    unittest.main()
