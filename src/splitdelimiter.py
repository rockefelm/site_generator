from textnode import *
from htmlnode import *
from extractors import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    """
    Splits a list of TextNode objects into multiple TextNode objects based on image markdown syntax.
    
    Args:
        old_nodes (list): List of TextNode objects to be split.
    
    Returns:
        list: A new list of TextNode objects after splitting.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        image_parts = extract_markdown_images(node.text)
        if not image_parts:
            new_nodes.append(node)
            continue
        image_markdown = f"![{image_parts[0][0]}]({image_parts[0][1]})"
        parts = node.text.split(image_markdown) 
        if parts[0]:
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(image_parts[0][0], TextType.IMAGE, image_parts[0][1]))
        if parts[1]:
            remaining_nodes = split_nodes_image([TextNode(parts[1], TextType.TEXT)])
            new_nodes.extend(remaining_nodes)
        
    
    return new_nodes

def split_nodes_link(old_nodes):
    """
    Splits a list of TextNode objects into multiple TextNode objects based on link markdown syntax.
    
    Args:
        old_nodes (list): List of TextNode objects to be split.
    
    Returns:
        list: A new list of TextNode objects after splitting.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        link_parts = extract_markdown_links(node.text)
        if not link_parts:
            new_nodes.append(node)
            continue
        link_markdown = f"[{link_parts[0][0]}]({link_parts[0][1]})"
        parts = node.text.split(link_markdown) 
        if parts[0]:
            new_nodes.append(TextNode(parts[0], TextType.TEXT))
        new_nodes.append(TextNode(link_parts[0][0], TextType.LINK, link_parts[0][1]))
        if parts[1]:
            remaining_nodes = split_nodes_link([TextNode(parts[1], TextType.TEXT)])
            new_nodes.extend(remaining_nodes)
        
    
    return new_nodes