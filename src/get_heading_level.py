def get_heading_level(block):
    count = 0
    for char in block:
        if char == "#":
            count += 1
        else:
            break
    level = min(count, 6)
    new_block = block[count:].strip()
    return level, new_block