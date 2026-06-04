A = input()

# Please write your code here.
def is_pallin(word:str)->bool:
    return word == word[::-1]

print('Yes' if is_pallin(A) else 'No')