from enum import Enum

class TextType(Enum):
    """
    Enum representing different types of text nodes.
    """
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    """
    Class representing a text node with a type and content.
    """
    def __init__(self, text, text_type, url=None):
        self.text_type = text_type
        self.text = text
        self.url = url

    def __eq__(self, value):
        return (self.text == value.text and
                self.text_type == value.text_type and
                self.url == value.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"