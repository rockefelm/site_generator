import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a different text node", TextType.ITALIC)
        node4 = TextNode("This is a text node", TextType.CODE)
        node5 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node3, node4)
        self.assertEqual(node, node2)
        self.assertEqual(node, node5)
        self.assertEqual(node2,node5)



if __name__ == "__main__":
    unittest.main()