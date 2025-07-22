from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def block_to_block_type(block):
    lines = block.splitlines()
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    elif all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    elif re.match(r'^#{1,6} ', block):
        return BlockType.HEADING
    elif all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST
    elif len(lines) > 0:  # Make sure we have lines to check
        is_ordered_list = True
        for i, line in enumerate(lines):
            expected_num = i + 1
            # Check if line matches pattern AND has correct number
            match = re.match(r'^(\d+)\. ', line)
            if not match or int(match.group(1)) != expected_num:
                is_ordered_list = False
                return BlockType.PARAGRAPH
        
        if is_ordered_list:
            return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH