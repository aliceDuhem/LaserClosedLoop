from ratioCodes import ratios

ratioDict = ratios.find_ratio(1.8)
# print(ratioDict)

laserIntensity = 1.2
wantedIntensity =1
testVals = [0.95, 0.9, 0.8,0.7,1.1,1.2,1.05]


for i in testVals:
    print(i)
    print(ratios.Pc_from_Pd(i,90))


test = ratios.csv_to_ratio('/Users/chooxuanwing/Desktop/Matlab works/LaserClosedLoop/MatlabStuff/ratioCSV')
print(test)