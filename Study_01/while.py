# while 조건 반복문
# 조건이 거짓이되면 끝난다.
num = 0
while num < 3: #num이 3보다 작으면 들어간다
    print('안녕 거북이', num)
    num = num + 1 #num +1을 해서 다시 저장했다

#조건 반복하기
#조건1: while의 코드블록을 5번만 반복하게 하세요
#조건2: 반복할 때마다 몇 번째 바퀴인지 출력하세요
#조건3: 전부 다 돌면 '경주 끝!'을 외치세요
count = 0
while count < 5:
    count = count + 1
    print(count, '번째 바퀴입니다.')
print('경주 끝!')