# Creating a dictionary via iterative method
def make_dictionary():
    l=[]
    t=()
    n = int(input("Enter the number of elements (Key,value) pairs you want to insert into the dictionary: "))
    print("Enter your key,value pairs separated by a comma (e.g - key('space')value)")
    for i in range(n):
        m,n=input().split()
        t=(m,n)
        l.append(t)

    d=dict(l)
    return d


dictionary1 = make_dictionary()
print(dictionary1)