# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence

print('EX1-1 -')
print(__name__)
# 실행영역이 이파일 자체가 메인이다 __main__

# id vs __eq__ (==)증명
x = {'name':'kim', 'age': 33, 'city' : 'Seoul'}
y = x

print('EX2-1 -', id(x), id(y)) # 얕은 복사(copy)
print('EX2-2 -', x == y) 
print('EX2-3 -', x is y)
print('EX2-4 -', x,y)

x['class'] = 10
print('EX2-5 -', x, y)

print()
print()

z = {'name':'kim', 'age': 33, 'city' : 'Seoul', 'class' : 10}

print('EX2-6 -', x, z)
print('EX2-7 -', x is z) # 같은 객체
print('EX2-8 -', x is not z)
print('EX2-9 -', x == z) # 값이 같다
print('EX2-10 -', id(x), id(z)) 

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성)비교, ==(__eq__) 는 값 비교
# 데이터가 많은경우 == 보단 is로 먼저 객체아이디값을 비교하는게 좋다.

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2))
print('EX3-2 -', tuple1 is tuple2)
print('EX3-3 -', tuple1 == tuple2)
print('EX3-4 -', tuple1.__eq__(tuple2)) # ==

# Copy, Deepcopy(깊은 복사, 얕은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1)

print('EX4-1 -', tl1 == tl2)
print('EX4-2 -', tl1 is tl2)
print('EX4-3 -', tl1 == tl3)
print('EX4-4 -', tl1 is tl3)

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1)
print('EX4-6 -', tl2)
print('EX4-7 -', tl3)

print()
print(id(tl1[2]))
tl1[1] += [110, 120]
tl2[2] += (110, 120)

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플 재 할당(객체 새로 생성)
print('EX4-10 -', tl3)
print(id(tl1[2]))

# 리스트안에 튜플은 선호하지 않는다.

print()
print()

# Deep Copy 깊은 복사

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = []
        else:
            self._products = list(products)
    
    def put_prod(self, prod_name):
        self._products.append(prod_name)
    
    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

Basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
Basket2 = copy.copy(Basket1)
Basket3 = copy.deepcopy(Basket2)

print('EX5-1 -', id(Basket1), id(Basket2), id(Basket3))
print('EX5-2 -', id(Basket1._products), id(Basket2._products), id(Basket3._products))

print()

Basket1.put_prod('Orange')
Basket2.del_prod('Snack')

print('EX5-3 -', Basket1._products)
print('EX5-4 -', Basket2._products)
print('EX5-5 -', Basket3._products)

print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y # x + y
    return x

x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y)
print()

a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b) # 가변형 a -> 원본 데이터 변경

c = (10, 100)
d = (5, 10)

print('EX6-3 -', mul(c, d), c, d) # 불변형 c -> 원본 데이터 변경안됨

# 파이썬 불변형 예외
# str, byte, frozenset, Tuple: 사본 생성 x -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1)
tt3 = tt1[:]

print('EX7-1 -', tt1 is tt2, id(tt1), id(tt2))
print('EX7-2 -', tt3 is tt1, id(tt3), id(tt1))


tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 -', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5))
print('EX7-4 -', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2))

