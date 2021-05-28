# # # 혼자작성해본 1번 답
# students = {'A':100, 'B': 50, 'C':85, 'D':78, 'E':75, 'F':45}

# x = list(students.items())

# x.sort(key=lambda a : a[1], reverse=True)

# v = (x[0], x[1], x[2])

# def prize(**kwargs):
    # c = 0
    # for a, b in v:
    #     c = c + 1
    #     print(c, '등', ':', a, b, '점')
        

# prize()

def prize2(kwargs):
  x = list(kwargs.items())
  x.sort(key=lambda a : a[1], reverse=True)
  v = (x[0], x[1], x[2])
  c = 0
  for a, b in v:
    c = c + 1
    print(f'{c} 등 : {a, b} 점')
    

##################################
students = {'A':100, 'B': 50, 'C':85, 'D':78, 'E':75, 'F':45}

rank_list = sorted(students.items(), key=lambda x: x[1], reverse=True)

fail = list(filter(lambda x: x[1] <= 50 , rank_list))
leng = len(students) - len(fail)
for i in range(len(fail)):
    print(f'{leng+i+1}등 : {fail[i][0]} {fail[i][1]}점')


# for i in range(3):  # i = 0, 1, 2
    # print(f'{i+1}등 : {rank_list[i][0]} {rank_list[i][1]}점')
