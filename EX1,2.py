def modulo(x, y):
    if x < y:
        return x
    else:
        return modulo(x-y, y)

print((modulo(6, 13)))
print(modulo(37, 10))
print(modulo(8, 2))
print(modulo(50, 7))

def reverseString(s, i = 0):
    if i == len(s):
        return ""
    return reverseString(s, i+1) + str(s[i])


print(reverseString(""))
print(reverseString("bonjour"))
print(reverseString("ressasser"))
