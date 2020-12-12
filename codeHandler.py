import geohash
import json
import os
import shutil
import re
import googlemaps
import math
from datetime import datetime

def textReader():
    fileName = "provinces.txt"
    file_object = open(fileName)
    dict = {}
    with open(fileName) as f:
        line = f.readline()
        line = f.readline()
        while line:
            print(line)
            information = line.split()
            province = information[1]
            if ord(province[0])<=ord('9') and ord(province[0])>=ord('0'):
                print("===================numbers found!===============")
                print(line)
                # input()
                line = f.readline()
                continue
            lat = float(information[-2])
            lon = float(information[-1])
            code = geohash.encode(lat, lon, precision = 6)
            print(code)
            subName = code[0:3]
            subDict = dict.get(subName, {})
            str = ""
            for i in range(len(information)-2): str = str+" "+information[i]
            subDict[code] = str
            dict[subName] = subDict
            line = f.readline()

    print("============================encode finished================================")
    # print(dict)
    path = "./dics/"
    for key,value in dict.items():
        subDict = dict[key]
        # print(subDict)
        j = json.dumps(subDict)
        subName = key
        js = open(path+subName+".json","w")
        js.write(j)
        js.close()

def findNearestProvince(lat, lon, precis, K):
    folderPath = "./dics/"
    code = geohash.encode(lat,lon,precision=precis)
    print("GeoHash Code: "+code)

    # neighbours = geohash.neighbours(code)
    pre3 = code[0:3]
    json_list = os.listdir(folderPath)
    # print(json_list)

    n1 = findHelper(pre3,json_list,10)#find 10 nearest json files
    # print(n1,n2)

    middle = n1[-1]
    count = K+1
    i = 0
    provinces = []
    keys = []
    while count > 0:
        fileName = folderPath+n1[middle+i]
        with open(fileName) as f:
            file = json.load(f)

            key, res = dictFinder(code, file, count)

            count = count - int(key[-1])

            for loop in range(len(key)-1):
                provinces.append(res[loop])
                keys.append(distanceCal(code, key[loop]))
    d = dict(zip(keys, provinces))
    d_k = dict(sorted(d.items(), key=lambda x: x[0]))
    values = set()
    l = list(d_k.keys())[:]
    for loop in l:
        val = d_k[loop]
        if val in values:
            del d_k[loop]
        else:
            values.add(val)
    return d_k

def distanceCal(code1,code2):
    lat1, lon1 = geohash.decode(code1)
    lat1 = math.radians(float(lat1))
    lon1 = math.radians(float(lon1))
    lat2, lon2 = geohash.decode(code2)
    lat2 = math.radians(float(lat2))
    lon2 = math.radians(float(lon2))
    x = (lon2 - lon1) * math.cos((lat1+lat2)/2)
    y = lat2 - lat1
    distance = (math.sqrt(x * x + y * y)) * 6371
    return distance

# return the same type as the list
def findHelper(code, list, K):
    length = len(list)-1
    left = 0
    right = len(list)-1
    while right>=left:
        mid =  int((left+right)/2)
        m = list[mid]
        if code>list[mid]:
            left = mid+1
        elif code<list[mid]:
            right = mid-1
        else:
            break
    ans = getKLists(mid, list, K)
    return ans

def dictFinder(code, dic, limit):
    if len(dic) < limit:
        return len(dic), dict
    else:
        res = []
        ans = findHelper(code, list(dic.keys()), limit)
        for i in range(len(ans)-1):
            res.append(dic[ans[i]])
        res.append(ans[-1])
        return ans, res



# return K nearest lists and append the spread center to the end of results
def getKLists(index, list, K):
    length = len(list)
    ans = []
    for i in range(int(K/2)):
        if (index - i) >= 0:
            ans.append(list[index - i])
            K = K - 1
    middle = K
    for i in range(K):
        if (index + i) < length:
            ans.append(list[index + i])
    ans.append(middle)
    return ans

def fileMover():
    file_list = os.listdir("./")
    for i in range(len(file_list)):
        s = file_list[i].split(".")
        if len(s)>1 and s[1]=="json":
            shutil.move("./"+file_list[i], "./dics")

def compare2provinces(orig, comp1, comp2, precis):
    if comp1==comp2: return comp1
    count1 = 0
    count2 = 0
    charOrig = [ord(char) for char in orig]
    char1 = [ord(char) for char in comp1]
    char2 = [ord(char) for char in comp2]
    for i in range(precis):
        count1 = count1 + abs(charOrig[i] - char1[i])
        count2 = count2 + abs(charOrig[i] - char2[i])
    return comp1 if count1<count2 else comp2


if __name__ == '__main__':
    # textReader()
    # print("The Geohash precision in this project is 6")
    # lat = float(input("Please input Latitude and press Enter: "))
    # lon = float(input("Please input Longitude and press Enter: "))
    # K = int(input("Please input how many provinces you want to find near this point: "))
    # print(findNearestProvince(lat,lon,6, K))
    ans = findNearestProvince(36.4611122, -109.4784394, 6, 6)
    for k,v in ans.items():
        print("The nearest reference point would be in" + str(v) + " with approximately "+ str(k) + " km distance")
    print("This results has removed the replicated points.")
    # print(geohash.encode(36.4611122,-109.4784394 ,precision=6))