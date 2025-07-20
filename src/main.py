from textnode import *
from htmlnode import *

def text_node_to_html_node(text_node):
    """
    Converts a TextNode to an HTMLNode based on its type.
    """
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown TextType: {text_node.text_type}")

def main():
    image_node = TextNode("Image alt text", TextType.IMAGE, "https://example.com/image.jpg")
    html_node = text_node_to_html_node(image_node)
    print(html_node.to_html())



main()  

