# 치환문의 예

a = 1
b = a + 1

print(a, b)

# 동적 타이핑 : 변수에 새로운 값이 할당되면 값을 버리고 새로운 값으로 치환된다.

a = 1
print(a, type(a))
a = 'hello'
print(a, type(a))


# 확장 치환문
a = 10
a += 10 # a = a + 10
print(a)
