mylist = ['banana', "banana", "cherry", "apple", "5", True]
mylist.append("lemon")
mylist.insert(1, "blueberry")
mylist.append("dragon fruit")
last_item = mylist.pop( )
print(mylist)
print(f"last item : {last_item}")

mylist.remove("banana")
# mylist.remove("banana1")  # non esisting so error
# mylist.clear()  # all clear
print(mylist)
 
list2 = list()
list3 = []
print(list2)
print(list3)

nums = [1, 2, 4, 3, 6, 5]
print(nums)
nums.sort()
print(nums)

new_list = mylist + nums
# new_list.sort()  # error
print(new_list)