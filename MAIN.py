import os
import numpy as np
import matplotlib.pyplot as plt

from scipy import fftpack

def hilbert(x):
    t = np.linspace(1e-10, 2*np.pi, len(x))
    y = np.convolve(x,1/(np.pi*t))
    return y[0:len(x)]/1e9


##测试从路径打开文件
def testFileKeep():
    NowPath = os.getcwd()
    L = os.listdir(NowPath+"\\TrainingData")
    ##列出该文件夹下的文件的名字
    print L
    os.chdir(NowPath+"\\TrainingData")
    f = open(L[0])
    a = f.readlines()
    print(a)


if __name__ == "__main__":
    #testFileKeep()

    SamplingRate = 100.0
    t = np.linspace(1e-10, 2*np.pi, SamplingRate)
    x = np.cos(t)
    hy = hilbert(x)

    hhy = fftpack.hilbert(x)

    print(len(t), len(x))

    plt.plot(t,x)
    plt.plot(t,hhy)
    plt.show()
