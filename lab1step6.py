# function sfd_start = find_preamble(data)
# function find_preamble: find the preamble in the frame data
# input: data  descrambled bit sequence
# output: sfd_start: the poistion of the first sfd bit, if cannot find the
#                   sfd, set sfd_start=-1

import numpy as np

def find_preamble(data):
    ## you need to write your own code to do DBPSK decoding
    sfd_start = -1
    for i in range(len(data)-15):
        if data[i] == 0 and data[i + 1] == 0 and data[i + 2] == 0 and data[i + 3] == 0:
            hexstr = ""
            for j in range(16):
                hexstr += str(data[i + j])
            if hexstr == "0000010111001111":
                sfd_start = i
                break
    return sfd_start