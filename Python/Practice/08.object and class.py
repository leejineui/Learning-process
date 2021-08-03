#object(객체, 인스턴스)? 속성(상태,특징)과 행위(행동,동작,기능)로 구성된 대상 
# 속성 : 변수  행위 :함수     변수 + 함수 = 객체 
# 객체 자전거  변수 색깔 크기  함수 전진 멈춤
#class object의 틀 

#class  클레스 명: 
#   [변수] 
# 
#   def 함수 (인자):
#       <코드블럭>

# class 선언 
class Bicycle():
    def move(self, speed):
        print("자전거 : 시속 {0} 킬로미터로 전전" .format(speed))


    def turn(self, direction):
        print("자전거: {0}회전".format(direction))

    def stop(self):
        print("자전거({0},{1}): 정지" .format(self.wheel_size)  )

#객체명 = 클레스명()         print(함수명(인자))
my_bicycle = Bicycle()

# 객체에 속성 할당  객체명.변수명 = 속성값
my_bicycle.wheel_size =26
my_bicycle.color ='black'

print("바퀴크기:", my_bicycle.wheel_size )
