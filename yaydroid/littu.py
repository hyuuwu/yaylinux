import base64



#littu

#Little
#Installable
#Translator
#To
#Understand Base64
def crypt(inp, fileee):
    """
    Base64 encodes the given input string and saves it to a file.
    """


    # The input to b64encode must be bytes. We encode the string to bytes using UTF-8.
    input_bytes = inp.encode('utf-8')
    encoded_bytes = base64.b64encode(input_bytes)

    # To write the encoded data to a file in text mode, we must decode it back to a string.
    encoded_string = encoded_bytes.decode('utf-8')

    with open(fileee, 'w') as f:
        f.write(encoded_string)

def cryptfile(filepath):
    """
    Reads the content of a text file and 'encrypts' it using the crypt function.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        crypt(content)
        print(f"Successfully encoded the content of '{filepath}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt(fileuwant):
    """
    Reads a Base64 encoded file, decodes it, and returns the original string.
    """
    try:
        with open(fileuwant, 'r', encoding='utf-8') as f:
            encoded_string = f.read()

        # The input to b64decode must be bytes. We encode the string to bytes using UTF-8.
        encoded_bytes = encoded_string.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)

        # Decode the bytes back to a string.
        original_string = decoded_bytes.decode('utf-8')
        return original_string
    except FileNotFoundError:
        print(f"Error: The file '{fileuwant}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

# ---How 2 Use
# littu.crypt(the text you want to encrypt, the file u want to save it to)
# littu.decrypt(the file u gon decrypt)
# littu.cryptfile(the file u want to encrypt)
#ex:
#
#littu.crypt("i miss my ex", file.txt)
#that is going to encrypt the text into base64,and save it into an file
#
#
#
# writtn by hyuuwu, AkA Luiz
