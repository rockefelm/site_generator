from blocktype import BlockType, block_to_block_type
from htmlnode import HTMLNode, ParentNode
from textnode import TextType, TextNode
from text_node_to_html_node import text_node_to_html_node
from text_to_children import text_to_children
from get_heading_level import get_heading_level
from strip_blockquote_markers import strip_blockquote_markers
from block_to_list_items import block_to_list_items
import re

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.CODE:
        lines = block.split('\n')
        if lines[0].startswith("```"):
            lines = lines[1:]  # remove first line
        if lines and lines[-1].startswith("```"):
            lines = lines[:-1]  # remove last line
        code_contents = "\n".join(lines) + "\n"
        return ParentNode("pre", [text_node_to_html_node(TextNode(code_contents, TextType.CODE))])
    elif block_type == BlockType.PARAGRAPH:
        clean_block = block.replace('\n', ' ').strip()
        return ParentNode("p", text_to_children(clean_block))
    elif block_type == BlockType.HEADING:
        level, new_block = get_heading_level(block)
        return ParentNode(f"h{level}", text_to_children(new_block))
    elif block_type == BlockType.QUOTE:
        cleaned_block = strip_blockquote_markers(block)
        return ParentNode("blockquote", text_to_children(cleaned_block))
    elif block_type == BlockType.UNORDERED_LIST:
        items = block_to_list_items(block)  # ["first item", "second item", ...]
        li_nodes = []
        for item in items:
            # text_to_children(item) returns a list of inline nodes for this list item
            li_nodes.append(ParentNode("li", text_to_children(item)))
        return ParentNode("ul", li_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        items = block_to_list_items(block)  # ["first item", "second item", ...]
        li_nodes = []
        for item in items:
            # text_to_children(item) returns a list of inline nodes for this list item
            li_nodes.append(ParentNode("li", text_to_children(item)))
        return ParentNode("ol", li_nodes)
    else:
        raise Exception("not a valid BlockType")
    