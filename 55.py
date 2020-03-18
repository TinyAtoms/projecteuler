from tools.words import is_palindrome




def is_lychrel(n, count=0):
    if count > 50:
        return True
    new_number = int(str(n)[::-1]) + n
    if is_palindrome(str(new_number)):
        return False
    else:
        return is_lychrel(new_number, count + 1)



lychrels = []
for i in range(1,10000):
    if is_lychrel(i):
        lychrels.append(i)
        print(i)

print(len(lychrels))