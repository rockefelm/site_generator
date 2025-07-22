def block_to_list_items(block):
    items = []
    for line in block.split('\n'):
        line = line.strip()
        if not line:
            continue
        elif line.startswith(("-", "*")):
            # unordered, remove first 2 characters
            items.append(line[2:].strip())
        elif line and line[0].isdigit():
            # ordered, remove digits and leading dot
            parts = line.split('.', 1)
            if len(parts) == 2:
                items.append(parts[1].strip())
        # you may want to handle edge cases here
    return items