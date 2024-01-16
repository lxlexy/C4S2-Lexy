def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
    }
    text_morse = []
    text = text.upper()

    for letter in text:
        if letter == " ":  # Check if the character is a space
            text_morse.append(" / ")  # Add a slash for word separation
        elif letter in morse_code_dict:
            text_morse.append(morse_code_dict[letter] + " ")  # Append the Morse code for the letter with a space

    return "".join(text_morse).strip()  # Strip to remove any trailing space