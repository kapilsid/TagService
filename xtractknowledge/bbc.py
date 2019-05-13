import os
import numpy as np
from numpy import zeros

def load_bbc(path="."):

    artPath = os.path.join(path, 'bbc.mtx')
    vocPath = os.path.join(path, 'bbc.terms')
    labPath = os.path.join(path, 'bbc.classes')

    vocab = {}
    counter = 0
    fvocab = open(vocPath, 'r')
    for line in fvocab:
        vocab[line.replace('\n','')] = counter
        counter +=1
    fvocab.close()


    farticles = open(artPath,"r")
    farticles.readline()
    sizing = farticles.readline().split(" ")
    articles = np.zeros((int(sizing[1]), int(sizing[0])), dtype=np.uint16)
    for line in farticles:
      point = line.replace('\n','').split(" ")
      articles[int(point[1])-1][int(point[0])-1] = float(point[2])

    farticles.close()

    flabels = open(labPath, 'r')
    flabels.readline() 
    flabels.readline()
    keyValues = flabels.readline().replace('\n','') 
    keys = keyValues.split(' ')[2].split(',')
    flabels.readline()
    labels = np.zeros((int(sizing[1])), dtype=np.uint8)
    for line in flabels:
      point = line.replace('\n','').split(" ")
      labels[int(point[0])] = int(point[1])
    flabels.close()

    return vocab, articles, labels, keys