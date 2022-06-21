# Conversion Tables

MASTER_HEX_TO_TEXT = {
    '09': '\t', '0A': '\n', '0D': '\r',
    '20': ' ', '21': '!', '22': '"', '23': '#', '24': '$', '25': '%', '26': '&', '27': "'", 
    '28': '(', '29': ')', '2A': '*', '2B': '+', '2C': ',', '2D': '-', '2E': '.', '2F': '/', 
    '30': '0', '31': '1', '32': '2', '33': '3', '34': '4', '35': '5', '36': '6', '37': '7', 
    '38': '8', '39': '9', '3A': ':', '3B': ';', '3C': '<', '3D': '=', '3E': '>', '3F': '?', 
    '40': '@', 
    '41': 'A', '42': 'B', '43': 'C', '44': 'D', '45': 'E', '46': 'F', '47': 'G', '48': 'H', 
    '49': 'I', '4A': 'J', '4B': 'K', '4C': 'L', '4D': 'M', '4E': 'N', '4F': 'O', '50': 'P', 
    '51': 'Q', '52': 'R', '53': 'S', '54': 'T', '55': 'U', '56': 'V', '57': 'W', '58': 'X', '59': 'Y', 
    '5A': 'Z', 
    '5B': '[', '5C': '\\','5D': ']', '5E': '^', '5F': '_', '60': '`', 
    '61': 'a', '62': 'b', '63': 'c', '64': 'd', '65': 'e', '66': 'f', '67': 'g', '68': 'h', '69': 'i', 
    '6A': 'j', '6B': 'k', '6C': 'l', '6D': 'm', '6E': 'n', '6F': 'o', '70': 'p', '71': 'q', '72': 'r', 
    '73': 's', '74': 't', '75': 'u', '76': 'v', '77': 'w', '78': 'x', '79': 'y', '7A': 'z', 
    '7B': '{', '7C': '|', '7D': '}', '7E': '~'}

MASTER_TEXT_TO_HEX = {
    '\t': '09', '\n': '0A', '\r': '0D', 
    ' ': '20', '!': '21', '"': '22', '#': '23', '$': '24', '%': '25', '&': '26', "'": '27', 
    '(': '28', ')': '29', '*': '2A', '+': '2B', ',': '2C', '-': '2D', '.': '2E', '/': '2F', 
    '0': '30', '1': '31', '2': '32', '3': '33', '4': '34', '5': '35', '6': '36', '7': '37', 
    '8': '38', '9': '39', ':': '3A', ';': '3B', '<': '3C', '=': '3D', '>': '3E', '?': '3F', 
    '@': '40', 
    'A': '41', 'B': '42', 'C': '43', 'D': '44', 'E': '45', 'F': '46', 'G': '47', 'H': '48', 
    'I': '49', 'J': '4A', 'K': '4B', 'L': '4C', 'M': '4D', 'N': '4E', 'O': '4F', 'P': '50', 
    'Q': '51', 'R': '52', 'S': '53', 'T': '54', 'U': '55', 'V': '56', 'W': '57', 'X': '58', 
    'Y': '59', 'Z': '5A', 
    '[': '5B', '\\': '5C', ']': '5D', '^': '5E', '_': '5F', '`': 
    '60', 'a': '61', 'b': '62', 'c': '63', 'd': '64', 'e': '65', 'f': '66', 'g': '67', 'h': '68', 
    'i': '69', 'j': '6A', 'k': '6B', 'l': '6C', 'm': '6D', 'n': '6E', 'o': '6F', 'p': '70', 'q': '71', 
    'r': '72', 's': '73', 't': '74', 'u': '75', 'v': '76', 'w': '77', 'x': '78', 'y': '79', 'z': '7A', 
    '{': '7B', '|': '7C', '}': '7D', '~': '7E'}



TEXT_TO_HEX = {
    '0':'30','1':'31','2':'32','3':'33','4':'34','5':'35',
    '6':'36','7':'37','8':'38','9':'39',
    ' ':'20',
    'A':'41','B':'42','C':'43','D':'44','E':'45',
    'F':'46','G':'47','H':'48','I':'49','J':'4A',
    'K':'4B','L':'4C','M':'4D','N':'4E','O':'4F',
    'P':'50','Q':'51','R':'52','S':'53','T':'54',
    'U':'55','V':'56','W':'57','X':'58','Y':'59','Z':'5A'}

HEX_TO_TEXT = {
    '30': '0', '31': '1', '32': '2', '33': '3', '34': '4', '35': '5', 
    '36': '6', '37': '7', '38': '8', '39': '9', 
    '20': ' ',
    '41': 'A', '42': 'B', '43': 'C', '44': 'D', '45': 'E', 
    '46': 'F', '47': 'G', '48': 'H', '49': 'I', '4A': 'J', 
    '4B': 'K', '4C': 'L', '4D': 'M', '4E': 'N', '4F': 'O', 
    '50': 'P', '51': 'Q', '52': 'R', '53': 'S', '54': 'T', 
    '55': 'U', '56': 'V', '57': 'W', '58': 'X', '59': 'Y', '5A': 'Z'
}

HEX_TO_BINARY = {
    '0' : "0000",'1' : "0001",'2' : "0010",'3' : "0011",
    '4' : "0100",'5' : "0101",'6' : "0110",'7' : "0111",
    '8' : "1000",'9' : "1001",'A' : "1010",'B' : "1011",
    'C' : "1100",'D' : "1101",'E' : "1110",'F' : "1111" }

BINARY_TO_HEX = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3', 
    '0100': '4', '0101': '5', '0110': '6', '0111': '7', 
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', 
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

BINARY_TO_DECIMAL = {
    '0000':0, '0001':1, '0010':2, '0011':3, '0100':4,
    '0101':5, '0110':6, '0111':7, '1000':8, '1001':9,
    '1010':10,'1011':11,'1100':12,'1101':13,'1110':14,'1111':15}

DECIMAL_TO_BINARY = {
    0: '0000', 1: '0001', 2: '0010', 3: '0011', 4: '0100', 
    5: '0101', 6: '0110', 7: '0111', 8: '1000', 9: '1001', 
    10: '1010', 11: '1011', 12: '1100', 13: '1101', 14: '1110', 15: '1111'}


# Valid key letters in hex
VALID_KEY_LETTERS = '0123456789ABCDEF'

#Values for the s and p boxes are taken from the textbook for accurate encryption and decryption

INITIAL_P_BOX = [
                58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

FINAL_P_BOX = [ 
                40, 8, 48, 16, 56, 24, 64, 32,
                39, 7, 47, 15, 55, 23, 63, 31,
                38, 6, 46, 14, 54, 22, 62, 30,
                37, 5, 45, 13, 53, 21, 61, 29,
                36, 4, 44, 12, 52, 20, 60, 28,
                35, 3, 43, 11, 51, 19, 59, 27,
                34, 2, 42, 10, 50, 18, 58, 26,
                33, 1, 41, 9, 49, 17, 57, 25]

EXPANSION_P_BOX = [
        32, 1 , 2 , 3 , 4 , 5 , 4 , 5,
        6 , 7 , 8 , 9 , 8 , 9 , 10, 11,
        12, 13, 12, 13, 14, 15, 16, 17,
        16, 17, 18, 19, 20, 21, 20, 21,
        22, 23, 24, 25, 24, 25, 26, 27,
        28, 29, 28, 29, 30, 31, 32, 1]

STRAIGHT_P_BOX = [
        16,  7, 20, 21, 29, 12, 28, 17,
        1,  15, 23, 26,  5, 18, 31, 10,
        2,   8, 24, 14, 32, 27,  3,  9,
        19, 13, 30,  6, 22, 11,  4, 25]

S_BOXES = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
            
        [   
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
   
        [ 
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
       
        [ 
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14] 
        ],
        
        [ 
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
       
        [ 
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
         
        [ 
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        
        [ 
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11] 
        ] 
    ]

KEY_COMPRESSION_P_BOX = [
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32 ]

roundKeys48 = []
roundKeys48_rev = []
roundKeysHEX = []

KEY_SHIFT_TABLE = [
    1,1,2,2,
    2,2,2,2,
    1,2,2,2,
    2,2,2,1]


class InvalidDESKeyLengthException(Exception):
    def __init__(self, invalidLength : int):
        super().__init__(f'Invalid Key Length: {invalidLength}')

class InvalidDESKeyException(Exception):
    def __init__(self, invalidLetter : str):
        super().__init__(f'Invalid Key Letter {invalidLetter}')

# Number system conversion functions
def textToHex(text : str) -> str:
    hex = ''
    for i in text:
        hex = hex + MASTER_TEXT_TO_HEX[i] 
    return hex

def hexToBin(hex : str) -> str:
    bin = ''
    for i in hex:
        bin = bin + HEX_TO_BINARY[i]
    return bin

def binToDec(bin : str) -> int:
    dec = BINARY_TO_DECIMAL[bin]
    return dec

def decToBin(dec : int) -> str:
    bin = DECIMAL_TO_BINARY[dec]
    return bin

def binToHex(bin : str) -> str:
    hex = ""
    for i in range(0, len(bin), 4):
        hex = hex + BINARY_TO_HEX[bin[i:i+4]]
    return hex

def hexToText(hex : str) -> str:
    print (f"HEX to be converted : {hex}")
    text = ""

    for i in range(0, len(hex), 2):
        text = text + MASTER_HEX_TO_TEXT[hex[i:i + 2]]

    return text

def checkKey(keyHEX : str) -> str:
    if len(keyHEX) != 14:
            raise InvalidDESKeyLengthException(len(keyHEX))
        
    for i in keyHEX:
        if i not in VALID_KEY_LETTERS:
            raise InvalidDESKeyException(i)

#Permuation Function
def permutation(input: str, box : list) -> str:
    output = ''
    #print(input)
    for i in range(len(box)):
        output = output + input[box[i] - 1]
    return output

#Left Shift Function
def leftShift(key28 : str, n : int) -> str:
    key = key28[n:] + key28[0:n]
    return key

# xor a and b
def xor(a : str, b  : str) -> str:
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result = result + '0'
        else:
            result = result + '1'
    return result

def resetState():
    global roundKeys48, roundKeysHEX
    roundKeys48 = []
    roundKeysHEX = []

def encryption(plaintext : str, keyHEX : str) -> str:
    resetState()
    
    ciphertextHEX = ''

    roundKeyGenerator(keyHEX)

    # Not needed when using master_table
    #plaintext = plaintext.replace('\n', ' ')

    plaintextHEX = textToHex(plaintext)
    print(f"Plaintext in HEX : {plaintextHEX}")

    plaintextBinary = hexToBin(plaintextHEX)
    #print(f"Plaintext in binary: {plaintextBinary}")

    # Encrypt blockwise
    for i in range (0, len(plaintextBinary), 64):

        block = plaintextBinary[i:i+64]

        if len(block) != 64:
            print("Padding while encrypting!")
            block = block + ('00100000' * (64 - len(block)))

        ciphertextBinary = encrypt(block)
        #print(f"Cipher Text in Binary is: {ciphertextBinary}")
        ciphertextHEX = ciphertextHEX + binToHex(ciphertextBinary)
        
    print(f"Cipher Text in Hex is: {ciphertextHEX}")
    return ciphertextHEX

def decryption(ciphertext : str, keyHEX : str) -> str:
    global roundKeys48, roundKeys48_rev
    
    resetState()

    plaintext = ''
    plaintextHEX = ''

    # Generating Round Keys
    roundKeyGenerator(keyHEX)
    roundKeys48 = roundKeys48_rev

    ciphertextHEX = ciphertext #textToHex(ciphertext)
    ciphertextBinary = hexToBin(ciphertextHEX)
    #print(f"Cipher Text in binary is :{ciphertextBinary}")

    # Decrypting blockwise
    for i in range(0, len(ciphertextBinary), 64):

        block = ciphertextBinary[i:i+64]

        if len(block) != 64:
            print("Padding while decrypting!")
            block = block + ('00100000' * (64 - len(block)))

        plaintextBinary = encrypt(block)

        #print(f"Plain text in binary is: {plaintextBinary}")
        plaintextHEX = plaintextHEX + binToHex(plaintextBinary)
        
    print(f"Plain text in hex is: {plaintextHEX}") 
    plaintext = hexToText(plaintextHEX)
    print(f"Plain text is: {plaintext}")

    return plaintext


#Takes 64 bit plain text and converts to 64 bit cipher text
def encrypt(plain64 : str) -> str:
    cipher64 = ''

    #Initial permutation
    plain64 = permutation(plain64, INITIAL_P_BOX)

    left32 = plain64[0:32]
    right32 = plain64[32:]

    # Round Function
    for i in range(16):
        
        # Expansion P Box
        pbox48 = permutation(right32, EXPANSION_P_BOX)

        # XOR
        xor48 = xor(pbox48, roundKeys48[i])

        # S-Box
        sbox32 = ''
        for j in range(8):
            bin6 = xor48[j*6:(j*6) + 6]
            val = S_BOXES[j][binToDec("00"+bin6[0]+bin6[5])][binToDec(bin6[1:5])]
            sbox32 = sbox32 + decToBin(val)
        
        # Straight P Box
        pbox32 = permutation(sbox32, STRAIGHT_P_BOX)

        # XOR with left
        xor32 = xor(left32, pbox32)

        # Left becomes result
        left32 = xor32

        # Swap left and right
        if (i != 15):
            left32, right32 = right32, left32


    combined64 = left32 + right32

    # Final Permutation
    cipher64 = permutation(combined64, FINAL_P_BOX)

    return cipher64

# Generates 16 48-bit round keys from 56-bit HEX key
def roundKeyGenerator(keyHEX : str):

    global roundKeys48, roundKeys48_rev

    key56 = hexToBin(keyHEX)
    
    leftKey28 = key56[0:28]
    rightKey28 = key56[0:56]

    for i in range(16):

        leftKey28 = leftShift(leftKey28, KEY_SHIFT_TABLE[i])
        rightKey28 = leftShift(rightKey28, KEY_SHIFT_TABLE[i])

        combined56 = leftKey28 + rightKey28

        roundKey48 = permutation(combined56, KEY_COMPRESSION_P_BOX)

        roundKeys48.append(roundKey48)
        roundKeysHEX.append(binToHex(roundKey48))

    roundKeys48_rev = roundKeys48[::-1]

    print(roundKeysHEX)

