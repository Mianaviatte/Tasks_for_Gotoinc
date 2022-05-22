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
    
    while text is None:
        try: 
            text = input('Please, insert your password: ')
            encrypted_text = 

            print(encrypted_text)

        except TypeError:
            print('Input is invalid.')

        except:
            print('Something went extremely wrong.')    


def decrypt (encrypted_text, n):
    while encrypted_text is None:
        try: 
            encrypted_text = 
            result_text = 

            print(result_text)


        except TypeError:
            print('Input is invalid.')

        except:
            print('Something went extremely wrong.')    


    
