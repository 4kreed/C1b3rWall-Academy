import base64

# Source of raw data encoded in base64- https://pastebin.com/prRSPN5G

with open('encoded_text.txt', 'r', encoding='utf-8') as file:
    data = file.read()
    data += '=' * (-len(data) % 4)
    numero = int(input("How many times do you want to decode it? "))
    for i in range(1, numero+1):
        try:
            data = base64.b64decode(data)
            print(data)
            print('\n')
        except:
            print("Data couldn't be decoded. Last data was:")
            print(data)
            break
