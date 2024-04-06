import numpy as np
import copy
raw_bits = np.ones(200, dtype=int)

## you need to write your own code to do DBPSK decoding
frame_bits = copy.deepcopy(raw_bits) 
for i in range(0, len(raw_bits)):
    frame_bits[i] = (raw_bits[i - 7] if i >= 7 else 0) ^ (raw_bits[i - 4] if i >= 4 else 0) ^ raw_bits[i]
print(frame_bits)
for i in range(0, len(frame_bits)):
    raw_bits[i] = (frame_bits[i - 7] if i >= 7 else 0) ^ (frame_bits[i - 4] if i >= 4 else 0) ^ frame_bits[i]
print(raw_bits)