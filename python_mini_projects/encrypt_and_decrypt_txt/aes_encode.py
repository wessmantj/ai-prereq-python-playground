from cryptography.fernet import Fernet
from lorem_text import lorem

extra = lorem.sentence() # add extra text

message_str = ("Hello, this is a secret message that needs to be encoded. Travis is the recipient and he needs more text to use so he installed lorem ipsum." + extra) # the message to be encoded

message_bytes = message_str.encode('utf-8') # turn to bytes

print(f"Original message (bytes): {message_bytes}\n") # print to terminal for reference

# generate a key 
key = Fernet.generate_key()

# save in variable
fernet = Fernet(key)

# encrypt the single bytes object
token = fernet.encrypt(message_bytes)
print(f"Encrypted token: {token}\n")

# decrypt the token and decode the result back to a string
decrypted_message_bytes = fernet.decrypt(token)
decrypted_message_str = decrypted_message_bytes.decode('utf-8')

print(f"Decrypted Message: {decrypted_message_str}")