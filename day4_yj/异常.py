

names=["aiden","bob"]

try:
    print(names[2])

except IndexError as e:
    print("列表中不存在该值",e)



