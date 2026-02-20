"""
Morse Code Converter (Numbers Only)
This script converts between numeric digits and their corresponding 
Morse code representations.
"""

# Mapping of numbers to their standard 5-character Morse code equivalents
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
MORSE = [
    '-----', '*----', '**---', '***--', '****-', 
    '*****', '****-', '***--', '**...', '*---.'
]

def main():
    print("--- Numeric Morse Code Converter ---")
    print("1. Number to Morse")
    print("2. Morse to Number")
    
    choice = input("Select conversion direction (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid selection. Please run the script again and choose 1 or 2.")
        return

    value = input("Enter value to be converted: ")

    if choice == '1':
        # Number to Morse
        # We remove spaces in case the user entered "1 2 3"
        clean_value = value.replace(" ", "")
        result = []
        
        for char in clean_value:
            if char in NUMBERS:
                index = NUMBERS.index(char)
                result.append(MORSE[index])
            else:
                print(f"Warning: '{char}' is not a number. Skipping.")
        
        if result:
            print("Result:", " ".join(result))
        else:
            print("Error: No valid numbers were provided.")

    elif choice == '2':
        # Morse to Number
        # Handles input with multiple spaces or different separators
        morse_chars = value.split()
        result = []
        
        for m_char in morse_chars:
            if m_char in MORSE:
                index = MORSE.index(m_char)
                result.append(NUMBERS[index])
            else:
                print(f"Warning: Unknown Morse sequence '{m_char}' ignored.")
        
        if result:
            print("Result:", "".join(result))
        else:
            print("Error: No valid Morse code sequences found. (Note: use spaces between codes)")

if __name__ == "__main__":
    main()