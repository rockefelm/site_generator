from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode
from textnode import TextType, TextNode
from text_node_to_html_node import text_node_to_html_node
from text_to_children import text_to_children
from get_heading_level import get_heading_level
from strip_blockquote_markers import strip_blockquote_markers
from block_to_list_items import block_to_list_items

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        return HTMLNode("pre", None, [text_node_to_html_node(TextNode(block, TextType.CODE))])
    elif block_type == BlockType.PARAGRAPH:
        return HTMLNode("p", None, text_to_children(block))
    elif block_type == BlockType.HEADING:
        level, new_block = get_heading_level(block)
        return HTMLNode(f"h{level}", None, text_to_children(new_block))
    elif block_type == BlockType.QUOTE:
        cleaned_block = strip_blockquote_markers(block)
        return HTMLNode("blockquote", None, text_to_children(cleaned_block))
    elif block_type == BlockType.UNORDERED_LIST:
        items = block_to_list_items(block)  # ["first item", "second item", ...]
        li_nodes = []
        for item in items:
            # text_to_children(item) returns a list of inline nodes for this list item
            li_nodes.append(HTMLNode("li", None, text_to_children(item)))
        return HTMLNode("ul", None, li_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        items = block_to_list_items(block)  # ["first item", "second item", ...]
        li_nodes = []
        for item in items:
            # text_to_children(item) returns a list of inline nodes for this list item
            li_nodes.append(HTMLNode("li", None, text_to_children(item)))
        return HTMLNode("ol", None, li_nodes)
    else:
        raise Exception("not a valid BlockType")
    