# ✅ 튜플 (Tuple)
# - 리스트와 비슷하지만 **값을 변경할 수 없음(Immutable)**
# - **소괄호 `()`를 사용하여 생성**
# - 단, 소괄호 없이 쉼표(,)로 구분해도 튜플 생성 가능
# - 숫자, 문자, 리스트 등 다양한 자료형을 저장 가능

# ✅ 빈 튜플 생성
my_tuple = ()
print(my_tuple)  # 출력: ()

# ✅ 여러 자료형을 포함한 튜플 생성
my_tuple2 = (1, -2, 3.14)  # 숫자로만 입력
print(my_tuple2)  # 출력: (1, -2, 3.14)

my_tuple3 = '토끼', 10, 1.0, 1.2  # 소괄호 없이 문자와 숫자 작성
print(my_tuple3)  # 출력: ('토끼', 10, 1.0, 1.2)

# ✅ 값이 한 개인 튜플을 입력할 경우 반드시 쉼표(,) 필요
my_int = (1)  # 그냥 정수 1이 된다.
print(type(my_int))  # 출력: <class 'int'>

my_tuple4 = (1,)  # 튜플로 표현하고 싶으면 쉼표가 필요
print(type(my_tuple4))  # 출력: <class 'tuple'>

# ✅ 튜플의 특징
# - 리스트는 값을 변경할 수 있지만, 튜플은 변경할 수 없음
my_list = [1, 2, 3]
my_tuple5 = (1, 2, 3)

my_list[0] = 100  # 리스트는 값 변경 가능
print(my_list)  # 출력: [100, 2, 3]

# my_tuple5[0] = 100  # ❌ 튜플은 값 변경 불가능 → 오류 발생

# ✅ 튜플을 사용하는 이유
# 1️⃣ **값 변경 방지 (Immutable)**
#    - 튜플은 한 번 생성되면 값이 변경되지 않음.
#    - 중요한 데이터가 실수로 변경되는 것을 방지하여 **코드의 신뢰성(무결성)을 유지**할 수 있음.

# 리스트를 사용할 경우 값 변경 가능 (실수로 변경될 위험)
my_list = [1, 2, 3]
my_list[0] = 100  # 값 변경 가능
print(my_list)  # 출력: [100, 2, 3]

# 튜플을 사용할 경우 값 변경 불가능
my_tuple = (1, 2, 3)
# my_tuple[0] = 100  # ❌ 오류 발생 (튜플은 값 변경 불가능)

# 2️⃣ **리스트보다 빠른 연산 속도**
#    - 튜플은 리스트보다 **메모리 사용량이 적고, 연산 속도가 빠름**.
#    - 큰 데이터에서 성능이 중요한 경우 튜플을 사용하면 효율적.

import timeit

list_test = timeit.timeit(stmt="x = [1, 2, 3, 4, 5]", number=1000000)
tuple_test = timeit.timeit(stmt="x = (1, 2, 3, 4, 5)", number=1000000)

print("리스트 생성 시간:", list_test)  # 리스트 실행 속도
print("튜플 생성 시간:", tuple_test)  # 튜플 실행 속도

# 3️⃣ **파이썬 곳곳에서 사용**
#    - 튜플은 함수의 반환값, 딕셔너리의 키, 여러 개의 값 저장 등에서 자연스럽게 사용됨.
#    - 예제: 함수에서 여러 개의 값을 반환할 때 튜플을 사용

def get_position():
    return (10, 20)  # 튜플 반환

pos = get_position()
print(pos)  # 출력: (10, 20)

# 튜플을 사용하면 여러 개의 값을 한 번에 반환하고, 이후 값 변경을 방지할 수 있음.


# 튜플도 index를 이용하여 값을 가져올 수 있다
clovers = ('클로버1', '하트2', '클로버3')
print(clovers[1])  # 튜플에서 하트 2를 가져오는 코드
# 튜플은 한번 지정한 값은 바꿀 수 없다.

# ✅ 패킹과 언패킹 (Packing & Unpacking)
# 패킹과 언패킹 기본 개념 설명

# 튜플(Tuple)은 여러 개의 값을 하나로 묶어서 저장하는 자료형
# 튜플을 활용하면 여러 데이터를 하나로 묶어 관리할 수도 있고, 개별 변수로 쉽게 분해할 수도 있음
# 이러한 기능을 패킹(Packing)과 언패킹(Unpacking)이라고 함

# 1️⃣ 패킹(Packing) - 여러 개의 값을 하나의 튜플로 묶는 과정
# 여러 개의 데이터를 하나의 튜플로 저장하는 방법
# 소괄호(())는 생략 가능하지만, 명확한 표현을 위해 사용하는 것이 일반적

# 여러 개의 데이터를 하나의 튜플로 묶음 (패킹)
my_tuple = 3.14, 'Python', False  # 소괄호 생략 가능
print(my_tuple)  # 출력: (3.14, 'Python', False)

# 2️⃣ 언패킹(Unpacking) - 튜플에 저장된 값을 개별 변수로 분해하는 과정
# 튜플의 각 요소를 개별 변수에 할당하는 방법
# 변수의 개수는 튜플의 요소 개수와 반드시 일치해야 함

# 튜플의 각 요소를 개별 변수에 할당 (언패킹)
i, s, b = (123, 'abc', True)
print(i)  # 출력: 123
print(s)  # 출력: abc
print(b)  # 출력: True

# 3️⃣ 패킹과 언패킹을 활용한 실용적인 예제
# RGB 색상 값을 저장 & 분해하는 예제
# 함수에서 여러 개의 값을 반환할 때 활용하는 예제

# 🎨 RGB 색상 값 패킹 & 언패킹
# 튜플을 이용해 색상 값을 저장하고 개별 변수로 분해하는 예제

sky_blue = (135, 206, 235)  # 하늘색(RGB) 값을 튜플로 저장 (Packing)
r, g, b = sky_blue  # 튜플의 값을 각각의 변수로 할당 (Unpacking)
print('Red:', r, 'Green:', g, 'Blue:', b)  # 출력: Red: 135 Green: 206 Blue: 235

# 🏷️ 제품 정보 반환 (Packing & Unpacking 활용)
# 함수에서 여러 개의 값을 한 번에 반환할 때 활용하는 예제

def get_product():
    return "Wireless Mouse", 29.99, "Electronics"  # 튜플 형태로 여러 값 반환

product_name, price, category = get_product()  # 함수 반환 값을 언패킹하여 변수에 저장
print(product_name)  # 출력: Wireless Mouse
print(price)  # 출력: 29.99
print(category)  # 출력: Electronics



# dodo에는 박하맛 alice에는 딸기맛을 저장
# 패킹과 언패킹을 사용해 둘의 사탕을 교환하자
dodo = '박하맛'
alice = '딸기맛'
print('도도새:', dodo, '앨리스:', alice)
dodo, alice = alice, dodo
print('도도새:', dodo, '앨리스:', alice)
