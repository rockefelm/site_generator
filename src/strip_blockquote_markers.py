

def strip_blockquote_markers(block):
    lines = block.split('\n')
    cleaned_lines = []
    for line in lines:
        if line.startswith(">"):
            line = line[1:]
            if line.startswith(" "):
                line = line[1:]
        cleaned_lines.append(line)
    return "\n".join(cleaned_lines)