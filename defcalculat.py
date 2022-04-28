def calculator(n):
    
    recur = ''
    for i in range(len(n)): #(1 + 2 + 3) * 3 - > [1, 2, 3, 3] [(, +, +, ), *]
        if i >= len(n):
            break #n값이 계속 업뎃 되는데, 이때 range에넣은 len(n)값은 변하지않아서 i가 업데이트된 len(n)보다 클수가있음, 그래서 빼버림
        if n[i] == '(':
            for j in range(i, len(n)):
                if n[j] == ')': #처음 괄호를 만나면, 일단은 포함해서 자름 
                    a = n[:i]
                    b = n[j+1:len(n)]
                    recur = calculator(n[i+1:j+1])
                    n = a + recur + b
                    break # 재귀를 통해 괄호 만날때마다 괄호 안에꺼 계산하고감
        
        else: #1 + (2 + 3) = [1, 2, 3] [+, (, + ,)]
            pass
       
    num = []
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
        elif '^' in i:
            order.append('^')
    

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
        elif n[i] == '^':
            x = n[:i]
            y = n[i+1:]
            n = x + ';'+ y

    temp = n.split(';') #숫자들을 temp리스트에 모아넣음(문자열)
    if '' in temp:
        temp.remove('')

    for i in temp:
        num.append(float(i)) #수식에 있는 숫자들을 순서대로 num 리스트에 넣어줌(부동소수점으로 변환)

    if len(num) == 1:
        order = [] #마이너스 관련 작업을 하다보면 order에 +만남아 들어갈수가 있음... 그래서 그거 없애주기

    
    iter = len(order)
    for k in range(iter): #총 연산자 갯수만큼 연산을 하면 됨
        for i in range(len(order)): #연산자의 숫자만큼 반복문을 통해 계산해줌, 제곱부터곱하기나누기더하기빼기 순으로 코딩하여 사칙연산 순서를 지키게함
            if order[i] == '^':
                num[i] = num[i] ** num[i + 1] #계산에 필요한 숫자의 인덱스와 해당 숫자로 계산하기위해 필요한 연산자의 인덱스는 일치함
                num.pop(i+1) #remove로하면 겹치는 원소가 존재하면 해당원소 지우질 못함 ex) 2+3*6*2/2 (2가 여러개있는데 인덱스를 잡아줘도 값이 같으면 앞에꺼를 삭제해버림, 따라서 pop을써야)
                order.remove('^') #연산자는 어차피 순서대로 계산이라 상관없음, 사용한 연산자는 리스트에서 삭제
                
        for j in range(len(order)): #일단 반복문으로 해결 ^^ 
            for t, i in enumerate(order): #연산이 길어지면 이런게 더필요함.... 나중에생각해보자.
                if '*' in i:
                    num[t] = num[t] * num[t + 1]
                    num.pop(t+1)
                    order.remove('*')
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

    return str(num[0])

while(1):
    print('나눗셈후 곱셈 - 분수로 판단됨')
    print('지수 내의 계산에선 괄호를 권장합니다.')
    n = input('숫자(연산자)숫자(연산자)숫자...로 입력해주세요: (띄어쓰기안됨)')
    print(calculator(n))


def A():
    
    Aa()
    Ab()

def Aa():
    print()

def Ab():
    print()