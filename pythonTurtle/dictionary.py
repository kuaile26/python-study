'''
brand = ["a", "b", "c", "d"]
slogan = ["everything is possible", "just do it", "haha", " i am d"]

print("my slogan is ", slogan[brand.index("just do it")])



#创造和产生字典

dic1 = {"a": "everything is possible", "b": "just do it" ,"c":"haha", "d": "i am d"}     #字典为映射类型
print(dic1["a"])


dic3 = dict((("F", 70),("i",105)))

print(dic3)

dict4 = dict(iloveyou = "forever")

print(dict4)

dict4[ "songqi"] = "i hate you"

print(dict4)
'''
dict1 = {}
dict1 = dict1.fromkeys(range(20), "")  #fromkeys

for eachkey in dict1.items(): #items
    print(eachkey)

print(dict1.get(32)) #get

dict1.clear()  #clear
print(dict1)

help( dict)