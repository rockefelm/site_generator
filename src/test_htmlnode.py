import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Boot.dev", [], {"href": "https://boot.dev", "target": "_smellyballs"})
        self.assertEqual(node.props_to_html(), ' href="https://boot.dev" target="_smellyballs"')
    
    def test_props_to_html_single(self):
        node = HTMLNode("img", None, [], {"src": "dog.png"})
        self.assertEqual(node.props_to_html(), ' src="dog.png"')
    
    def test_props_to_html_empty(self):
        node = HTMLNode("p", "No props here!", [], {})
        self.assertEqual(node.props_to_html(), '')
