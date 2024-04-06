def scrambler(input_bits):
    # 初始化寄存器为全0
    registers = [0, 0, 0, 0, 0, 0, 0]
    
    # 输出序列
    output_bits = []

    for bit in input_bits:
        # 计算输出
        output = (bit + registers[6] + registers[3]) % 2
        output_bits.append(output)
        
        # 更新寄存器
        registers = [output] + registers[:-1]

    return output_bits

# 127为周期
input_bits = [1] * 127

# 获取输出序列
output_sequence = scrambler(input_bits)

# 将输出序列转换为16进制表示
output_hex = ''.join(str(bit) for bit in output_sequence)
output_hex = f"{int(output_hex, 2):X}"

print("输出序列（十六进制）:", output_hex)
