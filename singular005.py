import num as n
def sample(math):
    #math=[[2,4],[1,2]]
    abc=n.linealgo.abc(math)
    if(abc!=0):
        print(abc)
        print("number is non singular")
    else:
        print(abc)
        print("number is singular")
sample([[2,4],[1,2]])


#[[2,4],[1,2]]
