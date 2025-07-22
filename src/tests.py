import unittest
from htmlnode import *
from textnode import *
from text_node_to_html_node import text_node_to_html_node
from splitdelimiter import split_nodes_image, split_nodes_link, split_nodes_delimiter
from text_to_textnodes import text_to_textnodes
from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from markdown_to_html_node import markdown_to_html_node

class TestHTMLNode(unittest.TestCase):
    def test_heading(self):
        md = "# Title Heading\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Title Heading</h1></div>"
        )

    def test_heading_level_and_inline(self):
        md = "### Level 3 with **bold**\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h3>Level 3 with <b>bold</b></h3></div>"
        )
    def test_blockquote(self):
        md = "> Quoth the raven _nevermore_\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Quoth the raven <i>nevermore</i></blockquote></div>"
        )
    def test_unordered_list(self):
        md = "- apples\n- bananas\n- **boldfruit**\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>apples</li><li>bananas</li><li><b>boldfruit</b></li></ul></div>"
        )
    def test_ordered_list(self):
        md = "1. first\n2. _second_\n3. third\n"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>first</li><li><i>second</i></li><li>third</li></ol></div>"
        )
    def test_mixed_blocks(self):
        md = (
            "# Shopping List\n"
            "\n"
            "> Remember: _fresh_ only!\n"
            "\n"
            "- milk\n"
            "- eggs\n"
            "- bread\n"
        )
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>Shopping List</h1><blockquote>Remember: <i>fresh</i> only!</blockquote><ul><li>milk</li><li>eggs</li><li>bread</li></ul></div>"
        )