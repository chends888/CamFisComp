import numpy as np

# ray = [1,2,3,4,5]
# print(ray)

# ray = np.array_split(ray, 2)

# print(ray)

# stri = "oiuygv 88oiugvcbhjok88kjhgcvhjk88"

# stri = stri.split("88")

# print(stri)

# pack = b"331233"

# print (pack.find(b"33"))

# dado = "./enviar/Screenshot.png"
# txBuffer = open(dado, 'rb').read()
# print (txBuffer)


def crc16(data: bytes):
    '''
    CRC-16-CCITT Algorithm
    '''
    data = bytearray(data)
    print(data)
    poly = 0x8408
    crc = 0xFFFF
    for b in data:
        cur_byte = 0xFF & b
        for _ in range(0, 8):
            if (crc & 0x0001) ^ (cur_byte & 0x0001):
                crc = (crc >> 1) ^ poly
            else:
                crc >>= 1

            cur_byte >>= 1

    crc = (~crc & 0xFFFF)
    crc = (crc << 8) | ((crc >> 8) & 0xFF)

    return crc



# print(crc16(121))

# dado = "./enviar/Screenshot2.png"
# dado = open(dado, 'rb').read()
# dado = b'\x08\xce\xf5\xe8\x0e'
# print (int.from_bytes(dado, byteorder='big'))

# dadoint = int.from_bytes(dado, byteorder='big')

# print (crc16(dado))
# print (crc16(dadoint))

# head = (len(dado)).to_bytes(7, byteorder='big')
# print (head)


ray = [1,2,3,4,5]

ray[1:2] = 9
print (ray)