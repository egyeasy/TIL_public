# def g(x):
#     def h():
#         print(x) # 참조를 먼저 할 때 문제가 된다.
#         # x = 'abc' # 없으면 작동. 이 scope 내에서 x를 참조/재정의하려면 하나만 선택해라!
#     x = x + 1
#     print('in g(x): x = ', x)
#     h()
#     return x

# x = 3
# z = g(x)


# def g(y):
#     print(x)
#     def h():
#         print(x)
#         # x = 'abc' # 없으면 작동. 이 scope 내에서 x를 참조/변형하려면 하나만 선택해라!
#     # x = x + 1
#     print('in g(x): x = ', x)
#     h()
#     return x

# x = 3
# z = g(x)


# def g(y):
#     print(x)
#     def h():
#         print(x)
#     # x = 8 # 이게 없으면 코드 작동. 같은 scope 내에서 x 또다시 정의되어서는 안됨!
#     h()

# x = 3
# g(6)

# def g(x): # g(x)에 명시적으로 x를 넘겨준다면 문제 없다. 넘겨받은 걸로 덮어씀
#     print(x)
#     def h():
#         print(x)
#     x = 8
#     h()

# x = 3
# g(6)

# mutable
def h(y):
    x.append(4) # mutable은 global 것도 변형 가능. but 재정의하면 마찬가지로 에러.
    # x = [4, 5, 6] # 없으면 에러 안남.
    print(x)

x = [1, 2, 3]
h(3)


# def h(y):
#     # x.append(4)
#     x = [4, 5, 6]
#     print(x)

# x = [1, 2, 3]
# h(3)
# print(x)