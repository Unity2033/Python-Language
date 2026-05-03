#region 조건문
# 어떤 조건이 주어질 때 해당 조건에 따라 동작을
# 수행하도록 실행하는 명령문입니다.

#region 관계 연산자
# 두 개의 피연산자의 값을 비교하여 그 결과를 논리적인 값으로 나타내는 연산자입니다.

# print("10 is less than 20 : " , 10 < 20)
# print("10 is greater than 20 : " , 10 > 20)
# print("10 is less than or equal to 20 : ", 10 <= 20)
# print("10 is greater than or equal to 20 : ", 10 >= 20)
# print("10 is not equal to 20 : ", 10 != 20)
# print("10 is equal to 20 : ", 10 == 20)

#endregion

#region if문
# 어떤 특정한 조건을 비교하여 조건이 일치하면
# 실행되는 명령문입니다.

# health = 0

# if health <= 0:
    # print("knocked out")

# if문은 조건식의 결과가 True 상태일 때 실행되며,
# False 상태일 때는 실행되지 않습니다.
#endregion

# region elif문
# 앞에 있는 조건이 일치하지 않은 경우 새로운 조건을 
# 검사하여 조건이 일치하면 실행되는 명령문입니다.

# level = 99

# if level < 11 :
    # print("1 Circles")
# elif level >= 99:
    # print("5 Circles")

# elif 문은 여러번 정의할 수 있으며, if문이
# 존재할 때 사용할 수 있습니다.
# endregion

# region else문
# 앞에 있는 조건문의 결과가 전부 일치하지 않으면
# 실행되는 명령문입니다.

# integer = 0

# if integer > 0:
   # print("positive")
# elif integer < 0:
   # print("negative")
# else:
   # print("integer")

# 앞에 연결된 조건문은 위에서부터 순서대로 검사하며,
# 가장 먼저 조건이 일치한 조건문만 실행됩니다.
# endregion

# region match - case문
# 하나의 값이 특정한 패턴과 일치하는지에 따라 분기가 실행하는 명령문입니다.

# key = "left"

#match key:
    # case "left":
        # print("◀")
    # case "right":
        # print("▶")
    # case _:
        # print("exception")
        
# match - case문의 경우 값을 순차적으로 비교하여 일치하는 경우 해당 코드를 실행하는 구조입니다.
# endregion

#region 논리연산자

#region AND 연산자
# 두 개의 조건이 다 성립될 때 실행되는 연산자입니다.

# x = 10
# y = 0

# if x != 0 and y == 0 :
   # print("x-intercept")

# 조건문에서 하나 이상의 조건이 있다면 왼쪽에서부터 검사합니다.
#endregion

#region OR 연산자
# 두 개의 조건 중에 하나라도 조건이 성립될 때 실행되는 연산자입니다.

# month = 12

# if month >= 12 or month <= 2:
    # print("It’s winter.")

# 조건문의 논리 표현식을 평가하는 도중에 결과가 이미 확정이 났다면, 그 이후의 평가는 생략합니다.
#endregion

#region NOT 연산자
# 하나의 조건을 반전시키는 연산자입니다.

#switch = False

#if not switch:
    #print("the switch is on")
#else:
    #print("the switch is off")
#endregion

#endregion

#endregion