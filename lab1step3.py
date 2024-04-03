# function find_frame_bounary, find the boundary of the frames by magnitude
# changes
#input: data -- despreaded data
#output: 
#   f_boundary -- the start and ending points of the frames in a 2*n
#                 matrix,n is the number of detected frames, the first row
#                 is the starting point, the second row is the ending point
import numpy as np

def find_frame_boundary(data):
    f_boundary=np.empty(shape=[2, 0])
    if(data.shape[0]<1000):
        return f_boundary
    filter=np.array([1, 1, 1, -1, -1, -1]) #edge detector
    filter2=np.array([1, 1, 1, 1, 1, 1])     #moving average
    data=abs(data)
    temp=np.convolve(data,filter)      # use the edge detector to find sharp edges
    thr=np.convolve(data,filter2)*0.8  # the threshod determined by moving average
    posedge=(np.sign(temp-thr)+1)/2     #find the postive edge, magnitude jump up
    negedge=-(np.sign(temp+thr)-1)/2    #fine the negative edge, magnitude jump down 
    pos=np.argwhere(posedge==1)
    neg=np.argwhere(negedge==1)
    pstart=0
    pend=0
    while (pstart<pos.shape[0]-1) and (pend<neg.shape[0]-1):
        while (neg[pend]<pos[pstart]) and (pend<neg.shape[0]-1):
            pend=pend+1
        if (neg[pend]-pos[pstart]>1000) and (pos[pstart+1]-pos[pstart])>1000 and pos[pstart+1]>neg[pend]:
            f_boundary= np.append(f_boundary,[ (pos[pstart]+filter.shape[0]), (neg[pend]-filter.shape[0]) ],axis=1)
        pstart=pstart+1
    f_boundary= (np.rint(f_boundary[:,1:-1])).astype(int)
    return f_boundary