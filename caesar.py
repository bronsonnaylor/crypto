def alphabet_position(letter):
    compare = ord("a")
    number = ord(letter.lower()) - compare
    return number

def rotate_character(char, rot):
    if char.isalpha():
        char_number = (alphabet_position(char) + rot) % 26
        if ord(char) > ord("Z"):
            character = chr(char_number + ord("a"))
        else:
            character = chr(char_number + ord("A"))
    else:
        character = char
    return character

def encrypt(text, rot):
    encryption = ""
    for i in text:
        encryption += rotate_character(i, rot)
    return encryption


def main():
    print(encrypt(input("What message would you like to encrypt?"), int(input("How many rotations?"))))

if __name__ == "__main__":
    main()
