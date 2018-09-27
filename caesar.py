def alphabet_position(letter):
    letter_n = letter.lower()
    return (ord(letter_n)-97)

def rotate_character(char,rot):
    up = 0
    check = ord(char)
    if (check < 65) or (90 < check < 97) or (check > 122):
        return char
    if check < 97:
        up = 1
    bet = alphabet_position(char)
    boat = bet + rot
    new = boat%26 
    letter = (chr(new+97))
    if up == 1:
        letter = letter.upper()
    return letter

def encrypt(text,rot):
    encrypted = ""
    for char in text:
        encrypted = encrypted + rotate_character(char,rot)
    return encrypted
