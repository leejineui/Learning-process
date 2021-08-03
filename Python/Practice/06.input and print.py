# print , 로 구분하면 출력에서 자동으로 빈칸(공백)이 하나씩 들어간다. 
print("Best","python","book")

#sep = 문자열 추가 
print("Best","python","book", sep = "++")

# +는 빈칸이 없다. 
print('abd'+'bds')
print("Best","python","book" +":") #Best python book:

# 변수 이름을 이용해 출력할때는 따옴표 없어야 함 
x=10
print(10) 

#\n 출력할 때 줄이 바뀜
print("James is \n korean")
#James is
#korean

# print 함수는 항상 뒤에 줄바꿈이 있다고 생각. 같이 쓰고 싶을 때는 end=" "
print("나") 
print("너")

print("나", end='') #나너
print("너")


#%s : 문자열 %d : 정수

name ="광재"
print("%s는 내친구" %name) #광재는 내친구

#.format
animal_0="cat"
animal_1="dog"
animal_2="fox"

print( "Animal : {0}" .format(animal_0))

print( "Animal : {1}" .format(animal_0, animal_1,animal_2))
print( "Animal : {0}, {2}" .format(animal_0, animal_1,animal_2))
print( "Animal : {}, {}" .format(animal_0, animal_1,animal_2)) # cat, dog
print( "Animal : {}, {},{}" .format(animal_0, animal_1,animal_2)) # cat, dog, fox


num= input("숫자를 입력하세요: ")
print("당신이 입력한 숫자는 {} 입니다.".format(num))

c= input("정사각형 한 변의 길이는?: ")
area=float(c)**2
print("정사각형의 넓이: {}" .format(area))


