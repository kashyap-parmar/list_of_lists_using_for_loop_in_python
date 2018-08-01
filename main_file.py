# list_of_lists_using_for_loop_in_python
Creating the lists of lists in python

m = int(input(""))
n = int(input(""))


inner_list = []
outer_list = []




for i in range(0,m):
    
    for j in range(0,n):
        
        no = int(input(""))
        
        inner_list.append(no)
    
    outer_list.append(list(inner_list))
    inner_list=[]

print(outer_list)
