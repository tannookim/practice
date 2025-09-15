mem = {
    'kim':63, 'lee':88, 'park':97, "gang":77, "hwang":100, "ga":65,
    "na":92, "la":90, "wang":100, "gu":79
}

#90점 이상인 사람의 이름만 출력
for set in mem.items():
    if set[1]>=90:
        print(f'90점 이상인 사람 : {set[0]}')
