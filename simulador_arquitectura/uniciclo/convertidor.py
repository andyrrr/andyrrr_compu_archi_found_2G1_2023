def invert_binary(binary_number):
    inverted_result = ''
    for bit in binary_number:
        if bit == '0':
            inverted_result += '1'
        else:
            inverted_result += '0'
    return inverted_result


def decimal_to_binary(decimal_number):
    absolute_value = abs(decimal_number)
    binary_result = ''
    counter = 0

    while absolute_value >= 2:
        binary_result = str(absolute_value % 2) + binary_result
        absolute_value //= 2
        counter += 1

    binary_result = str(absolute_value) + binary_result

    while counter < 4:
        binary_result = '0' + binary_result
        counter += 1

    if decimal_number < 0:
        final_result = decimal_to_binary(binary_to_decimal(invert_binary(binary_result)) + 2)
        return final_result
    else:
        return binary_result


def negative_binary_to_decimal(binary_number):
    inverted_binary = decimal_to_binary(binary_to_decimal(binary_number) - 2)
    return -1 * binary_to_decimal(invert_binary(inverted_binary))


def binary_to_decimal(binary_number):
    result = 0
    while binary_number[0] == '0':
        binary_number = binary_number[1:]

        if len(binary_number) == 1 and binary_number[0] == '0':
            return result

    index = 0
    size = len(binary_number)

    while index < size:
        tmp = binary_number[-1]
        result += int(tmp) * 2 ** index
        binary_number = binary_number[:-1]
        index += 1

    return result


def decimal_to_hexadecimal(decimal_number):
    counter = 0
    hexadecimal_result = ''

    while decimal_number >= 16:
        remainder = decimal_number % 16

        if 10 <= remainder <= 15:
            hexadecimal_result = chr(ord('a') + remainder - 10) + hexadecimal_result
        else:
            hexadecimal_result = str(remainder) + hexadecimal_result

        decimal_number //= 16
        counter += 1

    if 10 <= decimal_number <= 15:
        hexadecimal_result = chr(ord('a') + decimal_number - 10) + hexadecimal_result
    else:
        hexadecimal_result = str(decimal_number) + hexadecimal_result

    counter += 1

    while counter < 8:
        hexadecimal_result = '0' + hexadecimal_result
        counter += 1

    return '0x' + hexadecimal_result


def hexadecimal_to_decimal(hexadecimal_number):
    result = 0
    hexadecimal_number = hexadecimal_number[2:]

    while hexadecimal_number[0] == '0':
        hexadecimal_number = hexadecimal_number[1:]

        if len(hexadecimal_number) == 1 and hexadecimal_number[0] == '0':
            return result

    index = 0
    size = len(hexadecimal_number)

    while index < size:
        tmp = hexadecimal_number[-1]

        if 'a' <= tmp <= 'f':
            result += (ord(tmp) - ord('a') + 10) * 16 ** index
        else:
            result += int(tmp) * 16 ** index

        hexadecimal_number = hexadecimal_number[:-1]
        index += 1

    return result
