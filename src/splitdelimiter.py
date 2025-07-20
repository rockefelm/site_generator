from textnode import *
from htmlnode import *
from main import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    """
    Splits a list of TextNode objects into multiple TextNode objects based on a delimiter.
    
    Args:
        old_nodes (list): List of TextNode objects to be split.
        delimiter (str): The delimiter to split the text nodes by.
        text_type (TextType): The type of text for the new TextNode objects.
    
    Returns:
        list: A new list of TextNode objects after splitting.
    """
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception("Unmatched delimiter")
        for idx, part in enumerate(parts):
            if part != "":
                if idx % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT, node.url))
                else:
                    new_nodes.append(TextNode(part, text_type, node.url))           
    
    return new_nodes