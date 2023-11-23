import convertidor

class ALU:
    def add(self, num1, num2):
        return convertidor.decimal_to_binary(convertidor.hexadecimal_to_decimal(num1) + convertidor.hexadecimal_to_decimal(num2))

    def sub(self, num1, num2):
        res = ''
        tmp = convertidor.hexadecimal_to_decimal(num1) - convertidor.hexadecimal_to_decimal(num2)
        if tmp < 0:
            ext = ImmExtend()
            tmp = ext.extend(convertidor.decimal_to_binary(abs(tmp)))
            for i in tmp:
                if i == '0':
                    res = res + '1'
                else:
                    res = res + '0'
            return convertidor.decimal_to_hexadecimal(convertidor.binary_to_decimal(res) + 1)
        else:
            return convertidor.decimal_to_hexadecimal(tmp)

    def bSub(self, num1, num2):
        return convertidor.hexadecimal_to_decimal(num1) - convertidor.hexadecimal_to_decimal(num2)

    def andOP(self, num1, num2):
        result = ''
        ext = ImmExtend()
        bin1 = ext.extend(convertidor.decimal_to_binary(convertidor.hexadecimal_to_decimal(num1)))
        bin2 = ext.extend(convertidor.decimal_to_binary(convertidor.hexadecimal_to_decimal(num2)))
        for i in range(0, 32):
            if bin1[i] == '1' and bin2[i] == '1':
                result = result + '1'
            else:
                result = result + '0'
        return convertidor.decimal_to_hexadecimal(convertidor.binary_to_decimal(result))

    def orOP(self, num1, num2):
        result = ''
        ext = ImmExtend()
        bin1 = ext.extend(convertidor.decimal_to_binary(convertidor.hexadecimal_to_decimal(num1)))
        bin2 = ext.extend(convertidor.decimal_to_binary(convertidor.hexadecimal_to_decimal(num2)))
        for i in range(0, 32):
            if bin1[i] == '1' or bin2[i] == '1':
                result = result + '1'
            else:
                result = result + '0'
        return convertidor.decimal_to_hexadecimal(convertidor.binary_to_decimal(result))

class ImmExtend:
    def extend(self,imm):
        size = len(imm)
        while size < 32:
            imm = '0' + imm
            size = size + 1
        return imm