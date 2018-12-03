import pickle, os, time


def check_bill(wallet, bill):
    print(
        '%-12s%-12s%-12s%-12s%-20s' % ('Time', 'Income', 'Expenses', 'Balance', 'Comment')
    )
    with open(bill, 'r') as bobj:
        blist = bobj.readlines()
        for line in blist:
            print(line,end='')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj)
    print('\033[31;1mLatest Balance:%d\033[0m' % balance)


def income(wallet, bill):  # 收入
    try:
        income = int(input('Income:'))
    except ValueError:
        print('\033[31;1mInvalid input. Try again.\033[0m')
    comment = input('comment:')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) + income
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)
    with open(bill, 'a') as fobj:
        fobj.write(
            '%-12s%-12s%-12s%-12s%-20s\n' % (date,income,'',balance, comment)
        )


def expenses(wallet, bill):  # 支出

    try:
        expenses = int(input('Expenses:'))
    except (ValueError,KeyboardInterrupt,EOFError):
        exit()
    comment = input('comment:')
    date = time.strftime('%Y-%m-%d')
    with open(wallet, 'rb') as fobj:
        balance = pickle.load(fobj) - expenses
    with open(wallet, 'wb') as fobj:
        pickle.dump(balance, fobj)
    with open(bill, 'a') as fobj:
        fobj.write(
            '%-12s%-12s%-12s%-12s%-20s\n' % (date,'',expenses,balance,comment)
        )


def show_menu():
    cmds = {'0': check_bill, '1': income, '2': expenses, '3': exit}
    prompt = '''(0) check bill
(1) income
(2) expenses
(3) exit
Please chioce[0/1/2/3]:'''
    wallet = 'wallet.txt'
    bill = 'bill.txt'

    if not os.path.isfile(wallet):
        with open(wallet, 'wb') as wobj:
            pickle.dump(10000, wobj)

    if not os.path.isfile(bill):
        os.mknod(bill)

    while True:
        try:
            chioce = input(prompt).strip()[0]
        except (EOFError, KeyboardInterrupt):
            print('\033[34;1m\nBye\033[0m')
            break
        if chioce not in '0123':
            print('Invalid input. Try again.')
            continue
        if chioce == '3':
            print('Bye')
            break
        cmds[chioce](wallet, bill)


if __name__ == '__main__':
    show_menu()
