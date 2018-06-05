aobj=None
b_obj = None
my_dic={
    "A":{"a1":aobj},
    "B":{"b1":b_obj}
}

re = my_dic.get("A")
if(re["a1"] == None):
    re["a1"] ="updated"
print(re)