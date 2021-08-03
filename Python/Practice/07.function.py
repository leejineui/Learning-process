#특정 기능을 수행하는 코드의 묶음 
# def 함수명(인자):
#   <코드블록> 
#   return <반환값>
#print(함수명(인자))

# 인자도 반환도 없는 함수 

def my_func():
    print("안녕")

print(my_func())

# 인자는 있으나 반환 값이 없는 함수 

def my_friend(friendName):
    print("{}는 나의 친구입니다.".format(friendName))

print(my_friend("이진의"))


def my_student_info(name,school_ID,phoneNumber):
    print("================")
    print("-이름:",name)
    print("-ID:", school_ID)
    print("-전화번호:", phoneNumber)
    print("================")


print(my_student_info("현아", "01", "01114579"))


# 인자를 코드내에서 list 로 만들어 버리기 
def my_student_info(student_info):
    print("================")
    print("-이름:",student_info[0])
    print("-ID:", student_info[1])
    print("-전화번호:", student_info[2])
    print("================")


student_info=["현아", "01", "01114579"]
print(my_student_info(student_info))

# 인자도 있고 반환 값도 있는 함수 
def my_calc(x,y):
    z=x*y
    return z

print(my_calc(3,5))


# lambda 함수 
# lambda <인자> :<인자 활용 수행 코드>

mysquare = lambda x: x**2
print(mysquare(2))

mySimpleFunc = lambda x,y,z : 2*x +3*y + z 
print(mySimpleFunc(4,5,6))


# 유용한 내장 함수 
print(int(0.123)) # int 정수로 바꾸기 

int()
float()
str()
list()
tuple()
set()

# min()
# max()
# sum()
# abs()  # 절대값 
# len() 
# len((1,2,3,4,5))
# len([1,2,3,4,5])
# len({1,2,3,4,5})
# len({1:'tom',2:'jan',3:'you',4:'me',5:'we'})  #5
# len("ab cd") #5

print(bool())  # False
print(bool(2)) #True   뭐라도 있으면 True 
print(bool("a")) #True

myfriend =[]
print(bool(myfriend)) # False

# bool 함수의 이용 
def print_name(name):
    if bool(name):
        print("입력된 이름 :", name)
    else:
        print("입력된 이름이 없습니다.")

print(print_name(""))
print(print_name("dlwlsdml"))

# 총합과 평균 구하기 
# scores = [90,80,95,85]

# sum=0  # sum=[] 는 안됨  list 에 못들어감  append 해야됨 

# for s in scores:
#     sum= sum + s 

# avg = sum/len(scores)
# print(sum)
# print(avg)

# print("총점: {0}, 평균{1}" .format(sum, avg))


scores = [90,80,95,85]

# a= sum(scores)
# b= a/len(scores)

print("총점: {0}, 평균{1}" .format(sum(scores), sum(scores)/len(scores)))
print("최대: {0}, 최소{1}" .format(max(scores), min(scores)))