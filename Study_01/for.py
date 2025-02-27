# 🔄 반복문
# - 반복문은 동일한 작업을 여러 번 수행할 때 사용된다.
# - 파이썬에서 반복문은 `for`과 `while` 두 가지가 있다.
# - `for` 문은 보통 횟수를 기준으로 반복할 때 사용된다.

# 📝 for문의 기본 구조
# for 변수 in 순서열:
#     실행할 코드

# 🎯 예제1: 리스트의 요소를 하나씩 출력
my_list = [1, 2, 3]  # 리스트 생성
for count in my_list:
    print('횟수:', count)  # 각 요소를 하나씩 출력

# 🎯 예제2: 리스트의 요소를 하나씩 출력
characters = ['푸들', '포메라니안', '닥스훈트']
for character in characters:
    print(character, '산책가자')

# 🎯 횟수 반복하기
# - 특정 작업을 여러 번 반복할 때 for 문을 사용한다.
# - 리스트, 문자열, 숫자 등의 범위를 반복할 수 있다.

# 📌 단순 반복 예제
print('안녕 강아지 0')
print('안녕 강아지 1')

# ❌ 반복이 많아지면 하나씩 작성하기 어려우므로, for 문을 이용한다.
# ✅ for 문을 사용하면 반복적인 작업을 쉽게 처리할 수 있다.
for num in range(10):  # 🔄 0부터 9까지 반복 (10번 실행)
    print('안녕 강아지', num)

# 🎯 파이썬에서 반복문 종류
# - 횟수 기반 반복: `for` 문
# - 조건 기반 반복: `while` 문

# 📌 for 문 기본 구조
# for 변수 in 리스트:
#     실행할 명령(코드 블록)
for num in range(10):  # 🔄 0부터 9까지 반복
    print('안녕 강아지', num)  # 실행할 코드 블록

# 📌 리스트의 요소를 하나씩 가져와서 실행하는 방식
# - 리스트에 있는 값을 모두 가져올 때까지 반복
for num in [0, 1, 2]:
    print(num)

# 🎯 range() 함수
# - **반복문과 자주 함께 사용되는 함수**로, 특정 범위의 숫자 순서열을 생성한다.
# - **내장 함수(Built-in Function)**로, 별도의 모듈 없이 바로 사용 가능하다.
# - **0부터 입력한 값 -1까지의 정수**를 생성한다.

# 📌 예제 1: range()를 이용한 반복문
for count in range(3):  # 🔄 0부터 2까지 반복 (0, 1, 2)
    print('횟수:', count)

# 📌 range()를 리스트로 변환하여 확인
print(list(range(3)))  # 출력: [0, 1, 2]

# 🎯 range() 함수의 확장 사용법
# - range() 함수는 두 개의 값을 입력받아 시작(start)부터 끝(stop) 전까지의 숫자 순서열을 생성할 수 있다.

# 📌 range(start, stop)
# - start부터 stop **전까지** 숫자를 생성한다. (stop은 포함되지 않음)
# - 기본적으로 start를 생략하면 0부터 시작한다.

# 📌 예제 1: 0부터 2까지 반복 (기본 동작과 동일)
for count in range(0, 3):  # 🔄 0부터 2까지 반복
    print('횟수:', count)

# 📌 예제 2: 5부터 9까지 반복
for count in range(5, 10):  # 🔄 5부터 9까지 반복 (10은 포함되지 않음)
    print('횟수:', count)


# 🔠 문자열 반복문
# - 문자열도 리스트처럼 순서가 있는 자료형이므로 `for`문을 사용할 수 있다.
# - `for`문을 이용하면 문자열의 각 문자에 하나씩 접근할 수 있다.

# 🎯 예제: 문자열의 각 문자 출력
my_str = 'coding'  # 📌 문자열 선언
for letter in my_str:
    print('문자:', letter)  # 각 문자 출력

# 📝 들여쓰기 (Indentation)
# - **들여쓰기는 코드 블록을 구분하는 역할**을 한다.
# - **일반적으로 띄어쓰기 4칸**을 사용한다.
# - **일관된 들여쓰기 사용 필수** (탭과 띄어쓰기를 혼용하면 오류 발생 가능)

# 🎯 예제 1: 기본적인 들여쓰기 사용
nums = [0, 1, 2]  # 리스트 생성
for num in nums:  # 🔄 nums 리스트의 요소를 순회
    print(num)  # ✅ num을 출력 (0 → 1 → 2 순서)
print(nums)  # ✅ for문 종료 후 리스트 전체 출력

# 🎯 예제 2: 코드 블록 내에서 들여쓰기 적용
nums = [0, 1, 2]
for num in nums:
    print(num)  # ✅ num을 출력 (0 → 1 → 2)
    print(nums)  # ✅ for문 내에서 nums를 출력 (반복 실행)

# 🔍 실행 흐름:
# 1️⃣ `print(num)` 실행 후 `print(nums)` 실행
# 2️⃣ 다시 `print(num)`으로 돌아가 반복 수행
# 3️⃣ `nums` 리스트의 모든 요소를 순회할 때까지 반복됨

# 🎯 중첩 for문 (Nested for loop)
# - for문 안에 또 다른 for문을 작성하여 중첩할 수 있다.
# - 바깥쪽 for문이 한 번 실행될 때, 안쪽 for문은 모든 반복을 수행한다.

# 📌 예제: 중첩된 for문을 사용한 반복 출력
for j in range(2):  # 🔄 바깥쪽 for문 (j: 0 ~ 1)
    for i in range(2):  # 🔄 안쪽 for문 (i: 0 ~ 1)
        print('i:{}, j:{}'.format(i, j))  # 📌 i와 j 값을 출력

# ✅ 실행 결과
# i:0, j:0
# i:1, j:0
# i:0, j:1
# i:1, j:1

# 💡 중첩 for문을 활용하면 이중 반복이 필요한 다양한 문제를 해결할 수 있다.
# 예를 들어, 구구단 전체 출력, 2D 리스트 순회 등이 가능하다. 🔢

# 순서열 만들기
for num in range(3):
    print(num)

for y in range(1, 10):
    print(2, 'x', y, '=', 2 * y)

total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    total += num  # total에 num 값을 더함
print(f"1부터 10까지의 합은 {total}입니다.")

# 계산 과정까지 출력 (
total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    total += num  # total에 num 값을 더함
    print(total, "+", num, "=", total)  # 계산 과정을 출력
print(f"1부터 10까지의 합은 {total}입니다.")
# 현재 코드에서 중간 계산 과정이 생략되는 이유는 변수 total이 이미 더해진 상태에서 출력되기 때문

# 중간 과정까지 출력
total = 0  # 합을 저장할 변수
for num in range(1, 11):  # 1부터 10까지 반복
    print(total, "+", num, "=", total + num)  # 더하기 연산 수행 전의 값을 출력
    total += num  # total에 num 값을 더함
print(f"1부터 10까지의 합은 {total}입니다.")

total = 1  # 곱셈의 초기값은 1

for num in range(1, 11):  # 1부터 10까지 반복
    print(total, "x", num, "=", total * num)  # 곱하기 연산 수행 전 값을 출력
    total *= num  # total에 num 값을 곱함

print(f"1부터 10까지의 곱한 값은 {total}입니다.")

# for롸 리스트 인덱스를 사용해 roses의 '하얀장미'를 모두 '빨간장미'로 바꾸기
roses = ['하얀장미', '하얀장미', '하얀장미']
for i in range(3):
    roses[i] = '빨간장미'
print(roses)
