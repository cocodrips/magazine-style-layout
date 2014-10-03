import unittest
import page_generator
import os

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.path = os.path.dirname(os.path.abspath(__file__))
        self.generator = page_generator.PageGenerator()

    def testParse(self):
        pages = self.generator.generate_from_json(self.path + '/sample/sample1.json')
        self.assertEqual(pages[0][1].priority, 2)

        pages = self.generator.generate_from_json(self.path + '/sample/sample2.json')
        self.assertEqual(len(pages[1][2]), 2)

