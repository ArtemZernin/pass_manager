
STROKE = '1234567890@.qwertyuiopasdfghjklzxcvbnm_ !?QWERTYUIOPASDFGHJKLZXCVBNM'

def find_letter(letter):
    num = 0
    for l in STROKE:
        if l == letter:
            return num
        num += 1
    return 'err'

def encode_message(passw: str, message: str) -> str:
    coded_message = ''
    num_passw = 0
    for letter in message:    
        coded_message +=' 0x' + str(find_letter(letter) + find_letter(passw[num_passw]))
        num_passw += 1
        if num_passw == len(passw):
            num_passw = 0
    return coded_message

def decode_message(passw: str, coded_message: str) -> str:
    message = ''
    num_passw = 0
    for word in coded_message.split(' 0x'):
        if word.isdigit():
            message += STROKE[int(word) - find_letter(passw[num_passw])]
            num_passw += 1
            if num_passw == len(passw):
                num_passw = 0
    return message

if __name__ == "__main__":
    s = str(input('message: '))
    passw = str(input('password: '))
    out = encode_message(passw, s)
    print(out)
    print(decode_message(passw, out))
    