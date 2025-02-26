# ✅ print() 함수 사용법
# - print() 함수는 괄호 안에 있는 값을 출력하는 역할을 한다.
# - 전체 소문자로 작성해야 하며, 괄호 안에는 문자, 숫자, 연산 결과 등을 넣을 수 있다.

# 1️⃣ 문자열 출력
print('Hello World!')  # 문자열 출력
print('토끼야 안녕!')  # 한글 출력도 가능

# 2️⃣ 숫자 출력 (정수 및 실수)
print(1)  # 정수 출력
print(-2)  # 음수 출력
print(3.14)  # 실수 출력

# 3️⃣ 연산자 사용하기
# - 더하기, 빼기, 곱하기, 나누기 (+, -, *, /)
print(1 + 2)  # 덧셈
print(3 - 2)  # 뺄셈
print(2 * 4)  # 곱셈
print(6 / 3)  # 나눗셈 (결과는 실수로 출력)

# 4️⃣ 특수 연산자
# - 제곱 (**), 몫 (//), 나머지 (%)
print(5 ** 2)  # 5의 제곱
print(5 // 2)  # 5 나누기 2의 몫
print(5 % 2)  # 5 나누기 2의 나머지

# ✅ 연산자 예제
print(3 + 7)
print(6 * 3)
print(4 ** 2)  # 제곱 연산
print(9 % 5)  # 나머지 연산

# ✅ 변수(Variable)
# - 변수는 데이터를 저장하는 상자로, 특정 값에 이름을 붙여 보관할 수 있음.
# - 변수에는 숫자, 문자열, 리스트 등 다양한 값을 저장할 수 있으며, 저장된 값은 언제든지 변경 가능.
# - 변수 선언: `변수이름 = 값`

# 1️⃣ 변수 예제
my_int = 1  # 정수 저장
my_str = 'Python'  # 문자열 저장
my_bool = True  # 논리 값 저장
my_list = [1, 2, 3]  # 리스트 저장

# 2️⃣ 변수 활용 예제
rainbow = '빨주노초파남보'  # 문자열 변수
print(rainbow)  # 변수 값 출력

# 3️⃣ 변수 값 변경
count = 0
print(count)  # 출력: 0
count = 1
print(count)  # 출력: 1
count = count + 1  # 기존 count 값에 1을 더함
print(count)  # 출력: 2

# ✅ 복합 할당 연산자
# - `변수 연산자= 값` 형식으로 사용하며, 연산 후 해당 값을 변수에 저장함.
# - 사용 가능한 연산자: `+=, -=, *=, /=, %=, **=, //=`

count = 0
count += 3  # count = count + 3
print(count)  # 출력: 3

count -= 1  # count = count - 1
print(count)  # 출력: 2

count *= 2  # count = count * 2
print(count)  # 출력: 4

count /= 2  # count = count / 2
print(count)  # 출력: 2.0 (※ 나누기 연산 결과는 float형)

# ✅ 문자열(String)
# - 작은 따옴표(')나 큰따옴표(")를 이용하여 문자열을 표현할 수 있다.
# - 숫자를 작은 따옴표(') 또는 큰따옴표(")로 감싸면 문자열로 인식된다.
# - `type()` 함수를 사용하면 변수의 자료형을 확인할 수 있다.

# 예제:
# 'a' → 한 글자로 된 문자열
# '3.14' → 숫자처럼 보이지만 문자열
# 'coding' → 문자열
# "coding" → 동일한 문자열 표현 방식

my_str1 = 'a'
print(my_str1)  # 출력: a

my_str2 = '3.14'
print(my_str2)  # 출력: 3.14
print(type(my_str2))  # 출력: <class 'str'>

my_str3 = 'coding'
print(my_str3)  # 출력: coding

my_str4 = "coding"
print(my_str4)  # 출력: coding

# ✅ 문자열 연산(String Operations)
# - 문자열은 `+`(연결)와 `*`(반복) 연산이 가능하다.

# 예제:
# '토끼' + '야 안녕!' → '토끼야 안녕!'
# '데굴' * 2 → '데굴데굴'
# '데굴' * 4 → '데굴데굴데굴데굴'

print('토끼' + '야 안녕!')
print('다람쥐' + '야 안녕!')
print('데굴' * 2)
print('데굴' * 4)

# ✅ 손님의 주문을 받아보기 (문자열과 숫자 활용)
# - 커피(4100원), 주스(4600원), 홍차(3900원)의 가격이 주어졌을 때,
#   특정 개수를 주문하면 총 금액을 계산할 수 있다.

coffee = 4100
juice = 4600
tea = 3900

# 예제:
# 커피 3잔, 주스 2잔, 홍차 1잔 주문 → 4100 * 3 + 4600 * 2 + 3900 * 1
print(coffee * 3 + juice * 2 + tea * 1)

# 커피 4잔, 주스 3잔, 홍차 3잔 주문
print(coffee * 4 + juice * 3 + tea * 3)

# 커피 1잔, 주스 1잔, 홍차 2잔 주문
print(coffee * 1 + juice * 1 + tea * 2)

# ✅ 인덱싱(Indexing)
# - 문자열에서 특정 위치의 문자를 가져오는 방법
# - 문자열은 0부터 시작하는 **인덱스(index)**를 가진다.

# 예제 문자열: 'abcde'
# a  b  c  d  e
# 0  1  2  3  4  (양수 인덱스)
# -5 -4 -3 -2 -1  (음수 인덱스)

alphabet = 'abcde'

# 예제:
# alphabet[0] → 'a'
# alphabet[3] → 'd'
# alphabet[-1] → 'e'

print(alphabet[0])  # 첫 번째 문자 (a)
print(alphabet[3])  # 네 번째 문자 (d)
print(alphabet[-1])  # 마지막 문자 (e)

# ✅ 슬라이싱(Slicing)
# - 문자열에서 여러 개의 문자를 잘라서 가져올 수 있음.
# - `문자열[시작인덱스:끝인덱스]` 형식 사용 (끝 인덱스는 포함되지 않음).
# - 앞 또는 뒤의 인덱스를 생략하면 자동으로 처음 또는 끝까지 선택된다.

# 예제 문자열: 'Hello Python!'
# H  e  l  l  o     P  y  t  h  o  n  !
# 0  1  2  3  4  5  6  7  8  9 10 11 12

my_str = 'Hello Python!'

# 예제:
# my_str[0:1] → 'H'
# my_str[0:2] → 'He'
# my_str[3:7] → 'lo P'

print(my_str[0:1])
print(my_str[0:2])
print(my_str[3:7])

# 예제:
# my_str[:5] → 'Hello' (처음부터 5 앞까지)
# my_str[6:] → 'Python!' (6부터 끝까지)

print(my_str[:5])
print(my_str[6:])

# 메소드(Method)
# - **특정한 기능을 수행하는 함수로, 특정 자료형에서 사용할 수 있는 함수이다.**
# - 문자열, 리스트 등 다양한 자료형에서 사용할 수 있는 메소드가 존재한다.

# 1. split() 메소드
# - 문자열을 특정 기준(기본: 공백)으로 나누어 리스트로 변환하는 함수
fruit_str = 'apple banana lemon'
fruits = fruit_str.split()  # 공백 기준으로 문자열을 분리하여 리스트로 저장

print(fruits)  # 출력: ['apple', 'banana', 'lemon']
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

# 이스케이프 코드
# - 특정한 기능을 수행하는 특수한 문자 조합.
# - 문자열 내에서 줄바꿈, 탭, 따옴표 등 특수 문자를 표현하는 역할을 함.

# ✅ 대표적인 이스케이프 코드
# 1️⃣ \n : 줄바꿈 (엔터와 같은 효과)
# 2️⃣ \t : 수평 탭 (스페이스보다 넓은 공백)

# 줄바꿈 예제
print('줄바꿈\n줄바꿈')  # \n을 사용하여 줄바꿈 수행

# 탭 예제
print('탭\t탭')  # \t를 사용하여 수평 탭 적용

# ✅ 백슬래시(\) 자체를 출력하는 방법
# - 백슬래시는 이스케이프 코드로 사용되므로, 문자열에서 백슬래시 자체를 출력하려면 \\를 사용해야 함.

print('백슬래시 출력: \\')  # 백슬래시를 출력하려면 \\ 사용
print('이스케이프 코드 출력: \\n')  # 이스케이프 코드 문자 자체를 출력

# ✅ 따옴표를 문자열에 포함시키는 방법
# - 작은따옴표(')나 큰따옴표(")를 문자열 내에서 그대로 사용하려면 이스케이프 코드(\)를 사용하거나,
#   따옴표의 종류를 바꿔서 감싸면 됨.

# 작은따옴표를 포함한 문자열
print("I'm yours")  # 큰따옴표("")로 감싸면 작은따옴표 사용 가능
print('I\'m yours')  # 작은따옴표를 포함하려면 \' 사용

# 큰따옴표를 포함한 문자열
print('그는 말했다. "안녕하세요!"')  # 작은따옴표로 감싸면 큰따옴표 사용 가능
print("그는 말했다. \"안녕하세요!\"")  # 큰따옴표를 포함하려면 \" 사용

# ✅ 주석(Comment)이란?
# - 주석은 코드에 대한 설명을 추가하는 역할을 한다.
# - 주석은 컴퓨터가 무시하며 실행되지 않기 때문에, 오직 **사람이 읽기 위한 내용**이다.
# - 코드의 이해를 돕기 위해 작성하며, 특히 복잡한 코드일수록 주석이 중요하다.

# ✅ 주석 작성 방법
# - `#` 기호를 사용하면 해당 줄의 내용이 주석 처리된다.
# - 주석은 코드의 오른쪽이나 별도의 줄에 작성할 수 있다.

# 예제 1: 코드 오른쪽에 주석 작성
print('안녕!')  # 문자열을 출력

print(123456)  # 숫자를 출력

print(2 + 3)  # 계산 결과를 출력

# 예제 2: 코드 전체를 주석 처리하여 실행되지 않도록 만들기
# print('이 코드는 실행되지 않습니다.')

# ✅ 주석을 사용하는 이유
# 1️⃣ 사람이 코드를 더 쉽게 이해할 수 있도록 설명을 추가하기 위해 사용
# 2️⃣ 시간이 지나도 코드의 기능을 쉽게 기억할 수 있도록 도움
# 3️⃣ 다른 사람이 코드를 볼 때 어떤 기능을 수행하는지 명확하게 알 수 있도록 작성

# 예제 3: 코드 설명을 위해 주석 추가
# 아래 코드는 사용자의 나이를 출력하는 코드입니다.
age = 25  # 나이 변수 선언
print('사용자의 나이는', age, '세입니다.')  # 나이 출력

# ✅ 여러 줄 주석 (Multi-line Comment)
# - 여러 줄에 걸쳐 설명이 필요할 때는 작은 따옴표(`'''`)나 큰 따옴표(`"""`)를 세 개 연속으로 사용한다.
# - 여러 줄 주석은 보통 문서화 주석(Docstring)으로도 사용되며, 함수나 클래스의 설명을 작성할 때 활용된다.

'''
이 코드는 여러 줄 주석의 예제입니다.
여러 줄 주석은 작은 따옴표 세 개 ('*3) 또는 큰 따옴표 세 개 ("*3)로 작성할 수 있습니다.
'''

"""
이렇게 작성된 주석도 실행되지 않습니다.
주로 함수나 클래스 설명을 위해 사용됩니다.
"""

# ✅ 주석을 활용한 코드 비활성화
# - 특정 코드를 실행하지 않도록 주석 처리하여 일시적으로 비활성화할 수 있다.
# - 디버깅이나 테스트할 때 유용하게 활용할 수 있다.

# print("이 코드는 실행되지 않습니다.")  # 주석 처리된 코드 (실행되지 않음)
print("이 코드는 실행됩니다.")  # 주석이 없으므로 실행됨
