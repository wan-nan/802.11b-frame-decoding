# function decode_dbpsk: decode the rawbits from the despread signal of a
# single frame
# input: data  -- complex valued despread signal
# output: raw_bits -- logic valued vector contains True and False of the decoded
# bits
import numpy as np
import math

def decode_dbpsk(received_signal):
    ## you need to write your own code to do DBPSK decoding
    raw_bits = np.empty(0, dtype=int)

    # 计算相邻符号之间的相位差
    for i in range(1, len(received_signal)):
        phase_diff = np.angle(received_signal[i] / received_signal[i-1])
        
        # 根据相位差判断数据位的变化
        if abs(phase_diff) >= np.pi / 2:
            raw_bits = np.append(raw_bits, 1)  # 相位变化为180度，表示数据位为1
        elif abs(phase_diff) < np.pi / 2:
            raw_bits = np.append(raw_bits, 0)  # 相位不变，表示数据位为0
    assert len(raw_bits) == len(received_signal) - 1
    return raw_bits