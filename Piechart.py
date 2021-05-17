import matplotlib.pyplot as plt
import numpy as np

def readfile(filename):
    with open(filename,encoding="utf8",mode="r") as file:
        datas = file.read().split("\n")
        data_arr = []
        for item in datas:
            line = item.split(',')
            data_arr.append(line)
    return data_arr

def count(datas):
    count = [0,0,0,0,0,0,0,0,0]

    for item in datas:
        line = item[5:7] + item[9:]
        # print(line)
        temp = 0
        for i in range(len(count)):
            if line[i] != '-1':
                temp += 1
        count[temp-1] += 1
    return  count

if __name__ == '__main__':
    # get data
    datas = readfile("clean_data.csv")
    #get labels
    labels = []
    for i in range(1,10):
        labels.append(str(i)+' MÔN')
    print(labels)
    #count
    c = datas[1:]
    counter = count(c)

    #creat piechart

    plt.pie(x=counter,labels=labels,autopct='%1.1f%%',startangle=90,
            wedgeprops={'edgecolor':'white','linewidth':1},
            counterclock= False,
            pctdistance= 20.0
            )

    plt.show()

