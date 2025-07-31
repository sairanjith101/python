#Zero Division Error:
try:
    num1 = 10
    num2 = 0
    result = num1/num2
except ZeroDivisionError as ZE:
    print('Zero Division Error :: ' + str(ZE))
    print('~' * 60)

#Type Error:
try:
    num1 = 8
    print('result :: ' + num1)
except TypeError as TE:
    print('Type Error :: ' + str(TE))
    print('~' * 60)

#Value Error:
try:
    name = int('RKS')
    print(name)
except ValueError as VE:
    print('Value Error :: ' + str(VE))
    print('~' * 60)

#Multiple Errors:
try:
    num1 = 9
    num2 = int(input())
    result = (num1/num2)
    print('result :: ' + result)
except (ZeroDivisionError,TypeError,ValueError) as ME:
    print("Multiple Error :: " + str(ME))
    print('~' * 60)
