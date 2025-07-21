import unittest
from htmlnode import *
from textnode import *
from text_node_to_html_node import text_node_to_html_node
from splitdelimiter import split_nodes_image, split_nodes_link, split_nodes_delimiter
from text_to_textnodes import text_to_textnodes

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
        print(new_nodes)

    def test_text_to_textnodes_basic(self):
        text = "Hello **bold** and `code` and a [link](example.com)!"
        nodes = text_to_textnodes(text)
        expected = [
            TextNode("Hello ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "example.com"),
            TextNode("!", TextType.TEXT),
        ]
        self.assertEqual(nodes, expected)
        print(nodes)