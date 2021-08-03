# Variable = data/ trim the data using variable    

# List
# list methods  54p  변수.메서드이름()
myFriends =['James', 'Robert', 'Lisa', 'Mary']
print(myFriends)
print(myFriends[3]) # 변수[index 넘버] 로 불러온다
myFriends.append('Thomas')
print(myFriends)
myFriends.insert(1,'Paul')
print(myFriends)
myFriends.extend(['Laura', 'Bettry'])
print(myFriends)

a=myFriends.pop() 
print(myFriends)
print(a) # 지워진 값만 프린트 

myFriends.sort()
print(myFriends)

myFriends.reverse()
print(myFriends)


#Tuple  : 삭제 변경 되지 않음 
tuple1=(1,2,3,4)
print(type(tuple1))
print(tuple1[1]) # 변수[index 넘버] 로 불러온다. 

T= 5,6,7,8
print(T) # (5, 6, 7, 8)

tuple2=(1,)  # 하나의 항목의 튜플 만들기 
print(tuple2)
tuple3= 2,
print(tuple3)

tuple6 = 'a','b','c','d','e'
print(tuple6)
print(tuple6.index('a'))
print(tuple6.count('a'))

print("------")
# set : 집합 만들기 

A={1,2,3,4,5}
B={4,5,6,7,8,9,10}
#print(A[1]) set 값은 변수[index 넘버]로 가져 올 수 없다. 인덱스가 없음으로.. 
print(next(iter(A)))  # how to get the element in set? 
print(type(A))
print(A&B)
print(A-B)
print(A|B)


#리스트, 튜플, 세트 간의 변환
print('''리스트, 튜플, 세트 간의 변환''') 

a=[1,2,3,4,5]
print(a)
print(type(a))

b=tuple(a)
print(b)
print(type(b))

c= set(b)
print(c)
print(type(c))

a= list(c)
print(a)
print(type(a))

print("Dictionary")
#dictionary 
capital = {"영국" : "런던", "프랑스":"파리", "스위스" : "베른", "호주":"멜버른"}
print(type(capital))

print(capital["영국"]) #  변수[key ]: index 값이 아닌 key 값으로 value 찾기 
capital["독일"] ="베를린" # 삽입과 수정하는 방법이 같음: 변수[key] = "설정 value 값"
print(capital) 
capital["호주"] = "켄버라"
print(capital)

# dictionary methods  66p  변수.메서드이름()

fruit_code = {"사과":101, "배":102, "딸기":103, "포도":104, "바나나":105}
print(fruit_code.keys()) # key를 list 형태로 반환
print(fruit_code. values()) # values 를 list 형태로 반환 
print(fruit_code.items()) # 쌍을 list 형태로 반환
fruit_code.update({"오렌지": 106, "수박":107})
print(fruit_code)
 

