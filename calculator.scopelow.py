#지수는 따로 계산해야할거같다..
def cal(n):
    
    recur = ''
    i = -1
    while(1): #기존 for를 무한루프로 바꾸고, 그냥 종료조건을 괄호없앨때 까지 반복시키고 n도 계속 업뎃되게하여 소수점나와도 문제 x
        i += 1
        if n[i] == '(':
            for j in range(i, len(n)):
                if n[j] == ')':
                    a = n[:i]
                    b = n[j+1:len(n)]
                    recur = cal(n[i+1:j+1])
                    n = a + recur + b
                    i = -1
                    break
            else:
                pass
        
        if '(' not in n:
            break

    
    order = []
    n = n.replace(')', '').strip() #문자열 입력이라 n을 얻을때 경우에 따라 ')'가 붙어나와서 괄호 기호들을 다 지워버림
    if '--' in n:
        n = n.replace('--', '+') #마이너스 두개는 플러스
    if '++' in n:
        n = n.replace('++', '') #중복되는 플러스들 다 삭제함

    for t, i in enumerate(n): #반복문을 통해 수식에있는 연산자를 순서대로 order 리스트에 넣어줌
        if '+' in i:
            if t == 0:
                pass
            else:
                order.append('+')
        elif '-' in i:
            if (t == 0 or n[t - 1] == '^' or n[t - 1] =='+' or
             n[t - 1] == '*' or n[t - 1] == '/') :
                pass
            else:
                order.append('-')
        elif '*' in i:
            order.append('*')
        elif '/' in i:
            order.append('/')
        #elif '^' in i:
            #order.append('^')
    

    for i in range(len(n)):
        if n[i] == '+': #숫자를 구분하기위해, 연산자를 모두 ';'로 바꿔버림
            x = n[:i]
            y = n[i+1:]
            n = x + ';'+ y
        elif ((n[i] == '-' and i != 0) and 
        (n[i] == '-' and n[i - 1] != ';')):
            x = n[:i]
            y = n[i+1:]
            n = x + ';'+ y
        elif n[i] == '*':
            x = n[:i]
            y = n[i+1:]
            n = x + ';'+ y
        elif n[i] == '/':
            x = n[:i]
            y = n[i+1:]
            n = x + ';'+ y
        

    temp = n.split(';') #숫자들을 temp리스트에 모아넣음(문자열)
    if '' in temp:
        temp.remove('')
    
    num = []
    for i in temp:
        num.append(float(i)) #수식에 있는 숫자들을 순서대로 num 리스트에 넣어줌(부동소수점으로 변환)

    if len(num) == 1:
        order = [] #마이너스 관련 작업을 하다보면 order에 +만남아 들어갈수가 있음... 그래서 그거 없애주기

    #3241^((-1.5)/(-1.2))
    iter = len(order)
    while(1): #총 연산자 갯수만큼 연산을 하면 됨
        if order == []:
            break  
        for j in range(len(order)): #일단 반복문으로 해결 ^^ 이렇게 찾을때마다 break시키고 다중반복하면 인덱스 변해도 곱셈 범위 유지가능
            for t, i in enumerate(order): #연산이 길어지면 이런게 더필요함.... 나중에생각해보자.
                if '*' in i:
                    num[t] = num[t] * num[t + 1] #계산에 필요한 숫자의 인덱스와 해당 숫자로 계산하기위해 필요한 연산자의 인덱스는 일치함
                    num.pop(t+1) #remove로하면 겹치는 원소가 존재하면 해당원소 지우질 못함 ex) 2+3*6*2/2 (2가 여러개있는데 인덱스를 잡아줘도 값이 같으면 앞에꺼를 삭제해버림, 따라서 pop을써야)
                    order.remove('*') #연산자는 어차피 순서대로 계산이라 상관없음, 사용한 연산자는 리스트에서 삭제
                    break
        #-8*-9*-100*0.32-100
        
        flag = 0 #0으로 나누는 경우 반복을 빠져나갈 깃발
        for j in range(len(order)):
            for i in range(len(order)):
                if order[i] == '/':
                    if num[i + 1] == 0: 
                        print('/////////////0으로 나눌수는 없어요/////////////')
                        flag = 1
                        break   
                    num[i] = num[i] / num[i + 1]
                    num.pop(i+1)
                    order.remove('/')
                    break
            if flag: break    
        if flag: break  

        for i in range(len(order)):
            if order[i] == '+':
                num[i] = num[i] + num[i + 1]
                num.pop(i+1)
                order.remove('+')
                break
        for i in range(len(order)):
            if order[i] == '-':
                num[i] = num[i] - num[i + 1]
                num.pop(i+1) 
                order.remove('-') 
                break

                
    return str(round(num[0], 4)) #임시방편. 소수점 자르기


while(1):
    print('나눗셈후 곱셈은 분수로 판단됩니다.')
    n = input('필요한 연산을 띄어쓰기 없이 입력해주세요: ')
    if '^' in n:
        a = n[:n.index('^')]
        b = n[n.index('^')+1:]
    
        result = float(cal(a)) ** float(cal(b))
    else:
        result = float(cal(n))
    print(result)

