#load the uint16 USRP rx_sample_to_file dumpfile
#input:
#  -filename: the dumpfile
#  -start: the number of samples to skip at the start
#  -num: the number of samples to read, use inf if read all data
#output:
#  -count: the number of read samples
#  -loadtrace16: the complex sample data;
import numpy as np

def load_baseband(filename,start,num):
    rawarr=np.fromfile(filename,dtype=np.dtype([('i','<i2'),('q','<i2')]),count=num,offset=start*4)
    baseband=rawarr['i']+1j*rawarr['q']
    return baseband.shape[0], baseband