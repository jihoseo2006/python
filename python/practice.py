# a = 123
# print(a)

# a = -321
# print(a)

# a = 0
# print(a)

# print(type(a))

# a = 10
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)

# a = 2
# b = 4
# print(a ** b)


# print("python is strong")
# print("You need Python")
# print(type("python"))

#작은 따옴표 표기
# a = "teacher's favorite food is apple"
# print(a)

#큰 따옴표 표기
# b = 'teacher says "you are good students"'
# print(b)

#이스케이프 시퀸스
# print("Teacher\ 's favorite food is apple")
# print("Teacher says \"you are good students\"")

#\n 사용하기

# line = "Python is strong\nYou need Python"
# print(line)


#큰따옴표 3개 사용

# line = """
# python is strong
# You need Python
# """
# print(line)


#문자열 연산
#문자열 더해서 연결하기 
# a = "python"
# b = " is"
# c = " strong"

# result = a + b + c
# print(result)
# print(a, b, c)

#문자열 곱해서 반복하기
# a = "python"

# result = a * 3
# print(result)

#곱하기 연산자 응용
# print("="*10)
# print("python")
# print("="*10)

#문자열 길이 구하기
# a = 'python is strong'
# print(len(a))

#문자열 인덱싱과 슬라이싱

#문자열 인덱싱: '가리킨다',슬라이싱: '잘라낸다'를 의미

#인덱싱
# a = "python is strong, you need python"
# print(a[0])
# print(a[5])
# print(a[18])

# print(a[-1])#음수 인덱스
# print(a[-6])

#문자열 슬라이싱

#a[x:y] 는 문자열 a 에 대해 인덱스 x부터 y이전까지 슬라이싱 한다.

# a = "python is strong, you need python"

# print(a[0:6])
# print(a[:6])

# print(a[:16])
# print(a[18:])

# print(a[:])


#슬라이싱에서도 음수 인덱스를 사용할수 있다.
# a = "python is strong, you need python"

# print(a[10:-17])
# print(a[18:-7])


#슬라이싱 예시
# a ="20010331Rainy"
# year = a[:4]
# day = a[4:8]
# weather = a[8:]
# print(year, day, weather)

# #주의! 문자열의 요솟값은 수정할수 없다.
# a = "pithon"
# a[1] = "y"
# print(a)
#이거 안된다!!

# #재할당으로 수정
# a = "python"

#문자열 포매팅
#문자열 포매팅이랑 문자열 안에 특정 값을 삽입하는 방법이다.

#1.포멧 코드 사용하기
# print("I have three %d pens" % 3)
# print("I have %s pens" % "three")

# a = 3
# b ="three"

# print("I have %d pens" % a)
# print("I have %s pens" % b)


#여러게 사용할때 사용하는 방식(튜플)
# a = 4
# b = 6
# print("I have %d apples and %d bananas" % (a, b))

#%s의 경우 숫자를 입력하더라도 문자열로 변환하여 출력한다.
# print("I have %s apples" % 3)

#정렬과 공백
# print("%10s" % "hi")
# print("%-10s" % "hi")
# print("%-10shi" % "teacher")

#소수점 표현하기
# print("%0.4f" % 3.42134234)
# print("%10.4f" % 3.42134234)

#format 함수를 사용한 포멧팅
# print("I eat {0} apples".format("3"))
# print("I eat {0} apples".format("five"))


#변수 대입하기 
# a = 5
# print("I eat {0} apples".format(a))

#2개 이상의 값 넣기
# a = 5
# b = 4
# print("I eat {0} apples and {1} bananas".format(a,b))

#이름으로 넣기
# print("I ate {number} apples. so I was sick for {days} days".format(number=10, days=3))

#f 문자열 포메팅
# name = "seo"
# age = 18
# print(f"My name is {name},my age is {age}")

#딕셔너리 자료형(나중에 배움.)사용법
      #키 :  벨류(값)
# d = {"name": "seo", "age": 18}
# print(f"나의 이름은{d[name]}입니다. 나이는 {d[age]}입니다.")

# a = "apple"
# print(a.count("p"))

#위치 알려주기 -1(find)
# a = "python is very strong"
# print(a.find("t"))
# print(a.find("is"))

#print(a.find("Q"))

#위치 알려주기 -2(index)
# a = "python is very strong"
# print(a.index("t"))
# print(a.index("is"))

# print(a.rindex("q"))
# 해당 문자가 처음으로 나온 인덱스를 반환한다

# 4.문자열 삽입(join)
# print(",".join('abcd'))
#구분자 조인(족)은 문자열의 문자마다 구분자를 삽입하여 문자열로 변환 후 반환한다.

# a = ",".join(['a', 'b', 'c', 'd'])
# print(a)


#문자열 바꾸기(리플레이스)
# a = "python is strong"
# print(a.replace("python", "my arm"))
# print(a)


# a = "python is very strong"
# b = a.replace("python", "my arm")
# print(a)
# print(b)


#문자열 나누기(스플릿)
# a = "Life is too short"
# a1 = a.split()
# print(a1)

# b = "1:2:3:4:5"
# b1 = b.split(":")
# print(b1)
#구분자로 문자열을 구분하여 리스트의 각 요소에 정리한다.

#리스트

#리스트 만들고 사용하기

# odd = [1, 3, 5, 7, 9]
# print(odd)
# print(type(odd))


#리스트의 인덱싱과 슬라이싱

#리스트의 인덱싱
# a = [1,2,3]
# print(a[0])
# print(a[1] + a[2])

# print(a[-1])


#삼중 리스트
# a = [1,2, ['a', 'b', ['life', 'is']]]

#리스트의 슬라이싱
# a = [1,2,3,4,5]
# print(a[0:2]
#중첩된 리스트에서 슬라이싱하기

# a = [1,2,3,['a','b','c'], 4,5]
# print(a[2:3])

# a = [1,2,3]
# b = [4,5,6]

# c = a + b
# print(c)

# a = [1,2,3]
# b = str(a[2]) + "hi"
# print(b)


#리스트 수정 및 삭제하기

# a = [1,2,3]
# a[2] = 4
# print(a)

# a= [1,2,3]
# del a[1]
# print(a)

# a = [1,2,3]
# a.append(4)
# print(a)

# a.append([5,6])
# print(a)

#리스트 정렬

# a = [1,5,3,2,4]
# a.sort(reverse=True)
# print(a)

# a = [1,2,3,4,5]
# i = a.index(3)
# print(i)

# a = [1,2,3,1,2,3]
# a.remove(3)
# print(a)

#리스트 요소 꺼내기(pop)
# a = [1,2,3,4,5]
# print(a.pop())
# print(a.pop())
# print(a)

#리스트 확장하기
# a = [1,2,3]
# a.extend([4,5])
# print(a)
# b = [6,7]
# a.extend(b)
# print(a)

#튜플

# t1 = ()
# t2 = (1,)

# t3 = (1,2,3)
# t4 = 1,2,3

# t5 =("a", "b", ('ab,cd'))

# print(type(t1))

# t2 = (1)
# print(type(t2))

#요소값 삭제:튜플은 요소 값을 수정할수 없음.

# t = (1,2, 'a', 'b')
# del t[0]

# t = (1,2 , 'a', 'b')
# t[0] = 3

# t = 1,2,3,4
# print(t[0])
# print(t[1])

#인덱싱
# t1 = 1,2,3
# t2 = 4,5,6
# t3 = t1 + t2
# print(t3)


#딕셔너리

# d = {"name": "seo", "age":18, "phone": "010-2276-9729"}
# print(type(d))
# print(d)

# a = {"a":[1,2,3]}
# print(a)

# a = "name"
# d = {a:"seo"}
# print(d)


#중복되게 사용하면 안된다!
# d = {1:'a',1:'b'}
# print(d)


#key에 리스트를 사용할수 없다.
# d = {[1,2,3]: 'a'}
# print(d)
#튜플은 가능하다.......

#딕 셔너리

# grade = {'pey': 10, 'julliet': 99}
# print(grade['pey'])
# print(grade['julliet'])

#딕 셔너리 관련 함수들
#key 값만 모아놓기
# a ={'name': 'pey', 'phone': '010-2276-9729', 'birth':'0322'}
# keys = a.keys()
# print(keys)

# a ={'name': 'pey', 'phone': '010-2276-9729', 'birth':'0322'}
# l = list(a.keys())
# print(l)
# print(type(l))

# a ={'name': 'pey', 'phone': '010-2276-9729', 'birth':'0322'}
# values = a.values()
# print(values)

# a ={'name': 'pey', 'phone': '010-2276-9729', 'birth':'0322'}
# print(a.get('name'))
# print(a.get('phone'))

#집합과 불

# s1= set([1,2,3])
# print(type(s1)) 
# print(s1)

# s2 = set("Hello")
# print(type(s2))
# print(s2)

#교집합
# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# s3 = s1 & s2
# print(s3)

# #차집합

# s1 = set([1,2,3,4,5,6])
# s2 = set([4,5,6,7,8,9])

# s3 = s1 - s2
# print(s3)

# s1 = set([1,2,3])
# s1.update([4,5,6])
# print(s1)

# s1 = set([1,2,3])


# a = [1,2,3,4]
# while a:
#     print(a.pop())

# print(bool("python"))
# print(bool(""))

#제어문

# money = 10000
# if money:
#     print("택시 타자")
# else:
#     print("걸어가자")

# money = 2900

# if money >= 3000:
#     print("택시타자")
# else:
#     print("걸어가자")

# money = 2900 
# if not money >=3000:
#     print("걸어가라")
# else:
#     ("택시타라")

# in, not in
# l = [1,2,3]
# t = (1,2,3)
# s = "String"

# print(2 in l)
# print(5 in l)
# print(2 in t)
# print(5 in t)
# print("r" in s)
# print("u" in s)

# l = ["paper", "cellphone", "money"]

# if "money" not in l:
#     print("걸어가라")
# else: 
#     print("택시타라")

# pocket = ["money", "card"]

# if "money" in pocket:
#     print("택시 타자")
# elif "card":
#     print("택시타자")
# else:
#     print("걸어가자")

# score = int(input())

# result =  "even" if score % 2 == 0 else "odd"
# print(result)

# list = ['one', 'two', 'three']
# for i in list:
#     print(i)

# list = ['one', 'two', 'three','four', 'five']
# for i in list:
#     print(i)


# a = [(1,2),(3,4),(5,6)]
# for (first, last) in a:
#     print(a)


# score = [90,25,87,45,80]
# for i in score:
#     if i>= 80:
#         print("%d 번째 학생은 합격" % (score.index(i) + 1))
#     else:
#         print("%d 번째 학생은 불합격" % (score.index(i) + 1))




# score = [90,25,87,45,80]
# for i in score:
#     if not i>= 50:
#         print("%d 번째 학생 보충학습입니다" % (score.index(i) + 1))
#     else:
#         continue

# temp = 0

# for i in range(1,11):
#     if i % 2 == 1:
#         temp += i
    
# print(temp)


# for i in range(2,10):
#     for j in range(1,10):
#         print("%d X %d = %d  " % (i, j, i*j),end="")
#         if j == 9:
#             print(sep="\n")

# list = [i for i in range(1,11)]
# print(list)

# list = [i for i in range(1,11)]
# list2 = [i for i in list if i % 2 == 1]
# print(list2)

# count = 1
# while count <=10:
#     print("나무를 %d번 찍었습니다." % count)
#     count += 1
# print("나무가 넘어졌습니다.")


# a ="Hello World!"
# number = 1
# while(number != 10):
#     print(a)
#     number = int(input("0을 입력하면 종료됩니다."))
# print("종료되었습니다.")

# coke = 10
# while 1:
    
#     money = int(input("금액을 입력해 주세요: "))
#     if coke ==0:
#         print("콜라가 다 떨어졌습니다..")

#     if money == 300:
#         print("콜라를 드립니다")
#     elif money > 300:
#         print("콜라를 드립니다 잔돈은 %d 원 입니다." % (money - 300))
#     else:
#         print("금액이 부족합니다.%d 원을 돌려드립니다." % money)


#함수

# def add(a , b):
#     return a + b

# print(add(1,2))

# def hel():
#     return "Hi"
# print (hel())

# def add(a, b):
#     print("%d" %(a+b))

# add(2,3)

# def say():
#     print("Hi")
# say()

# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#         return result
    
# print(add_many(1,2))
# print(add_many(1,2,3))
# print(add_many(1,2,3,4,5,6,7,8,9,10))

# def person(**kwargs):
#     print(kwargs)

# person(name="seo")
# person(name="seo", age = 18, height = 175)

# def say_myself(name, age, man = True):
#     print("나의 이름은 %s 입니다." % name)
#     print("나이는 %d살 입니다." % age)
#     if man: 
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# print(say_myself("seo", 18))
        

# a = 1
# def vartest(a):
#     a = a + 1

# vartest(a)
# print(a)

# a = 1
# def vartest():
#     global a
#     a = a + 1

# vartest()
# print(a)

# add = lambda a,b: a + b
# result = add(3,4)
# print(result)


# a = input()
# print(a)

#파일 생성하기
# w 쓰기 및 파일생성
# f =  open("새파일.txt", "w", encoding="utf-8")
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

#r 읽기
# f = open("새파일.txt", "r", encoding="utf-8")
# line = f.readline()
# print(line)
# f.close()


# f = open("새파일.txt", "r", encoding="utf-8")
# while True:
#     line = f.readline()
    
#     if line:
#       print(line)
#     else:  break
# f.close()


# f = open("새파일.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     print(line)
# f.close()

#공백 제거
# f = open("새파일.txt", "r", encoding="utf-8")
# lines = f.readlines()
# for line in lines:
#     line  = line.strip()
#     print(line)
# f.close()

# f = open("새파일.txt", "r", encoding="utf-8")
# data  = f.read()
# print(data)
# f.close()

#a 파일에 내용 추가

# f = open("새파일.txt", "a", encoding="utf-8")
# for i in range(11,20):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()


#with 
#with를 사용한 경우 with블록을 벗어나는 순간 파일객체 f가 자동으로 close된다.

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")

# f = open("foo.txt", "r")
# lines = f.readlines()
# print(lines)
# f.close()

#백준 알고리즘 풀기!!

#2408 - 주사위 세개

# l = list(map(int, input().split()))
# l.sort()
# if l[0]==l[1] and l[1]==l[2]:
#     print(10000 + l[0] * 1000)
# elif l[0]==l[1] :
#     print(1000 + l[0] * 100)
# elif l[1]==l[2] :
#     print(1000 + l[1] * 100)
# else:
#     print(l[2]* 100)

#2884 - 알람시계
# (h,m) = map(int,input().split())

# if m < 45:
#     d = 45 - m
#     m = 60 - d
#     if h == 0:
#         h = 23
#     else:
#         h = h - 1
# else:
#     m = m - 45
# print(h,m)

#25304 - 영수증

# totalcost = int(input())

# count = int(input())
# costtotal = 0

# for i in range(count):
#     cost,costcount = map(int, input().split())
#     costtotal += (cost * costcount)
# if totalcost == costtotal:
#     print("Yes")
# else:
#     print("No")

#번호 기억 안남 - 별찍기 4

# ru = int(input())

# for i in range(1,ru+1):
#     print(" " * (ru-i) + "*" * i)

 #5597 - 과제 안내신 분?

# l = [i + 1 for i in range(30)]
# result = []

# for _ in range(28):
#     a = int(input())
#     if a in l: l.remove(a)
# print(l[0])
# print(l[1])

# 2562 - 최댓값

# numbers = [int(input()) for _ in range(9)]

# print (max(numbers))
# print (numbers.index(max(numbers)) + 1)


#클래스

# class Calculator:
#     def __init__(self):
#         self.result = 0
  
#     def add(self, num):
#         self.result += num
#         return self.result

#     def sub(self, num):
#         self.result -= num
#         return self.result
    
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(1))
# print(cal1.add(2))
# print(cal2.add(3))
# print(cal2.add(4))

#사칙연산 계산기 만들기

# class Calculator:
#     def setdata(self, data1, data2):  #self는 자기자신(객체 임!) 파라미터 아님!
#         self.data1 = data1
#         self.data2 = data2
        
#     def add(self):
#         result = self.data1 + self.data2
#         return result
#     def sub(self):
#         result = self.data1 - self.data2
#         return result
#     def mul(self):
#         result = self.data1 * self.data2
#         return result
#     def div(self):
#         result = self.data1 / self.data2
#         return result
    
# inputs = Calculator()

# inputs.setdata(1,2)
# print(inputs.add())

# sum = 0
# n = int(input())
# s = list(input())

# for i in range(n):
#     sum += int(s[i])

# print(sum)

# #백준 10809
# al = input() #26개
# a = [-1] * 26

# for i in al:
#     a[ord(i)-97] = al.index(i)
# for i in a:
#      print(i, end=" ")


#클래스

# class Calculator:
#     def __init__(self):
#         self.result = 0
  
#     def add(self, num):
#         self.result += num
#         return self.result
#     def sub(self, num):
#         self.result -= num
#         return self.result

# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(1))
# print(cal1.add(2))
# print(cal2.add(3))
# print(cal2.add(4))

# print(cal1.sub(1))
# print(cal1.sub(2))
# print(cal2.sub(3))
# print(cal2.sub(4))

# class Calculator:
#     def setdata(self, num1, num2):
#         self.num1 = num1
#         self.num2 = num2

#     def add(self):
#         result = self.num1 + self.num2
#         return result

        
#     def sub(self):
#         result = self.num1 - self.num2
#         return result
    
        
#     def mul(self):
#         result = self.num1 * self.num2
#         return result
    
        
#     def div(self):
#         result = self.num1 / self.num2
#         return result
    
# class MoreCalculator(Calculator):
#     def pow(self):
#         result = self.num1 ** self.num2
#         return result

# a = MoreCalculator()
# a.setdata(3, 2)
# print(a.add())
# print(a.sub())
# print(a.mul())
# print(a.div())
# print("")
# print(a.pow())

# n = int(input())
# for _ in range(n):
#     a, b = input().split() 
#     a = int(a)
#     b = list(b) #문자열 b를 list를 사용하여 하나씩 리스트에 삽입
#     for i in range(len(b)):
#         print(b[i]*a, end="") # 리스트 요소를 하나씩 a만큼 반복하여 출력
#     print("")


# import mod1
# print(mod1.add(1, 2))
# print(mod1.sub(3, 1))


# import mod2

# a = mod2.Math()
# print(a.solv(2))

#패키지 안의 함수 실행하기
#방법 1. import 방법

# import game.sound.echo

# game.sound.echo.echo_test()

#방법 2 form ~ import
# import game.sound.echo

# game.sound.echo.echo_test()


#방법 3 from ~ import로 직접 함수 import하기

# from game.sound.echo import echo_test

# echo_test()

# from game.sound.echo import *
# echo_test()

#예외처리

# try:
#   n = int(input())
#   m = 10 / n
#   print(n)
# except:
#   print("Error")

# l = [10,20,30]

# try:
# 	index, x = map(int,input("input index and num: ").split())
# 	print(l[index] / x)
# except ZeroDivisionError:
# 	print("Can't divide by Zero")
# except IndexError:
# 	print("Wrong Index")
	
# try:
#     print(1+'b')
# except TypeError:
#     print("Error")
    
#발생 오류와 오류 변수까지 포함한 except 문

# l = [10,20,30]

# try:
# 	index, x = map(int,input("input index and num: ").split())
# 	print(l[index] / x)
# except ZeroDivisionError as e:
# 	print(e)
# except IndexError as e:
# 	print(e)

#else와 finally

#else try문을 실행 중 오류가 발생하였을 때는 
#except문을 실행하지만 오류가 발생하지 않을 경우 
#else문을 실행하게 된다.
	
# try:
#     x = int(input("input number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# else:
#     print(y)

#finally
#예외 발생 여부와 상관없이 항상 실행하고 싶은 코드가 있을 경우 
#finally 를 사용할 수 있다.

# try:
#     x = int(input("input number: "))
#     y = 10 / x
# except ZeroDivisionError:
#     print("Can't divide by Zero")
# else:
#     print(y)
# finally:
#     print('코드 실행이 끝났습니다.')


#예외 발생시키기
#raise

# try:
#     x = int(input("3의 배수를 입력하세요: "))
#     if x % 3 != 0:
#         raise Exception("3의 배수가 아닙니다.")
#     print(x)
# except Exception as e:
#     print(e)


#백준 문제풀기

# a,b = input().split()

# a = int(a)
# b = int(b)

# print(a/b)

# a,b = input().split()

# a = int(a)
# b = int(b)

# print(a + b)

#1152

# word = input().split()
# print(len(word))