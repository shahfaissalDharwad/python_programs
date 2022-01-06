myDict = {
    "fast" :"in a quick manner",
    "harry" : "a coder",
    "marks" : [1,2,5],
    "anotherdict" :{'harry':'player'},
    1 : 2
}
# print(myDict["fast"])
# print(myDict["harry"])
# print(myDict["marks"])
myDict["marks"] = [45,55]
print(myDict["marks"])
print(myDict["anotherdict"]["harry"])

#dictionary methods
print(list(myDict.keys())) #prints the keys of the dictionary
print(myDict.values()) #prints the values of the dictionary
print(myDict.items()) #prints the (keys,values) for all contenteds of  the dictionary

updateDict = {"lavish" : "friend",
"monish": "friend",
"rahul" : "friend"}
myDict.update(updateDict) #updates the dictionary by adding key value pairs from updateDict
print(myDict)
print(myDict.get("harry2"))