#function descramble: descramble the bits using LSFR
# input: raw_bits -- raw bits after DBPSK
# output: frame_bits -- real transmitted bits for the frame, converted to integers

import numpy as np
import copy
def descramble(raw_bits):
    ## you need to write your own code to do DBPSK decoding
    frame_bits = copy.deepcopy(raw_bits) 
    for i in range(7, len(raw_bits)):
        frame_bits[i] = raw_bits[i - 7] ^ raw_bits[i - 4] ^ raw_bits[i]
    return frame_bits