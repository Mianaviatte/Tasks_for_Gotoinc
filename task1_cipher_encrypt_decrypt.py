# Write a simple cipher code: 
# Take all even bits of the string and concatenate them with all odd n times. 
# As a result, return the string.

# Example: 
# ("Abcdefghij", 1) -> "bdfhjacegi" 
# ("Abcdefghij", 2) -> "bdfhjacegi" -> "dhaeibfjcg"

# Write two methods / functions:
# encrypt (text, n)
# decrypt (encrypted_text, n)

# For both methods: 
# If the input string is empty or NULL, return the input string value 
# If n <= 0, # return the original value of the input string

def encrypt (text, n):
    
    if text is None or len(text) == 0 or n <= 0:
        return text
    
    for i in range(n):
        encrypted_text = text[1::2] + text[::2]

    return encrypted_text.lower()


def decrypt (encrypted_text, n):

    if encrypted_text is None or len(encrypted_text) == 0 or n <= 0:
        return encrypted_text

    for i in range(n):
        result_list = []
        encrypted_list = list(encrypted_text)
        
        for j in range(len(encrypted_text)//2):
            result_list.append( encrypted_list[j + int((len(encrypted_text) / 2))])
            result_list.append( encrypted_list[j])
        
        if len(encrypted_text) % 2 == 1:
            result_list.append( encrypted_list[len(encrypted_text) - 1])

    result_text = ''.join(result_list)

    return result_text

# Testing the cipher No. 1
test_text = input('Insert your password, please: ') 
n = int(input('How many times do you wish the hash to be mixed? '))

print(f'Here is your password: {test_text} ciphered into {encrypt(test_text, n)} after {n} times.')
print(f'Back to my password: {decrypt(encrypt(test_text, n), n)}')

# Testing the cipher No. 2
stats = 0
attempts = 70

for i in range(attempts):
    test_encrypt = encrypt(test_text, i)

    if test_text.lower() == decrypt(test_encrypt, i):
        stats += 1

print(f'There were successful {stats} encryptions and decryptions of {attempts} attempts.')