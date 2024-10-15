plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    char_code = ord(char)
    
    if char.isalpha(): 
        if char == 'z':
            char_code = ord('a') 
        elif char == 'Z':
            char_code = ord('A') 
        else:
            char_code += 1
    
    encrypted_char = chr(char_code)
    
    encrypted_text += encrypted_char

print(f'Plain text: {plain_text}')
print(f'Encrypted text: {encrypted_text}')
    