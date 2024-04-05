def call_by_value(x):
    x=x*2
    print("function value updated to:",x)
    
def call_by_reference(list):
    list.append("D")
    print("function list updated to:",list)
    
my_list=["E"]
num=2
print("number before:", num)
call_by_value(num)
print("list before:",my_list)
call_by_reference(my_list)