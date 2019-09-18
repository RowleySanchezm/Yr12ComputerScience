num = 3
name = "Dave"
name_list = ["D","a","v","e"]

def add_one(num) :
    num = num +1
    return num
#end function

def add_s(name) :
    name = name +"s"
    return name
#end function

def append_s(name) :
    name.append("s")
    print(name)
#end procedure

print(add_one(num))
print(num)

print(add_s(name))
print(name)

append_s(name_list)
print(name_list)
