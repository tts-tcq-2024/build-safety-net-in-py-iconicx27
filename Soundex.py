def get_soundex_code(c):
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    return mapping.get(c, '0')  # Default to '0' for non-mapped characters


def process_character(soundex, prev_code, char):
    code = get_soundex_code(char)
    if code != '0' and code != prev_code:
        soundex += code
    return soundex, code


def pad_soundex(soundex):
    return soundex.ljust(4, '0')


def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = name[0].upper()
    prev_code = get_soundex_code(soundex)

    for char in name[1:]:
        if len(soundex) == 4:
            break
        soundex, prev_code = process_character(soundex, prev_code, char)

    return pad_soundex(soundex)
