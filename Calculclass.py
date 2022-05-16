class Calculator:
    def RecurCalculator(self, input_): #여기서는 매개변수 주지않아도 괜찮
        self.input_ = input_
        bcnt = Calculator.BracketCount(self.input_)
        
        for i in range(bcnt):
            bketix_1st, bketix_2nd = Calculator.BracketIndexAppend(self.input_)
            self.input_ = Calculator.RecurEngine(bketix_1st, bketix_2nd, self.input_)

        modinput_ = Calculator.DeleteMultiOperator(self.input_)
        op = Calculator.GetOperator(modinput_)
        num = Calculator.GetNumber(modinput_)
        res = Calculator.ComputeEngine(num, op)

        return res

    def BracketCount(input_):
        bketcnt = 0
        for i in range(len(input_)):
            if input_[i] == '(':
                bketcnt += 1
        return bketcnt

    def BracketIndexAppend(input_):
        bketix_1st = []
        bketix_2nd = []
        for i in range(len(input_)):
            if input_[i] == '(':
                bketix_1st.append(i)

            if input_[i] == ')':
                bketix_2nd.append(i)
                break
        return bketix_1st, bketix_2nd


    def RecurEngine(bketix_1st, bketix_2nd, input_):
        obj = Calculator() #이렇게 호출해줄땐 매개변수를 주어야함!
        #재귀 타고 들어갈 함수가 Calculator 클래스의 self 매개변수? 인자를 가진 
        #RecurCalculator라는 함수라서 이렇게 매개변수를 줘야 
        #변수 한개 필요한데 두개줬다 라는 오류가 안뜸
        #이게 정확히 맞는진 모르겠으나 나의 예측은... 그럼
        if bketix_1st == [] and bketix_2nd == []:
                pass
        else:
            u = max(bketix_1st)
            v = bketix_2nd[0]
            fir = input_[:u]
            sec = input_[v+1:]
            recur = obj.RecurCalculator(input_[u+1:v])
            input_ = fir + recur + sec
        return input_

    
    def DeleteMultiOperator(input_): #++과 --를 삭제 해주는 함수    
        input_ = input_.replace(')', '').strip() #문자열 입력이라 n을 얻을때 경우에 따라 ')'가 붙어나와서 괄호 기호들을 다 지워버림
        if '--' in input_:
            input_ = input_.replace('--', '+') #마이너스 두개는 플러스
        if '++' in input_:
            input_ = input_.replace('++', '') #중복되는 플러스들 다 삭제함
        return input_

    def GetOperator(n):
        order = []
        for t, i in enumerate(n): #반복문을 통해 수식에있는 연산자를 순서대로 order 리스트에 넣어줌
            if '+' in i:
                if (t == 0 or n[t - 1] =='+' or
                n[t - 1] == '*' or n[t - 1] == '/') :
                    pass
                else:
                    order.append('+')
            elif '-' in i:
                if (t == 0 or n[t - 1] =='+' or
                n[t - 1] == '*' or n[t - 1] == '/') :
                    pass
                else:
                    order.append('-')
            elif '*' in i:
                order.append('*')
            elif '/' in i:
                order.append('/')
        
        return order

    def GetNumber(input_):
        for i in range(len(input_)):
            if input_[i] == '+': #숫자를 구분하기위해, 연산자를 모두 ';'로 바꿔버림
                x = input_[:i]
                y = input_[i+1:]
                input_ = x + ';'+ y
            elif ((input_[i] == '-' and i != 0) and 
            (input_[i] == '-' and input_[i - 1] != ';')):
                x = input_[:i]
                y = input_[i+1:]
                input_ = x + ';'+ y
            elif input_[i] == '*':
                x = input_[:i]
                y = input_[i+1:]
                input_ = x + ';'+ y
            elif input_[i] == '/':
                x = input_[:i]
                y = input_[i+1:]
                input_ = x + ';'+ y
                
        temp = input_.split(';') #숫자들을 temp리스트에 모아넣음(문자열)

        if '' in temp:
            temp.remove('')
        
        numbers = []
        for i in temp:
            numbers.append(float(i)) #수식에 있는 숫자들을 순서대로 numbers 리스트에 넣어줌(부동소수점으로 변환)

        return numbers

    def ComputeEngine(numbers, order):
        if len(numbers) == 1:
            order = []
        while(1): #총 연산자 갯수만큼 연산을 하면 됨
            if order == []:
                result = str(round(numbers[0], 10))
                break  
            for j in range(len(order)): #일단 반복문으로 해결 ^^ 이렇게 찾을때마다 break시키고 다중반복하면 인덱스 변해도 곱셈 범위 유지가능
                for t, i in enumerate(order): #연산이 길어지면 이런게 더필요함.... 나중에생각해보자.
                    if '*' in i:
                        numbers[t] = numbers[t] * numbers[t + 1] #계산에 필요한 숫자의 인덱스와 해당 숫자로 계산하기위해 필요한 연산자의 인덱스는 일치함
                        numbers.pop(t+1) #remove로하면 겹치는 원소가 존재하면 해당원소 지우질 못함 ex) 2+3*6*2/2 (2가 여러개있는데 인덱스를 잡아줘도 값이 같으면 앞에꺼를 삭제해버림, 따라서 pop을써야)
                        order.remove('*') #연산자는 어차피 순서대로 계산이라 상관없음, 사용한 연산자는 리스트에서 삭제
                        break
            #-8*-9*-100*0.32-100
            
            flag = 0 #0으로 나누는 경우 반복을 빠져나갈 깃발
            for j in range(len(order)):
                for i in range(len(order)):
                    if order[i] == '/':
                        if numbers[i + 1] == 0: 
                            print('/////////////0으로 나눌수는 없음/////////////')
                            flag = 1
                            break   
                        numbers[i] = numbers[i] / numbers[i + 1]
                        numbers.pop(i+1)
                        order.remove('/')
                        break
                if flag: break    
            if flag: break  

            for i in range(len(order)):
                if order[i] == '+':
                    numbers[i] = numbers[i] + numbers[i + 1]
                    numbers.pop(i+1)
                    order.remove('+')
                    break
            for i in range(len(order)):
                if order[i] == '-':
                    numbers[i] = numbers[i] - numbers[i + 1]
                    numbers.pop(i+1) 
                    order.remove('-') 
                    break
            result = str(round(numbers[0], 10))        
                    
        return result #임시방편. 소수점 자르기

    
while(1):
    a = Calculator()
    print('나눗셈후 곱셈은 분수로 판단됩니다.')
    n = input('필요한 연산을 띄어쓰기 없이 입력해주세요: ')
    result = float(a.RecurCalculator(n))
    print(result)
#testset
'''
(43+33*(34))/(34-3)
321*((4-2)/(10)+333)
(3+2)*(3+3)'''