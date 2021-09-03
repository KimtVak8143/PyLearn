a = 60
# 60 = 0011 1100
b = 13
# 13 = 0000 1101
c = 0

print("a = ", a, ":", bin(a))
print("b = ", b, ":", bin(b))

c = a & b
print("AND of A, B = ", c, ":", bin(c))
c = a | b
print("OR of A, B = ", c, ":", bin(c))
c = a ^ b
print("XOR of A, B = ", c, ":", bin(c))
c = ~a
print("Complement of A = ", c, ":", bin(c))
c = a << 2
print("Left shift of A = ", c, ":", bin(c))
c = b >> 2
print("Right Shift of B = ", c, ":", bin(c))
