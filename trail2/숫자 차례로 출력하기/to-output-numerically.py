n = int(input())

# Please write your code here.
def n_to_1(n):
    if n==0:
        return
    print(n,end=" ")
    n_to_1(n-1)

def one_to_n(n):
    if n==0:
        return
    one_to_n(n-1)
    print(n, end=" ")

one_to_n(n)
print()
n_to_1(n)