# Conditions : 코드의 진행 순서를 바꾸는 구문 

# 단일 조건에 따른 분기(if)

#if <조건문>:
#    <코드 블럭>

x=100
if x >= 90:
    if x == 100:
        print("perfect")

    else:
        print("very good")

elif 90> x >=80:
    print("good")

else: 
    print("bad")

# for<반복변수> in < 반복 범위>:
#    <코드블록>

# <반복 범위> : 리스트와 range() 함수를 이용해 지정할 수 있음 


# 중첩문 
x_list = ['x1', 'x2']
y_list = ['y1', 'y2']

print("x,y")
for x in x_list : 
    for y in  y_list:
        print(x,y)  #  print() 함수에 , 를 쓰면 전체를 한 줄에 출력 할 수 있다. 


names = ['James', 'Robert', 'Lisa', 'Mary']
scores = [95,96,97,94]

for k in range(len(names)):
    print(names[k], scores[k])

#zip() 함수 : <길이가 같은 반복 범위>를 지정하고 데이터 별로 <반복 변수>를 지정해 이용할 수 도 있다. 
# for var1 , var2 in zip(list1, list2):
#           <코드 블록> 

for name, score in zip(names, scores):
    print(name, score)

# 조건에 따라 반복하는 while
# while <조건문>:
#    <코드 블록>


i = 0 
sum = 0 

while(sum<20):
    i= i+1
    sum = sum + i 
print("확인", i ,sum)

# break 되기 전까지 print
k=0 
while True: 
    k= k+1

    if(k>3):
        break 
    print(k)

for k in range(10): 
    if(k>2):
        break
    print(k)

# continue 가 실행돼 반복문의 처음으로 돌아가서 다음 반복으로 진행 continue 가 걸리면 그 조건만 취소

for k in range(5):
    if(k==2):
        continue 
    print(k,end= " ") #0 1 3 4

print("---------")

k=0
while True:
    k=k+1
    if (k==2):
        print("skip")
        continue
    if(k>4):
        break
    print(k)


# comprehension

# list comprehension 
#[<코드 블록> for <반복 변수> in <반복범위>]

numbers=[1,2,3,4,5]
square =[]

for i in numbers:
    square.append(i**2)

print(square)


square=[i**2 for i in numbers]
print(square)

#[<코드블록> for <반복변수>in<반복범위> if <조건문>]
numbers=[1,2,3,4,5]
square =[]

for i in numbers:
    if i >= 3:
        square.append(i**2)
        
print(square)

square= [i**2 for i in numbers if i>=3]
print(square)


        



