from django.http import HttpResponse
from django.shortcuts import render
import operator
import re
import datetime as d


# from wordcount.hex_key import *


def hex(request):
    return render(request, 'hex.html')


def home2(request):
    return render(request, 'hex.html')


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            # add to dictionary or increase number
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1

    sorted_words = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(wordlist),
                                          'sorted_words': sorted_words})


def about(request):
    return render(request, 'about.html')


def capk(request):
    return render(request, 'capk.html')


def capk_calculated(request):
    expire_text = request.GET['expires_text']

    if len(expire_text) != 6:
        numeric = re.compile(r'[^\d]+')
        expire_text = numeric.sub('', expire_text)
        expire_year = d.datetime.now()
        expire_new = expire_year.year + 1
        expire_text = str(expire_new)[2:]
        expire_text = "3112" + expire_text
        return expire_text

    """Rid info here"""
    rid_text = request.GET['rid_text']
    index_text = request.GET['index_text']
    data_text = ("[a" + rid_text[1:] + index_text + ".data]")
    modulus_text = ("[a" + rid_text[1:] + index_text + ".modulus]")

    key_text = request.GET['key_text'].strip()
    full_modulus_text = request.GET['full_modulus_text'].strip()
    key_length = len(full_modulus_text.strip()) * 4
    modulus_parse = int(key_length / 32)
    modulus_length = int(len(full_modulus_text) / 2)
    exponent_text = request.GET['exponent_text']

    mod1 = full_modulus_text[:modulus_parse]
    mod2 = full_modulus_text[modulus_parse:modulus_parse * 2]
    mod3 = full_modulus_text[modulus_parse * 2: modulus_parse * 3]
    mod4 = full_modulus_text[modulus_parse * 3: modulus_parse * 4]
    mod5 = full_modulus_text[modulus_parse * 4: modulus_parse * 5]
    mod6 = full_modulus_text[modulus_parse * 5: modulus_parse * 6]
    mod7 = full_modulus_text[modulus_parse * 6: modulus_parse * 7]
    mod8 = full_modulus_text[modulus_parse * 7: modulus_parse * 8]

    return render(request, 'capk_calculated.html',
                  {'key_text': key_text, 'key_length': key_length, 'modulus_text': modulus_text,
                   'expire_text': expire_text, 'data_text': data_text, 'full_modulus_text': full_modulus_text,
                   'modulus_length': modulus_length, 'exponent_text': exponent_text, 'modulus_parse': modulus_parse,
                   'mod1': mod1, 'mod2': mod2, 'mod3': mod3, 'mod4': mod4, 'mod5': mod5, 'mod6': mod6,
                   'mod7': mod7, 'mod8': mod8, 'rid_text': rid_text})


def hex2(request):
    hex_text = request.GET['hex']
    hex_value = hex_text.strip()
    # hex = hex.strip()

    scale = 16

    """Define Hex Keys"""
    hexkeys = {'0': '0000', '1': '0001', '2': '0010'}

    num_of_bits = 8

    binary = bin(int('1' + hex_value, scale))[3:].zfill(num_of_bits)

    binary_list = [binary[i:i + num_of_bits] for i in range(0, len(binary), num_of_bits)]

    byte = 1

    display_list = []
    for bytes in binary_list:
        half1 = bytes[4:]
        half2 = bytes[0:4]
        byte_header = "Byte #" + str(byte) + " = " + half1[::-1] + " " + half2[::-1]
        display_list.append(byte_header)
        display_list.append("Byte " + str(byte) + " Bit #1 = " + bytes[7:])
        display_list.append("Byte " + str(byte) + " Bit #2 = " + bytes[6:7])
        display_list.append("Byte " + str(byte) + " Bit #3 = " + bytes[5:6])
        display_list.append("Byte " + str(byte) + " Bit #4 = " + bytes[4:5])
        display_list.append("Byte " + str(byte) + " Bit #5 = " + bytes[3:4])
        display_list.append("Byte " + str(byte) + " Bit #6 = " + bytes[2:3])
        display_list.append("Byte " + str(byte) + " Bit #7 = " + bytes[1:2])
        display_list.append("Byte " + str(byte) + " Bit #8 = " + bytes[0:1])
        display_list.append("")
        byte += 1

    return render(request, 'hex_calc.html', {'hex': hex, 'hex_value': hex_value,
                                             # 'hexkeys': hexkeys,
                                             'byte': byte, 'binary_list': binary_list, 'display_list': display_list})


def hex_calculated(request):
    hex_text = request.GET['hex']
    hex_value = hex_text.strip()
    # hex = hex.strip()

    scale = 16

    """Define Hex Keys"""
    hexkeys = {'0': '0000', '1': '0001', '2': '0010'}

    num_of_bits = 8

    binary = bin(int('1' + hex_value, scale))[3:].zfill(num_of_bits)

    binary_list = [binary[i:i + num_of_bits] for i in range(0, len(binary), num_of_bits)]

    byte = 1

    display_list = []
    for bytes in binary_list:
        half1 = bytes[4:]
        half2 = bytes[0:4]
        byte_header = "Byte #" + str(byte) + " = " + half1[::-1] + " " + half2[::-1]
        display_list.append(byte_header)
        display_list.append("Byte " + str(byte) + " Bit #1 = " + bytes[7:])
        display_list.append("Byte " + str(byte) + " Bit #2 = " + bytes[6:7])
        display_list.append("Byte " + str(byte) + " Bit #3 = " + bytes[5:6])
        display_list.append("Byte " + str(byte) + " Bit #4 = " + bytes[4:5])
        display_list.append("Byte " + str(byte) + " Bit #5 = " + bytes[3:4])
        display_list.append("Byte " + str(byte) + " Bit #6 = " + bytes[2:3])
        display_list.append("Byte " + str(byte) + " Bit #7 = " + bytes[1:2])
        display_list.append("Byte " + str(byte) + " Bit #8 = " + bytes[0:1])
        display_list.append("")
        byte += 1

    return render(request, 'hex_calc.html', {'hex': hex, 'hex_value': hex_value,
                                             # 'hexkeys': hexkeys,
                                             'byte': byte, 'binary_list': binary_list, 'display_list': display_list})


def hex_reverse(request):
    return render(request, 'hex_reverse.html')


def hex_reverse_calculated(request):
    # hex_text_reverse = request.GET['hex_reverse']
    Byte1Bit1 = request.GET['Byte1Bit1']
    Byte1Bit2 = request.GET['Byte1Bit2']
    Byte1Bit3 = request.GET['Byte1Bit3']
    Byte1Bit4 = request.GET['Byte1Bit4']
    Byte1Bit5 = request.GET['Byte1Bit5']
    Byte1Bit6 = request.GET['Byte1Bit6']
    Byte1Bit7 = request.GET['Byte1Bit7']
    Byte1Bit8 = request.GET['Byte1Bit8']
    Byte1Half1 = str(Byte1Bit1 + Byte1Bit2 + Byte1Bit3 + Byte1Bit4).strip()
    Byte1Half2 = str(Byte1Bit5 + Byte1Bit6 + Byte1Bit7 + Byte1Bit8).strip()
    Byte1Hex = hex_function(Byte1Half2[::-1]) + hex_function(Byte1Half1[::-1])

    # Byte2
    Byte2Bit1 = request.GET['Byte2Bit1']
    Byte2Bit2 = request.GET['Byte2Bit2']
    Byte2Bit3 = request.GET['Byte2Bit3']
    Byte2Bit4 = request.GET['Byte2Bit4']
    Byte2Bit5 = request.GET['Byte2Bit5']
    Byte2Bit6 = request.GET['Byte2Bit6']
    Byte2Bit7 = request.GET['Byte2Bit7']
    Byte2Bit8 = request.GET['Byte2Bit8']
    Byte2Half1 = str(Byte2Bit1 + Byte2Bit2 + Byte2Bit3 + Byte2Bit4).strip()
    Byte2Half2 = str(Byte2Bit5 + Byte2Bit6 + Byte2Bit7 + Byte2Bit8).strip()
    Byte2Hex = hex_function(Byte2Half2[::-1]) + hex_function(Byte2Half1[::-1])

    Byte3Bit1 = request.GET['Byte3Bit1']
    Byte3Bit2 = request.GET['Byte3Bit2']
    Byte3Bit3 = request.GET['Byte3Bit3']
    Byte3Bit4 = request.GET['Byte3Bit4']
    Byte3Bit5 = request.GET['Byte3Bit5']
    Byte3Bit6 = request.GET['Byte3Bit6']
    Byte3Bit7 = request.GET['Byte3Bit7']
    Byte3Bit8 = request.GET['Byte3Bit8']
    Byte3Half1 = str(Byte3Bit1 + Byte3Bit2 + Byte3Bit3 + Byte3Bit4).strip()
    Byte3Half2 = str(Byte3Bit5 + Byte3Bit6 + Byte3Bit7 + Byte3Bit8).strip()
    Byte3Hex = hex_function(Byte3Half2[::-1]) + hex_function(Byte3Half1[::-1])

    Byte4Bit1 = request.GET['Byte4Bit1']
    Byte4Bit2 = request.GET['Byte4Bit2']
    Byte4Bit3 = request.GET['Byte4Bit3']
    Byte4Bit4 = request.GET['Byte4Bit4']
    Byte4Bit5 = request.GET['Byte4Bit5']
    Byte4Bit6 = request.GET['Byte4Bit6']
    Byte4Bit7 = request.GET['Byte4Bit7']
    Byte4Bit8 = request.GET['Byte4Bit8']
    Byte4Half1 = str(Byte4Bit1 + Byte4Bit2 + Byte4Bit3 + Byte4Bit4).strip()
    Byte4Half2 = str(Byte4Bit5 + Byte4Bit6 + Byte4Bit7 + Byte4Bit8).strip()
    Byte4Hex = hex_function(Byte4Half2[::-1]) + hex_function(Byte4Half1[::-1])

    Byte5Bit1 = request.GET['Byte5Bit1']
    Byte5Bit2 = request.GET['Byte5Bit2']
    Byte5Bit3 = request.GET['Byte5Bit3']
    Byte5Bit4 = request.GET['Byte5Bit4']
    Byte5Bit5 = request.GET['Byte5Bit5']
    Byte5Bit6 = request.GET['Byte5Bit6']
    Byte5Bit7 = request.GET['Byte5Bit7']
    Byte5Bit8 = request.GET['Byte5Bit8']
    Byte5Half1 = str(Byte5Bit1 + Byte5Bit2 + Byte5Bit3 + Byte5Bit4).strip()
    Byte5Half2 = str(Byte5Bit5 + Byte5Bit6 + Byte5Bit7 + Byte5Bit8).strip()
    Byte5Hex = hex_function(Byte5Half2[::-1]) + hex_function(Byte5Half1[::-1])

    Byte6Bit1 = request.GET['Byte6Bit1']
    Byte6Bit2 = request.GET['Byte6Bit2']
    Byte6Bit3 = request.GET['Byte6Bit3']
    Byte6Bit4 = request.GET['Byte6Bit4']
    Byte6Bit5 = request.GET['Byte6Bit5']
    Byte6Bit6 = request.GET['Byte6Bit6']
    Byte6Bit7 = request.GET['Byte6Bit7']
    Byte6Bit8 = request.GET['Byte6Bit8']
    Byte6Half1 = str(Byte6Bit1 + Byte6Bit2 + Byte6Bit3 + Byte6Bit4).strip()
    Byte6Half2 = str(Byte6Bit5 + Byte6Bit6 + Byte6Bit7 + Byte6Bit8).strip()
    Byte6Hex = hex_function(Byte6Half2[::-1]) + hex_function(Byte6Half1[::-1])

    Byte7Bit1 = request.GET['Byte7Bit1']
    Byte7Bit2 = request.GET['Byte7Bit2']
    Byte7Bit3 = request.GET['Byte7Bit3']
    Byte7Bit4 = request.GET['Byte7Bit4']
    Byte7Bit5 = request.GET['Byte7Bit5']
    Byte7Bit6 = request.GET['Byte7Bit6']
    Byte7Bit7 = request.GET['Byte7Bit7']
    Byte7Bit8 = request.GET['Byte7Bit8']
    Byte7Half1 = str(Byte7Bit1 + Byte7Bit2 + Byte7Bit3 + Byte7Bit4).strip()
    Byte7Half2 = str(Byte7Bit5 + Byte7Bit6 + Byte7Bit7 + Byte7Bit8).strip()
    Byte7Hex = hex_function(Byte7Half2[::-1]) + hex_function(Byte7Half1[::-1])

    Byte8Bit1 = request.GET['Byte8Bit1']
    Byte8Bit2 = request.GET['Byte8Bit2']
    Byte8Bit3 = request.GET['Byte8Bit3']
    Byte8Bit4 = request.GET['Byte8Bit4']
    Byte8Bit5 = request.GET['Byte8Bit5']
    Byte8Bit6 = request.GET['Byte8Bit6']
    Byte8Bit7 = request.GET['Byte8Bit7']
    Byte8Bit8 = request.GET['Byte8Bit8']
    Byte8Half1 = str(Byte8Bit1 + Byte8Bit2 + Byte8Bit3 + Byte8Bit4).strip()
    Byte8Half2 = str(Byte8Bit5 + Byte8Bit6 + Byte8Bit7 + Byte8Bit8).strip()
    Byte8Hex = hex_function(Byte8Half2[::-1]) + hex_function(Byte8Half1[::-1])

    BytesList = [Byte1Hex, Byte2Hex, Byte3Hex, Byte4Hex, Byte5Hex, Byte6Hex, Byte7Hex, Byte8Hex]
    BytesCombined = " ".join(BytesList)

    return render(request, 'hex_reverse_calculated.html', {'Byte1Half1': Byte1Half1, 'Byte2Half2': Byte2Half2,
                                                           'Byte3Half2': Byte3Half2, 'Byte4Half2': Byte4Half2,
                                                           'Byte5Half2': Byte5Half2, 'Byte6Half2': Byte6Half2,
                                                           'Byte7Half2': Byte7Half2, 'Byte8Half2': Byte8Half2,
                                                           'Byte1Hex': Byte1Hex, 'Byte2Hex': Byte2Hex,
                                                           'Byte3Hex': Byte3Hex, 'Byte4Hex': Byte4Hex,
                                                           'Byte5Hex': Byte5Hex, 'Byte6Hex': Byte6Hex,
                                                           'Byte7Hex': Byte7Hex, 'Byte8Hex': Byte8Hex,
                                                           'BytesCombined': BytesCombined})


def hex_function(hex_value):
    try:
        hex_dict = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6',
                    '0111': '7',
                    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E',
                    '1111': 'F'}
        return hex_dict[hex_value]
    except:
        return ''
