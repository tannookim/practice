a = [7,8,3,4,5,6,4,8,7,8,'g','h','l','h']

print(a.count(7))

# 리스트 a에서 7을 모두 지워주세요.
while True:
    a.remove(7)
    if a.count(7) == 0:
        break
print(a)

for i in a:
    if i == 7:
        a.remove(i)
print(a)

