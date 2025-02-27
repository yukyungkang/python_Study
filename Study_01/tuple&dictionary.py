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
