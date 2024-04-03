# pcap file generation functions
# you need to add your own code here

import numpy as np
import struct

def write_pcap_header(filename):
    with open(filename, mode='wb+') as writer:
        magicnumber=2712847316
        writer.write(struct.pack('@I',magicnumber))
        v_major=2
        v_minor=4
        writer.write(struct.pack('@H',v_major))
        writer.write(struct.pack('@H',v_minor))
        this_zone=0
        writer.write(struct.pack('@I',this_zone))
        sigfigs=0
        writer.write(struct.pack('@I',sigfigs))
        snaplen=32768
        writer.write(struct.pack('@I',snaplen))
        network=105
        writer.write(struct.pack('@I',network))

def write_pcap_frame(filename,data,offset):
    with open(filename, mode='ab+') as writer:
        ts_sec = 0
        writer.write(struct.pack('@I',ts_sec))
        writer.write(struct.pack('@I',offset))
        data_size= data.shape[0] // 8
        writer.write(struct.pack('@I',data_size))
        writer.write(struct.pack('@I',data_size))
        data= np.reshape(data[0:data_size*8],(-1,8) )
        weight=np.rint(np.exp2(range(8))).astype(int)
        for byte in data:
            writer.write(struct.pack('@B',np.dot(byte,weight)))