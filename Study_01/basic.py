#괄호 안에 있는 것을 출력해줘 print는 전체는 소문자로 쓰는것으로 약속
#Hello World! 출력하는 코드
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

# 변수(Variable)
# - 변수를 쉽게 말하면 **값을 저장하는 상자에 이름을 붙이는 것**과 같다.
# - 변수에는 숫자, 문자열 등 다양한 값을 저장할 수 있으며, 저장된 값은 언제든지 변경할 수 있다.
# - 변수에 값을 저장할 때 사용하는 기호(연산자)는 `=`이며,
#   **오른쪽 값을 왼쪽 변수에 저장(할당)**하는 역할을 한다.
#   (예: `변수이름 = 저장할값` → `count = 1`)
# - 변수는 프로그램 실행 중 한 줄씩 처리되며, **변수의 값은 계속 바뀔 수 있다.**

# 변수 이름 규칙
# - 문자, 숫자, 언더스코어(`_`) 사용 가능 (예: `my_var`, `count1`)
# - 대문자와 소문자를 구분함 (예: `MyVar`와 `myvar`는 다른 변수)
# - 변수 이름은 **숫자로 시작할 수 없음** (예: `1count` ❌)
# - 변수 이름에 **공백을 포함할 수 없음** (예: `my var` ❌)
# - **파이썬에서 미리 지정된 예약어(if, for 등)는 변수 이름으로 사용할 수 없음**

# 변수 예제
my_int = 1  # 정수 1을 저장
my_str = 'Python'  # 문자열 'Python'을 저장
my_bool = True  # 논리 값(True) 저장
my_list = [1, 2, 3]  # 리스트 [1, 2, 3] 저장

# 문자열 변수 예제
rainbow = '빨주노초파남보'  # rainbow 변수에 문자열 저장
print(rainbow)

# 변수 값 변경 예제
count = 0
print(count)  # 0 출력
count = 1
print(count)  # 1 출력
count = count + 1  # 기존 count 값에 1을 더함
print(count)  # 2 출력


# 복합 할당 연산자
# - **할당 연산자(`=`)와 사칙연산(+, -, *, / 등)을 함께 사용**하여 값을 간편하게 변경할 수 있다.
# - 기존 변수 값을 연산한 후, 그 결과를 다시 해당 변수에 저장하는 방식이다.
# - 복합 할당 연산자의 기본 구조: `변수 연산자= 값`  (예: `count += 3` → `count = count + 3`과 동일)
# - 사용 가능한 연산자: `+=, -=, *=, /=, %=, **=, //=`
#   (※ `//=`는 몫 연산, `**=`는 거듭제곱 연산)

count = 0
count += 3  # count = count + 3 (3 증가)
print(count)  # 출력: 3

count -= 1  # count = count - 1 (1 감소)
print(count)  # 출력: 2

count *= 2  # count = count * 2 (곱하기 2)
print(count)  # 출력: 4

count /= 2  # count = count / 2 (나누기 2)
print(count)  # 출력: 2.0 (※ 나누기 연산은 결과가 항상 `float`형)


# 문자열(String)
# - **작은 따옴표(')나 큰따옴표(")를 이용하여 문자열을 표현할 수 있다.**
# - **숫자를 작은 따옴표(') 또는 큰따옴표(")로 감싸면 문자열로 인식된다.**
# - `type()` 함수를 사용하면 변수의 자료형을 확인할 수 있다.

my_str1 = 'a'  # 한 글자로 된 문자열
print(my_str1)  # 출력: a

my_str2 = '3.14'  # 따옴표 안에 있기 때문에 숫자가 아닌 문자열
print(my_str2)  # 출력: 3.14
print(type(my_str2))  # 변수의 타입을 확인 (출력: <class 'str'>)

my_str3 = 'coding'  # 작은 따옴표 사용
print(my_str3)  # 출력: coding

my_str4 = "coding"  # 큰 따옴표 사용 (작은 따옴표와 동일한 역할)
print(my_str4)  # 출력: coding


# 문자열 연산(String Operations)
# - 사용 가능한 연산자는 `+`(문자열 연결)와 `*`(문자열 반복)이다.

# 문자열 + 문자열 → 두 문자열을 붙여서 연결
print('토끼' + '야 안녕!')  # 출력: 토끼야 안녕!
print('다람쥐' + '야 안녕!')  # 출력: 다람쥐야 안녕!

# 문자열 * 정수 → 문자열을 정수만큼 반복 (※ 정수만 곱할 수 있음)
print('데굴' * 2)  # 출력: 데굴데굴
print('데굴' * 4)  # 출력: 데굴데굴데굴데굴

#손님의 주문을 받아보기
coffee = 4100
juice = 4600
tea = 3900
print(coffee * 3 + juice * 2 + tea * 1) #커피 3잔, 주스 2잔, 홍차 1잔
print(coffee * 4 + juice * 3 + tea *3) #커피 4잔, 주스 3잔, 홍차 3잔
print(coffee * 1 + juice * 1 + tea * 2) #커피 1잔, 주스 1잔, 홍차 2잔

# 인덱싱(Indexing)
# - 문자열에서 특정 위치의 문자를 가져오는 방법이다.
# - Python에서 문자열은 0부터 시작하는 **인덱스(index)**를 가진다.
# - 예를 들어, 문자열 'Python'의 각 문자는 다음과 같은 인덱스를 가진다.
#   P  y  t  h  o  n
#   0  1  2  3  4  5  (양수 인덱스)
#  -6 -5 -4 -3 -2 -1  (음수 인덱스)
# - 특정 문자를 가져오려면 **대괄호(`[]`)를 사용하여 인덱스 값을 넣으면 된다.**

# 예제 문자열
alphabet = 'abcde'

# 양수 인덱스 사용 (왼쪽부터 0부터 시작)
print(alphabet[0])  # 출력: a
print(alphabet[3])  # 출력: d
print(alphabet[4])  # 출력: e

# 음수 인덱스 사용 (오른쪽부터 -1부터 시작)
print(alphabet[-5])  # 출력: a
print(alphabet[-2])  # 출력: d
print(alphabet[-1])  # 출력: e

# 슬라이싱(Slicing)
# - **인덱싱과 다르게 여러 개의 문자를 잘라서 가져올 수 있다.**
# - 문자열의 일부를 가져오려면 **대괄호(`[]`)와 콜론(`:`)을 사용하여 시작 인덱스와 끝 인덱스를 지정**한다.
# - 슬라이싱의 기본 구조: `문자열[시작인덱스:끝인덱스]`
#   → 시작 인덱스부터 **끝 인덱스 직전까지** 가져온다.
# - 예제 문자열 ('Hello Python!')의 인덱스:
#   H  e  l  l  o     P  y  t  h  o  n  !
#   0  1  2  3  4  5  6  7  8  9 10 11 12

# 예제 문자열
my_str = 'Hello Python!'

# 슬라이싱 예제
print(my_str[0:1])  # 출력: H (0부터 1 앞까지)
print(my_str[0:2])  # 출력: He (0부터 2 앞까지)
print(my_str[3:7])  # 출력: lo P (3부터 7 앞까지)

# - 앞 또는 뒤의 인덱스를 생략하면 자동으로 처음 또는 끝까지 선택된다.
print(my_str[:5])  # 출력: Hello (처음부터 5 앞까지)
print(my_str[6:])  # 출력: Python! (6부터 끝까지)

# 메소드(Method)
# - **특정한 기능을 수행하는 함수로, 특정 자료형에서 사용할 수 있는 함수이다.**
# - 문자열, 리스트 등 다양한 자료형에서 사용할 수 있는 메소드가 존재한다.

# 1. split() 메소드
# - 문자열을 특정 기준(기본: 공백)으로 나누어 리스트로 변환하는 함수
fruit_str = 'apple banana lemon'
fruits = fruit_str.split()  # 공백 기준으로 문자열을 분리하여 리스트로 저장

print(fruits)   # 출력: ['apple', 'banana', 'lemon']
print(fruits[0])  # 출력: apple
print(fruits[1])  # 출력: banana

# 2. format() 메소드
# - **문자열 안에 변수를 삽입하여 원하는 형식으로 출력할 수 있는 메소드**
# - `format()` 메소드와 중괄호 `{}`를 함께 사용하여 값을 삽입한다.
# - `format()`에 작성된 값이 **중괄호 `{}`에 순서대로 들어간다.**

print('Life is {}'.format('Short!'))  # 출력: Life is Short!
print('{} X {} = {}'.format(2, 3, 2 * 3))  # 출력: 2 X 3 = 6

# '''문자열''' (여러 줄 문자열, Multi-line String)
# - **작은 따옴표(`'''`) 또는 큰 따옴표(`"""`)를 3개 연속으로 사용하여 작성하는 문자열이다.**
# - 여러 줄에 걸쳐 작성할 수 있으며, 줄 바꿈이 자동으로 적용된다.
# - 주석처럼 사용할 수도 있지만, 일반적으로 **긴 문자열을 출력할 때 활용**된다.

print('''첫 번째
두 번째
세 번째''')

# 큰따옴표 3개(`"""`)를 사용해도 동일하게 동작함
print("""Hello
World!
Python""")

# 문장의 끝을 지정하기 (print()의 end 매개변수)
# - `print()` 함수에서 `end` 키워드를 사용하면 출력 결과의 끝을 원하는 문자로 지정할 수 있다.
# - 기본적으로 `print()`는 출력 후 자동으로 줄 바꿈(`\n`)을 하지만, `end`를 설정하면 이를 변경할 수 있다.
print('coding', end='')  # 기본 줄 바꿈 없이 출력됨
print('coding', end='-')  # 출력 후 "-"를 붙임
print('coding', end='\n')  # `\n`을 사용하면 줄 바꿈 (기본값과 동일)
print('coding', end='\t')  # `\t`를 사용하면 탭 간격 추가 (다음 출력이 일정 간격 뒤에 위치)

# 포맷 연산자 (% 연산자)
# - 문자열 내에서 `%d`, `%f`, `%s` 등을 사용하여 값을 삽입할 수 있다.
#   - `%d` : 정수(`int`) 값 삽입
#   - `%f` : 실수(`float`) 값 삽입
#   - `%s` : 문자열(`str`) 값 삽입
# - `%` 연산자를 사용하여 문자열과 값을 연결한다.

# 문자열 삽입 (%s)
print('Life is %s' % 'Short!')  # 출력: Life is Short!
# 정수 삽입 (%d)
print('%d X %d = %d' % (2, 3, 2 * 3))  # 출력: 2 X 3 = 6
# 실수 삽입 (%f) - 기본적으로 소수점 이하 6자리까지 출력됨
print('원주율은 %f 입니다.' % 3.1415926535)  # 출력: 원주율은 3.141593 입니다.
# 실수 소수점 자리수 제한 (%.nf 사용)
print('원주율은 %.2f 입니다.' % 3.1415926535)  # 출력: 원주율은 3.14 입니다.


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

#튜플, 딕셔너리
# 튜플은 리스트와 같으나 값을 변경 할 수 없다.(숫자, 문자, 리스트를 또 저장하는 것이 가능)
# 튜풀은 소괄호를 사용한다.
my_tuple = () #튜플에 값을 지정하지 않은 상태
print(my_tuple)

my_tuple2 = (1, -2, 3.14) #숫자로만 입력
print(my_tuple2)

my_tuple3 = '앨리스', 10, 1.0, 1.2 #소괄호 없이 문자와 숫자 작성
print(my_tuple3)

#값이 한개인 튜플을 입력 할 경우 반드시 콤마가 같이 되어야 한다.
my_int = (1) #그냥 정수 1이 된다
print(type(my_int))
my_tuple = (1,) #튜플이란걸 표현하고 싶으면 콤마가 들어가야한다.
print(type(my_tuple))

#튜플도 index를 이용하여 값을 가져올 수 있다
clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1]) #튜플에서 하트 2를 가져오는 코드
#튜플은 한번 지정한 값은 바꿀 수 없다.

#패킹과 언패킹
clovers = '클로버1', '하트2', '클로버3' #여러개의 값을 하나로 패킹한다.
print(clovers)
alice_blue = (240, 248, 255)
r,g,b = alice_blue
print('R:', r, 'G:', g, 'B:', b) #각각의 변수에 숫자가 들어가는 언패킹

#dodo에는 박하맛 alice에는 딸기맛을 저장
#패킹과 언패킹을 사용해 둘의 사탕을 교환하자
dodo = '박하맛'
alice = '딸기맛'
print('도도새:', dodo, '앨리스:', alice)
dodo, alice = alice, dodo
print('도도새:', dodo, '앨리스:', alice)










