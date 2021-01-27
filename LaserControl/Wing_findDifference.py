from ratioCodes import ratio
from ratioCodes import absolute


ratioDict = ratio.find_ratioDict(1.8)
# print(ratioDict)

laserIntensity = 1.2
wantedIntensity =1
Plaser_testVals = [0.95, 0.9, 0.8,0.7,1.1,1.2,1.05]


for i in testVals:
    print(i)
    print(absolute.Pc_from_Pd(i,90))


test = ratio.csv_to_ratioDict('/Users/chooxuanwing/Desktop/Matlab works/LaserClosedLoop/MatlabStuff/ratioCSV')
print(test)