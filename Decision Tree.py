# -*- coding: utf-8 -*-
"""
Created on Wed Aug 03 20:36:51 2016

@author: YI
"""
import pandas as pd
import numpy as np
import operator

def entropy(dataset):
    m = len(dataset)
    labelcounts = {}
    for i in dataset:
        label = i[-1] #the index will change based on the location of the lables
        if label not in labelcounts.keys():
            labelcounts[label] = 0
        labelcounts[label] += 1
    entropy = 0
    for key in labelcounts:
        prob = labelcounts[key] / float(m)
        entropy -= prob * np.log(prob, 2)
    return entropy
    
def splitDataset(dataset, index, value):
    subDataset = []
    for example in dataset:
        if example[index] == value:
            reducedExample = example[:index]
            reducedExample.extend(example[index+1:])
            subDataset.append(reducedExample)
    return subDataset

#ID3    
def bestFeatures(dataset): #dataset is a list of lists, and contains labels
    numFeatures = len(dataset[0] - 1)
    baseEntropy = entropy(dataset)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataset]
        uniqueValues = set(featList)
        conEntropy = 0.0
        for value in uniqueValues:
            subDataset = splitDataset(dataset, i, value)
            prob = len(subDataset) / float(len(dataset))
            conEntropy += prob * entropy(subDataset)
        infoGain = baseEntropy - conEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

def majorityVote(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]
  
def decisionTree(dataset, labels):
    classList = [example[-1] for example in dataset]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataset[0]) == 1:
        return majorityVote(classList)
    bestFeature = bestFeatures(dataset)
    bfLabel = labels[bestFeature]
    tree = {bfLable:{}}
    del labels[bestFeature]
    featureValue = [example[bestFeature] for example in dataset]
    uniqueValue = set(featureValue)
    for value in uniqueValue:
        subLabels = lables[:]
        tree[bestFeature][value] = decisionTree(splitDataset(dataset, bestFeature, value),\
                                        subLabels)
    return tree
    
 

    
    
        
    
    
    
    
    
    
    
