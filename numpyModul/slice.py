import numpy as np
import sys
import os
def main(argc,argv,envp):
    a = np.arange(1,10)
    print(a)
    print(a[:3],a[::-1])
    print(a[:-4:-1])
    print(a[-1:-4:-1])
    print(a[-7::-1])
    print("*************")
    b = np.arange(1,25).reshape(2,3,4)
    print(b)
    # print(b[:,0,0])
    # print(b[0,:,:])
    print(b[0,...])
    # print(b[0,1,::2])
    print(b[0,])
    print(b[:,0])
    print(b[...,1])
    print(b[:,1])
    print(b[-1,1:,2:])
    return 0

if __name__ =='__main__':
    # print(sys.argv,sys.argv,os.environ)
    sys.exit(main(len(sys.argv),sys.argv,os.environ))