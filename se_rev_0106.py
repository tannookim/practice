int = 123
float = 3.14
octal = 0o117
hex = 0x8ff

print(f'int:{int}')

name = 'kim sung eun'
content = 'my content'
age = 34

multi = '''this is multi line string
thins is second line'''

print(f'{multi}')

print('name:'+name) #문자열과 변수를 할께 출력하는데 변수의 값이 문자일때는 {}중괄호를 넣지 않는다.

print('내 이름은 {0} 이고, 나이는 {1} 입니다.'.format(name, age))
print('내 이름은 '+name+'이고 나이는 '+str(age)+' 입니다.')
print(f'내 이름은 {name} 이고, 나이는 {age} 입니다.')

result = 7%2
print(result)

#두부가게에서 두부사오기
print('두부가게에 간다.')

#두부가 1개보다 많으면 두부를 사고 그렇지 않으면 순두부를 산다.
tofu = 0
if tofu > 0:
    print('두부를 산다.')
else:
    print('순두부를 산다.')

print('집으로 돌아온다.')


#콜라, 생수, 오렌지주스, 식혜, 이온음료

item = '콜라'

if item == '콜라':
    print(f'{item}가 나왔습니다.')

for cup in range(1,11):
    print(f'{cup}번 째 물을 가져왔습니다.')

print('for 문 연습 결과 이상!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#만약 커피 10을 타는데 한잔의 물에 믹스 2개씩을 넣고 믹스 넣을 때마다 3번 저어주어야 한다면?
for coffee in range(1,11):
    print(f'{coffee}번째 물을 떠왔습니다.')
    for mix in (1,3):
        print(f'{mix}번 째 믹스를 넣었습니다.')
        for spoon in range(1,4):
            print(f'{spoon}번째 스푼을 저었습니다.')

cup = 0
running2 = True

while running2:
    cup += 1
    print(cup)
    if cup == 10:
        running2 = False
