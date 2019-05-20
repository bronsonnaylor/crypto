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

def vig_encrypt(text, key):
    key_iterator = 0
    key_list = []
    char_list = []
    for character in key:
        key_list.append(character)
    for each in text:
        if each.isalpha():
            key_letter = key_list[key_iterator % len(key)]
            char_list.append(rotate_character(each, alphabet_position(key_letter)))
            key_iterator += 1
    return char_list

def main():
    print(vig_encrypt(input("What message would you like to encrypt?"), input("What is your Keyword?")))

if __name__ == "__main__":
    main()
