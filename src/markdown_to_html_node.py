from markdown_to_blocks import markdown_to_blocks
from blocktype import BlockType, block_to_block_type
from block_to_html_node import block_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in blocks:
        html_nodes.append(block_to_html_node(block))
    parent_node = ParentNode("div", html_nodes)
    return parent_node


            