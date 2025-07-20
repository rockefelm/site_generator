import unittest
from htmlnode import *

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

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_bold(self):
        node = LeafNode("b", "Bold text")
        self.assertEqual(node.to_html(), "<b>Bold text</b>")

    def test_leaf_to_html_italic(self):
        node = LeafNode("i", "Italic text")
        self.assertEqual(node.to_html(), "<i>Italic text</i>")