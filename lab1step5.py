#function descramble: descramble the bits using LSFR
# input: raw_bits -- raw bits after DBPSK
# output: frame_bits -- real transmitted bits for the frame, converted to integers

import numpy as np

def descramble(raw_bits):
    ## you need to write your own code to do DBPSK decoding
    frame_bits = raw_bits 
    return frame_bits