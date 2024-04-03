##################################################
#  Baseband decoding experiment main script
#  Nanjing University Dislab
#  Author: Wei Wang
#  Date: 2023/1/30
################################################### 

import numpy as np
from matplotlib import pyplot as plt
from lab1step1 import *
from lab1step3 import *
from lab1step4 import *
from lab1step5 import *
from lab1step6 import *
from lab1step7 import *
from pcapframe import *

# switch to turn off the interactive part
interactive=1

## Step 1 Load the dump file from USRP Software radio
# Source code in lab1step1.py
filename="../data/lab1.dat"  #filename of the baseband
num_samples, baseband_data=load_baseband(filename,0,-1)

print(num_samples)
if (interactive):
    plt.figure(0)
    plt.cla()
    plt.plot(range(1,1000000,31),np.abs(baseband_data[1:1000000:31]))
    plt.xlabel("Sample Points")
    plt.ylabel("Magnitude")
    plt.title("Magnitude of baseband signal")


    plt.figure(1)
    plt.cla()
    plt.plot(np.real(baseband_data[200000:210000:1]))
    plt.plot(np.imag(baseband_data[200000:210000:1]))
    plt.xlabel("Sample Points")
    plt.ylabel("Real/imaginary part")
    plt.legend(["Real", "Imaginary"])
    plt.title("Complex values of baseband signal")
    
    plt.figure(2)
    plt.cla()
    plt.plot(np.real(baseband_data[200200:200400:1]))
    plt.xlabel("Sample Points")
    plt.ylabel("Real part")
    plt.title("Enlarged of baseband signal")
    print('Showing magnitude of the baseband signal');
    print('Paused, close the figure to continue or use Ctrl-C to stop');
    plt.show()

## Step 2: Despread the baseband signal

# 25 point barker code
barker_25=np.array([+1, +1, -1, -1, +1, +1, +1, +1, +1, -1, -1, +1, +1, +1, +1, +1, +1, +1, -1, -1, -1, -1, -1, -1, -1])

# calculate the correlation of the barker code
# You should fillin your own code here
corr_result=baseband_data

if (interactive):
    plt.cla()
    plt.plot(np.real(corr_result[200200:200400:1]))
    plt.xlabel("Sample Points")
    plt.ylabel("Real part")
    plt.title("Correlation results")    
    print('Showing correlation result of the baseband signal');
    print('Paused, close the figure to continue or use Ctrl-C to stop');
    plt.show()

# Find out the peaks in the correlation
# You should fillin your own code here

despread_data=corr_result

if (interactive):
    plt.cla()
    plt.plot(np.abs(despread_data[1:40000:1]))
    plt.xlabel("Sample Points")
    plt.ylabel("Magnitude")
    plt.title("Magnitude of despreaded signal")    
    print('Showing despreaded result of the baseband signal');
    print('Paused, close the figure to continue or use Ctrl-C to stop');
    plt.show()

## Step 3: Finding the start and ending of the frame
# Sourcecode in lab1step3.py

frame_boundary= find_frame_boundary( despread_data )

if(interactive):
    print("Found " + str(frame_boundary.shape[1]) + " frames")

## loop over every frame to decode them

# You may add preparation code here

pcapname='myframes.pcap'
# Souce code in pcapframe.py
write_pcap_header(pcapname);

count = 0

for frame in np.transpose(frame_boundary):
    print("Decoding frame " + str(count) + " from "+ str(frame[0]) + " to " + str(frame[1])+ " samples")
    frame_data=despread_data[frame[0]:frame[1]]
    count = count + 1

    # Step 4: Decode the DBPSK signal
    # Source code in lab1step4.py
    raw_bits = decode_dbpsk(frame_data)
    
    # Step 5: Descramble the raw bits to get real bits
    # Source code in lab1step5.py
    frame_bits = descramble(raw_bits)

    # Step 6: Find the SYNC and remove them
    # Source code in lab1step6.py
    sfd_start = find_preamble (frame_bits)
    
    if(sfd_start < 0):
        print("Preamble not found!")
        continue

    # Step 7: Check SFD sequence
    # Source code in lab1step7.py
    sfd_data = bittohexstr (frame_bits[sfd_start:sfd_start+16])

    if(sfd_data == "F3A0"):
        print("SFD found = " + sfd_data )
    else:
        print("SFD not found")
        continue
    
    # Step 7 check SIGNAL, use the same function
    signal_data = bittohexstr (frame_bits[sfd_start+16:sfd_start+24])

    if(signal_data == "0A"):
        print("Signal = " + signal_data + ", rate 1M OK" )
    else:
        print("Signal = " + signal_data + ", rate Wrong" )
        continue

    # Step 8 Print out service, length and CRC
    print("Service = " + bittohexstr(frame_bits[sfd_start+24:sfd_start+32])\
        + " length = " + bittohexstr(frame_bits[sfd_start+32:sfd_start+48])\
        + " CRC = " +bittohexstr(frame_bits[sfd_start+48:sfd_start+64]))

    # Step 9 Get MPDU
    mpdu_start = sfd_start + 64
    # Souce code in pcapframe.py
    write_pcap_frame(pcapname, frame_bits[mpdu_start:],frame[0])