# function bittohexstr: change bits to hex strings
# input: data: raw bits
# output: result: the Captalized HEX result

import numpy as np

def bittohexstr(data):
    ## you need to write your own code to do DBPSK decoding
    result=""
    for i in range(len(data)//4):
        reserse_num_str = str(data[i*4])+str(data[i*4+1])+str(data[i*4+2])+str(data[i*4+3])
        num_str = reserse_num_str[::-1]
        num = int(num_str, 2)               # 将二进制字符串'1010'解释为整数
        hex_num = hex(num)                  # 将整数10转换为十六进制字符串'0xa'
        hex_char = hex_num[2:]              # 去掉十六进制字符串的前缀'0x'
        result = hex_char.upper() + result  # 将十六进制字符串转换为大写
    return result