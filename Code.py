Binary_List = {
        '01000001': 'A', '01000010': 'B', '01000011': 'C', '01000100': 'D',
    '01000101': 'E', '01000110': 'F', '01000111': 'G', '01001000': 'H',
    '01001001': 'I', '01001010': 'J', '01001011': 'K', '01001100': 'L',
    '01001101': 'M', '01001110': 'N', '01001111': 'O', '01010000': 'P',
    '01010001': 'Q', '01010010': 'R', '01010011': 'S', '01010100': 'T',
    '01010101': 'U', '01010110': 'V', '01010111': 'W', '01011000': 'X',
    '01011001': 'Y', '01011010': 'Z', '00110000': '0', '00110001': '1',
    '00110010': '2', '00110011': '3', '00110100': '4', '00110101': '5',
    '00110110': '6', '00110111': '7', '00111000': '8', '00111001': '9'
}

def binary_translator(binary_code):
    words = binary_code.split(' ')
    decoded_message = []

    for x in words:
        letters = x.split()
        decoded_word = ''.join(Binary_List[letter] for letter in letters)
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)

user_input = input("Enter Binary code: ")
decoded_message = binary_translator(user_input)
print(f"Translation: {decoded_message}")
