def open_account():
    print('새로운 계좌가 개설되었습니다.')

def deposit(balance, money): #잔액과 금액 입력
    print('입금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance+money))  
    return balance+money #balance에 합결과 리턴

def withdraw(balance, money):
    if (balance < money):
        print('잔액이 부족합니다. 잔액은 {0} 원입니다.'.format(balance))
        return balance
    else:
        print('출금이 완료되었습니다. 잔액은 {0} 원입니다.'.format(balance-money))
        return balance-money

def withdraw_night(balance, money):
    commission = 100
    if (balance < money+commission):
        print('잔액이 부족합니다. 잔액은 {0} 원입니다.'.format(balance))
        return balance
    else:
        print('출금이 완료되었습니다. 수수료는 {0}원이며, 잔액은 {1} 원입니다.'.format(commission, balance-money-commission))
        return balance-money-commission

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance,500)
balance = withdraw_night(balance, 100)
print(balance)
