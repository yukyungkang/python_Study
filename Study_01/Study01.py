#괄호 안에 있는 것을 출력해줘 print는 전체는 소문자로 쓰는것으로 약속
print('Hello World!')

#괄호 안에 있는 내용이 한글로도 가능(+기호도 숫자도 가능하다)
print('토끼야 안녕!')

#숫자형
#정수, 실수도 가능하다
#숫자를 쓸때는 작은 따옴표를 사용하지 않아도 된다.
print(1)
print(-2)
print(3.14)

#연산자 더하기,빼기,곱하기,나누기 (+, - , *, /)
print(1+2)
print(3-2)
print(2*4)
print(6/3)

# 제곱,몫,나머지 (**, //, %)
print(5**2)
print(5//2)
print(5%2)

#예제
print(3+7)
print(6*3)
print(4**2) #제곱
print(9%5) #나머지

#문자열
#큰따옴표와 작은 따옴표를 이용하여 사용 가능
print('Hello World!')
print('3.14') #숫자열이 아닌 문자열로 인식 숫자는 따옴표 없이 작성
print('토끼야 안녕!')
print("토끼야 안녕!")

#문자열 연산
#사용 가능한 연산자는 +와 *
print('토끼' + '야 안녕!')
print('다람쥐' + '야 안녕!')
# 문자열 + 문자열은 붙이기 문자열 * 정수에 맞게 문자열이 표시(정수만 곱할 수 있다)
print('데굴' * 2)
print('데굴' * 4)

#문자열 더하기 연산자 사용하기
print('빨'+'주'+'노'+'초'+'파'+'남'+'보')

#변수 값(숫자나 문자)을 저장하는 공간 (예 상자에 값을 넣는다)
    #오른쪽에 있는 값을 왼쪽에 저장한다(할당 연산자)
    #예: 변수이름 = 저장할값
rainbow = '빨주노초파남보' #rainbow 라는 변수에 '빨주노초파남보'를 저장한다.
print(rainbow)

#프로램은 위에서 한줄씩 실행이된다. 변수의 값은 계속 바뀔 수 있다.
count = 0
print(count)
count = 1
print(count)
count = count + 1
print(count)

#변수는 문자와 숫자,_를 사용 가능하다
#대문자와 소문자를 구분한다
#공백이나 숫자로 시작 할 수 없다.
#미리 지정된 문자를 사용 할 수 없다(if, for 등등...)

#손님의 주문을 받아보기
coffee = 4100
juice = 4600
tea = 3900
print(coffee * 3 + juice * 2 + tea * 1) #커피 3잔, 주스 2잔, 홍차 1잔
print(coffee * 4 + juice * 3 + tea *3) #커피 4잔, 주스 3잔, 홍차 3잔
print(coffee * 1 + juice * 1 + tea * 2) #커피 1잔, 주스 1잔, 홍차 2잔

#주석
# 사람을 위해 남기는 메모 '#'을 이용하여 주석을 작성한다
# 코드 앞에 '#' 추가하면 컴퓨터가 볼수 없다(코드가 무시된다)

# 리스트 여러 개의 사탕을 하나의 변수에 저장하는 코드
candies = ['딸기맛', '레몬맛', '수박맛', '박하맛', '우유맛']
print(candies)

#리스트
# 여러개 값을 저장하는 것 / 값 사이에 콤마를 넣어 저장
# 리스트는 문자, 숫자 그리고 리스트 안에 리스트도 가능하다
#값을 추가하기
# .apped() 사용하면 리스트 뒤에 값을 추가 할 수 있다
# fltmxm.append(추가할값)
# 메소드는 특정한 자료형에서만 사용 할 수 있는 함수(함수는 입력이 들어갔을 때 출력)
clovers = []
clovers.append('클로버1')
print(clovers)
clovers.append('하트2')
print(clovers)
clovers.append('클로버3')
print(clovers)

#리스트 값에 접근하기
# 0 인덱스로 시작되며, 인덱스 안에 없는 숫자를 입력할 경우 범위를 벗어나 에러를 호출됨
# 리스트[접금할인덱스]
clovers = ['클로버1', '하트2', '클로버3']
print(clovers[1])
clovers[1] = '클로버2' #하트2에서 클로버2로 바꿔주겠다
print(clovers[1])
#리스트 값 제거하기
# del 리스트[제거할인덱스]
clovers = ['클로버1', '하트1', '클로버2', '클로버3']
print(clovers)
del clovers[1]
print(clovers)

#예제
candies = ['레몬맛','박하맛']
print(candies)
candies.append('콜라맛')
print(candies)
candies.append('포도맛')
print(candies)
del candies[1]
print(candies)

#여러 값 가져오기 (슬라이싱 방법)
day = ['월', '화', '수', '목', '금', '토', '일']
print(day[2:5])
print(day)

#예제 사탕주기
candies = ['딸기맛', '레몬맛', '수박맛', '우유맛', '콜라맛', '포도맛']
cat_candy = candies[0]
print('채셔고양이에게는', cat_candy, '사탕을 줘요.')
duck_candy = candies[1]
print('오리에게는 ', duck_candy, '사탕을 줘요.')
dodo_candy = candies[2:5]
print('도도새에게는', dodo_candy, '사탕을 줘요.')

#정렬하기
# 리스트.sort() 메소드
#   () 안에 여러 방법으로 정렬이 가능하다
#       (reverse=True) 내림차순 정렬
#       (key=len) 문자열 길이 기준 정렬
animals = [ '채셔고양이', '오리', '도도새']
animals.sort() #가나다라 순으로 정렬
print(animals)
animals.sort(reverse=True) #내림차순 정렬
print(animals)
animals.sort(key=len) #문자열 길이 기준 정렬
print(animals)
animals.sort(key=len, reverse=True) #길이 기준 내림차순 적용
print(animals)


