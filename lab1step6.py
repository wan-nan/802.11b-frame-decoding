# function sfd_start = find_preamble(data)
# function find_preamble: find the preamble in the frame data
# input: data  descrambled bit sequence
# output: sfd_start: the poistion of the first sfd bit, if cannot find the
#                   sfd, set sfd_start=-1

import numpy as np

def find_preamble(data):
    ## you need to write your own code to do DBPSK decoding
    sfd_start = -1
    return sfd_start