import os

def hilbert(x):
    pass
    return y


def testFileKeep():
    NowPath = os.getcwd()
    L = os.listdir(NowPath+"\\TrainingData")
    print L
    os.chdir(NowPath+"\\TrainingData")
    f = open(L[0])
    a = f.readlines()
    print(a)


if __name__ == "__main__":
    testFileKeep()
