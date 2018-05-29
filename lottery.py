import pandas as pd
import random
import operator

dataset = pd.read_csv("/home/meet/Machine Learing/projects/loteryticket.csv")
num=dataset.values
print(num)
l=[]
for i in range(len(num)):
    l.append([int(i) for i in num[i][1].split()])

print(l)

def splitDataset(dataset, splitRatio):
    trainSize = int(len(dataset) * splitRatio)
    trainSet = []
    copy = list(dataset)
    while len(trainSet) < trainSize:
        index = random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet, copy]


train,test=splitDataset(l,0.7)


def build_dict(l1):
    dict={}
    for ls in l1:
        for i in ls:
            if i in dict.keys():
                dict[i]+=1
            else:
                dict[i]=1
    return dict

print("dict",build_dict(l))

train_dict=build_dict(train)
test_dict=build_dict(test)


print("train set",train_dict)
print("test set",test_dict)

sorted_tr = sorted(train_dict.items(), key=operator.itemgetter(1))
sorted_te = sorted(test_dict.items(), key=operator.itemgetter(1))
print("sorted trainset",sorted_tr)
print("sorted testset",sorted_te)
l1=[]
for i in range(1,20):
   l1.append(sorted_tr.pop(-1))

print(l1)
print(test)
count=0
for i in range(len(l1)):
    for j in range(len(test)):
        for k in range(0,19):
            if(l1[1][0]==test[j][k]):
                count=count+1

total=0
for i in range(len(test_dict)):
    total=total+test_dict[i+1]


print(count)
acc=count/total
print("Accuracy",acc)



