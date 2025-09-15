# import random
#
# number = random.randint(1,31)
# print(f'내 마음속 숫자:{number}')
# running = True
# while running:
#     guess = int(input('1~31 중 내가 생각한 숫자는?'))
#     print(f'입력 받은 숫자:{guess}')
#     if number > guess:
#         print('마음 속 숫자보다 작아요')
#     elif number < guess:
#         print('마음 속 숫자보다 커요')
#     elif number == guess:
#         print('정답!')
#         running = False


cup = 0
running2 = True

while running2:
    cup += 1
    print(cup)
    if cup == 10:
        break

for i in range(1,10):
    if i%3 ==0:
        continue
    print(i)


a = ['철수','미미','영수','영희']

a.append('성은')
print(f'리스느 a:{a}')

a.insert(2,'맹구')
print(f'리스느 a:{a}')

print(f'리스트 a의 길이는?: {len(a)}')

b = [1,2,3,4]
print(f'리스트 b의 길이는?: {len(b)}')

a.sort()
print(f'오름차순 정렬된 리스트 a:{a}')
a.sort(reverse=True)
print(f'내림차순 정렬된 리스트 a:{a}')

arr = [1,2,3,4]
print(arr)
arr[2:2] = ['a','b']
print(arr)

apple = [7,8,3,4,5,6,4,8,7,8,'g','h','l','h']
print(apple[1])
print(apple.index('h'))

#모든 7의 인덱스 번호를 출력하시오.
seven = 0
for ex in apple:
    if ex == 7:
        print(seven)
    seven += 1


#모든 h의 인덱스 번호를 출력하시오.
hhh = 0
while True:
    hhh = apple.index('h',hhh)
    print({hhh})
    hhh += 1
    # if hhh == len(apple)-1:
    #     break


