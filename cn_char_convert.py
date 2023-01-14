import csv
import os
import sys

characterFile = "translations/zh_Hans_CN/traditional_simplified.csv"

class CnCharConvert():
    def __init__(self) -> None:
        loaded=0
        curPath = os.path.dirname(os.path.realpath(sys.argv[0]))
        paths = [characterFile,os.path.join(curPath,characterFile)]
        self.simpDict = {}
        self.tradDict = {}
        for path in paths:
            if os.path.exists(characterFile):
                print("Found character translations in:",characterFile)
                with open(characterFile, encoding="gbk") as f:
                    reader=csv.reader(f, delimiter=',')
                    self.simpDict={row[0]:row[1] for row in reader}
        self.tradDict={v:k for k,v in self.simpDict.items()}
        print("Loaded:",len(self.simpDict),"conversions")

    def ConvertToTrad(self,input: str):
        result = input
        for char in input:
            if char in self.simpDict:
                result=result.replace(char, self.simpDict[char])
        return result
    def ConvertToSimp(self,input: str):
        result = input
        for char in input:
            if char in self.tradDict:
                result=result.replace(char, self.tradDict[char])
        return result      
    def ContainsTrad(self, input: str):
        for char in input:
            if char in self.tradDict:
                return True
        return False

if __name__ == "__main__":
    test = CnCharConvert()
    testStr = "麻煩"
    result = test.ConvertToSimp(testStr)
    print("Converted",testStr,"to:",result)