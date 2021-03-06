class Calculator:
    def MainofCalculator(self, input_): #계산기, 재귀로 타고 들어오는 함수. 외부에서 쓸땐 매개변수 필요
        #여기서는 매개변수 주지않아도 괜찮
        self.input_ = input_
        bcnt = Calculator.BracketCount(self.input_)
        
        for i in range(bcnt):
            bketix_1st, bketix_2nd = Calculator.BracketIndexAppend(self.input_)
            self.input_ = Calculator.RecurEngine(bketix_1st, bketix_2nd, self.input_)

        modinput_ = Calculator.DeleteMultiOperator(self.input_)
        operator = Calculator.GetOperator(modinput_)
        extractnumber = Calculator.GetNumber(modinput_)
        result = Calculator.ComputeEngine(extractnumber, operator)

        return result

    def BracketCount(input_): #입력의 괄호 수를 세주는 함수
        bketcnt = 0
        for ipt in range(len(input_)):
            if input_[ipt] == '(':
                bketcnt += 1
        return bketcnt

    def BracketIndexAppend(input_): #괄호마다 인덱스를 새겨주는 함수
        #'('의 인덱스를 세다가 ')'를 발견하는 순간 break 
        bketix_1st = []
        bketix_2nd = []
        for ipt in range(len(input_)):
            if input_[ipt] == '(':
                bketix_1st.append(ipt)

            if input_[ipt] == ')':
                bketix_2nd.append(ipt)
                break
        return bketix_1st, bketix_2nd

    def RecurEngine(bketix_1st, bketix_2nd, input_): #괄호를 떼고 메인 함수(MainofCalculator)로 보내주는 함수
        obj = Calculator() #이렇게 호출해줄땐 매개변수를 주어야함!
        #재귀 타고 들어갈 함수가 Calculator 클래스의 self 매개변수? 인자를 가진 
        #MainofCalculator라는 함수라서 이렇게 매개변수를 줘야 
        #변수 한개 필요한데 두개줬다 라는 오류가 안뜸
        #이게 정확히 맞는진 모르겠으나....
        #'('의 인덱스중 최댓값 +1, ')'의 인덱스 사이로 묶어서 괄호없게 만든후 다시 MainofCalculator로 보내서 계산
        if bketix_1st == [] and bketix_2nd == []:
                pass #재귀를 통해 이 단계까지 와야 더 이상 다시 돌아가지않음
        else:
            u = max(bketix_1st)
            v = bketix_2nd[0]
            fir = input_[:u]
            sec = input_[v+1:]
            recur = obj.MainofCalculator(input_[u+1:v])
            input_ = fir + recur + sec
        return input_
   
    def DeleteMultiOperator(input_): #++과 --를 삭제 해주는 함수    
        input_ = input_.replace(')', '').strip() #문자열 입력이라 n을 얻을때 경우에 따라 ')'가 붙어나와서 괄호 기호들을 다 지워버림
        if '--' in input_:
            input_ = input_.replace('--', '+') #마이너스 두개는 플러스
        if '++' in input_:
            input_ = input_.replace('++', '') #중복되는 플러스들 다 삭제함
        modinput_ = input_
        return modinput_

    def GetOperator(modinput_): #연산자를 추출하는 함수
        order = []
        for idx, ipt in enumerate(modinput_): #반복문을 통해 수식에있는 연산자를 순서대로 order 리스트에 넣어줌
            if '+' in ipt:
                if (idx == 0 or modinput_[idx - 1] =='+' or
                modinput_[idx - 1] == '*' or modinput_[idx - 1] == '/') :
                    pass
                else:
                    order.append('+')
            elif '-' in ipt:
                if (idx == 0 or modinput_[idx - 1] =='+' or
                modinput_[idx - 1] == '*' or modinput_[idx - 1] == '/') :
                    pass
                else:
                    order.append('-')
            elif '*' in ipt:
                order.append('*')
            elif '/' in ipt:
                order.append('/')
        
        return order

    def GetNumber(modinput_): #수들을 추출하는 함수
        for idx in range(len(modinput_)):
            if modinput_[idx] == '+': #숫자를 구분하기위해, 연산자를 모두 ';'로 바꿔버림
                fir_mod = modinput_[:idx]
                sec_mod = modinput_[idx+1:]
                modinput_ = fir_mod + ';'+ sec_mod
            elif ((modinput_[idx] == '-' and idx != 0) and 
            (modinput_[idx] == '-' and modinput_[idx - 1] != ';')):
                fir_mod = modinput_[:idx]
                sec_mod = modinput_[idx+1:]
                modinput_ = fir_mod + ';'+ sec_mod
            elif modinput_[idx] == '*':
                fir_mod = modinput_[:idx]
                sec_mod = modinput_[idx+1:]
                modinput_ = fir_mod + ';'+ sec_mod
            elif modinput_[idx] == '/':
                fir_mod = modinput_[:idx]
                sec_mod = modinput_[idx+1:]
                modinput_ = fir_mod + ';'+ sec_mod
                
        temp = modinput_.split(';') #숫자들을 temp리스트에 모아넣음(문자열)
        
        if '' in temp:
            temp.remove('')
        
        numbers = []
        for idx in temp:
            numbers.append(float(idx)) #수식에 있는 숫자들을 순서대로 numbers 리스트에 넣어줌(부동소수점으로 변환)

        return numbers

    def ComputeEngine(numbers, order): #추출한 연산자와 수들을 바탕으로 계산하는 함수
        if len(numbers) == 1:
            order = []
        while(1): #총 연산자 갯수만큼 연산을 하면 됨
            if order == []:
                result = str(round(numbers[0], 10))
                break  
            for extra_repeat_mul in range(len(order)): #일단 반복문으로 해결 ^^ 이렇게 찾을때마다 break시키고 다중반복하면 인덱스 변해도 곱셈 범위 유지가능
                for idx1, orderelement in enumerate(order): #연산이 길어지면 이런게 더필요함.... 나중에생각해보자.
                    if '*' in orderelement:
                        numbers[idx1] = numbers[idx1] * numbers[idx1 + 1] #계산에 필요한 숫자의 인덱스와 해당 숫자로 계산하기위해 필요한 연산자의 인덱스는 일치함
                        numbers.pop(idx1+1) #remove로하면 겹치는 원소가 존재하면 해당원소 지우질 못함 ex) 2+3*6*2/2 (2가 여러개있는데 인덱스를 잡아줘도 값이 같으면 앞에꺼를 삭제해버림, 따라서 pop을써야)
                        order.remove('*') #연산자는 어차피 순서대로 계산이라 상관없음, 사용한 연산자는 리스트에서 삭제
                        break
            #-8*-9*-100*0.32-100
            
            flag = 0 #0으로 나누는 경우 반복을 빠져나갈 깃발
            for extra_repeat_div in range(len(order)):
                for idx2 in range(len(order)):
                    if order[idx2] == '/':
                        if numbers[idx2 + 1] == 0: 
                            print('/////////////0으로 나눌수는 없음/////////////')
                            flag = 1
                            break   
                        numbers[idx2] = numbers[idx2] / numbers[idx2 + 1]
                        numbers.pop(idx2+1)
                        order.remove('/')
                        break
                if flag: break    
            if flag: break  

                
            for idx3 in range(len(order)):
                if order[idx3] == '+':
                    numbers[idx3] = numbers[idx3] + numbers[idx3 + 1]
                    numbers.pop(idx3+1)
                    order.remove('+')
                    break
                
                elif order[idx3] == '-':
                    numbers[idx3] = numbers[idx3] - numbers[idx3 + 1]
                    numbers.pop(idx3+1) 
                    order.remove('-') 
                    break
            result = str(round(numbers[0], 10))        
                    
        return result #임시방편. 소수점 자르기
    
while(1):
    para = Calculator()
    print('나눗셈후 곱셈은 분수로 판단됩니다.')
    inputnumber = input('필요한 연산을 띄어쓰기 없이 입력해주세요: ')
    result = float(para.MainofCalculator(inputnumber))
    print(result)
#testset
'''
(43+33*(34))/(34-3)
321*((4-2)/(10)+333)
(3+2)*(3+3)'''