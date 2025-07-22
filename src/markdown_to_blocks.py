

def markdown_to_blocks(markdown):
    text_nodes = []
    lines = markdown.split('\n\n')
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:
            text_nodes.append(stripped_line)
    return text_nodes

                         