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


if __name__ == '__main__':
    unittest.main()
