from textnode import TextNode, TextType
from splitdelimiter import split_nodes_image, split_nodes_link, split_nodes_delimiter

def text_to_textnodes(text):
    """
    Converts a text string into a list of TextNode objects, splitting it into text, image, and link nodes.
    
    Args:
        text (str): The input text string to be converted.
    
    Returns:
        list: A list of TextNode objects representing the text, images, and links.
    """
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, '`', TextType.CODE)
    nodes = split_nodes_delimiter(nodes, '**', TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, '__', TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, '_', TextType.ITALIC)

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes