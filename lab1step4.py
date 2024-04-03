# function decode_dbpsk: decode the rawbits from the despread signal of a
# single frame
# input: data  -- complex valued despread signal
# output: raw_bits -- logic valued vector contains True and False of the decoded
# bits
import numpy as np
import math

def decode_dbpsk(data):
    ## you need to write your own code to do DBPSK decoding
    raw_bits = np.zeros(data.shape)
    return raw_bits