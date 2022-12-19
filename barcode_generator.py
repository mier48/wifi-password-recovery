from barcode import EAN13

number = '5901234123457'

code = EAN13(number)
code.save("code_1")