# 字典排序

key_value ={}     
 
# 初始化
key_value[1] = 2 
key_value[2] = 56       
key_value[3] = 323 
key_value[4] = 24
key_value[5] = 24 
key_value[6] = 18      


# 按键排序
def dictionairy1(dict):  
    # for i in sorted(dict):
    #     print(i)
    print('按键排序')
    print(sorted(dict.items(), key = lambda di:di[0]))

dictionairy1(key_value)

# 按值排序   
def dictionairy2(dict):
    print('按值排序')
    print(sorted(dict.items(), key = lambda di:di[1]))

dictionairy2(key_value)

# 字典列表排序
lis = [{ "name" : "Taobao", "age" : 100},  
{ "name" : "Runoob", "age" : 7 }, 
{ "name" : "Google", "age" : 100 }, 
{ "name" : "Wiki" , "age" : 200 }] 
  
# 通过 age 升序排序
print ("列表通过 age 升序排序: ")
print (sorted(lis, key = lambda i: i['age']) )
  
print ("\r") 
  
# 先按 age 排序，再按 name 排序
print ("列表通过 age 和 name 排序: ")
print (sorted(lis, key = lambda i: (i['age'], i['name'])) )
  
print ("\r") 
  
# 按 age 降序排序
print ("列表通过 age 降序排序: ")
print (sorted(lis, key = lambda i: i['age'],reverse=True) )