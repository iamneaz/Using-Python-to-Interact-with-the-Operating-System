def character_frequency(filename):
    """Counts the frequency of each character in the given file."""
    #   First try to open the file
    try:
        file = open(filename)
    except OSError:
        return None

    #   Now process the file
    characters = {}
    for line in file:
        for char in line:
            characters[char] = characters.get(char, 0) + 1
    file.close()
    return characters
