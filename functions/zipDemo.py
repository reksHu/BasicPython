numbers=[10086,10000,10010,95588]
names = ["移动","电信","联通"]
zip_obj=zip(numbers,names)
# for no,name in zip_obj:
#     print(name," Number:",no)

# d = dict(zip(numbers,names))

#updated
d= dict(zip_obj)
print(d)