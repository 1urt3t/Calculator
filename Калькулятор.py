#Параметры окна
from tkinter import *
window = Tk()
window.resizable(False, False)
window.geometry('400x500')
window.title('Калькулятор')

#Задаем переменные
first_number = ''
second_number = ''
option = []

#Главный экран с числами
main_label = Label(text='0', font='Arial, 50', fg='black', anchor=E)
main_label.place(x=100, y=0, width=300, height=100)



#Делаем так чтобы действие было бесконечное
for i in range(1, ):
    #Знаки
    def option_plus():
        global option
        global second_number
        option = '+'
        main_label = Label(text=option, font='Arial, 50', fg='black', anchor=E)
        main_label.place(x=100, y=0, width=300, height=100)
        second_number = ''
        second_main()


    plus_button = Button(text='+', font='Arial, 40', fg='black', command=option_plus)
    plus_button.place(x=300, y=100, width=100, height=80)

    def option_umno():
        global option
        global second_number
        option = '*'
        main_label = Label(text=option, font='Arial, 60', fg='black', anchor=E)
        main_label.place(x=100, y=0, width=300, height=100)
        second_number = ''
        second_main()


    umno_button = Button(text='*', font='Arial, 60', fg='black', anchor=N, command=option_umno)
    umno_button.place(x=300, y=260, width=100, height=80)

    def option_lit():
        global option
        global second_number
        option = '/'
        main_label = Label(text=option, font=('Arial, 50'), fg='black', anchor=E)
        main_label.place(x=100, y=0, width=300, height=100)
        second_number = ''
        second_main()


    lit_button = Button(text='/', font='Arial, 50', fg='black', command=option_lit)
    lit_button.place(x=300, y=340, width=100, height=80, )




#-

    def option_minus():
        global option
        global second_number
        option = '-'
        main_label = Label(text=option, font=('Arial, 50'), fg='black', anchor=E)
        main_label.place(x=100, y=0, width=300, height=100)
        second_number = ''
        second_main()
    minus_button = Button(text='-', font='Arial, 70', fg='black', command=option_minus)
    minus_button.place(x=300, y=180, width=100, height=80)

    #Тире

    def tire_function():
        global first_number
        global option
        global second_number
        if second_number != '':
            if option == '+':
                first_number = (int(first_number) + (int(second_number)))
            elif option == '-':
                first_number = (int(first_number) - (int(second_number)))
            elif option == '*':
                first_number = (int(first_number) * (int(second_number)))
            elif option == '/':
                first_number = (int(first_number) // (int(second_number)))



            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
            first_main()

    tire_button = Button(text='=', font=('Arial, 40'), fg='black', command=tire_function)
    tire_button.place(x=300, y=420, width=100, height=80)






    #Первые цифры

    def first_main():
        global first_number
        global option
        global second_number
        #AC-Очищаем first_number
        def ac_button_function():
            global first_number
            global option
            global second_number
            first_number = ''
            second_number = ''
            option = []

            main_label = Label(text='0', font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        ac_button = Button(text='AC', font=('Arial, 40'), fg='black', command=ac_button_function)
        ac_button.place(x=0, y=0, width=100, height=100)

    # ЧИСЛА

    # Число 1
        def one_button_function():
            global first_number
            first_number += '1'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        one_number_button = Button(text='1', font=('Arial, 40'), fg='black', command=one_button_function)
        one_number_button.place(x=0, y=100, width=100, height=100)

    # Число 2

        def two_button_function():
            global first_number
            first_number += '2'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        two_number_button = Button(text='2', font=('Arial, 40'), fg='black', command=two_button_function)
        two_number_button.place(x=100, y=100, width=100, height=100)

    # Число 3

        def three_button_function():
            global first_number
            first_number += '3'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        three_number_button = Button(text='3', font=('Arial, 40'), fg='black', command=three_button_function)
        three_number_button.place(x=200, y=100, width=100, height=100)

    # Число 4

        def four_button_function():
            global first_number
            first_number += '4'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        four_number_button = Button(text='4', font=('Arial, 40'), fg='black', command=four_button_function)
        four_number_button.place(x=0, y=200, width=100, height=100)

    # Число 5

        def five_button_function():
            global first_number
            first_number += '5'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        five_number_button = Button(text='5', font=('Arial, 40'), fg='black', command=five_button_function)
        five_number_button.place(x=100, y=200, width=100, height=100)

    # Число 6

        def six_button_function():
            global first_number
            first_number += '6'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        six_number_button = Button(text='6', font=('Arial, 40'), fg='black', command=six_button_function)
        six_number_button.place(x=200, y=200, width=100, height=100)

    # Число 7

        def seven_button_function():
            global first_number
            first_number += '7'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        seven_number_button = Button(text='7', font=('Arial, 40'), fg='black', command=seven_button_function)
        seven_number_button.place(x=0, y=300, width=100, height=100)

        # Число 8

        def eight_button_function():
            global first_number
            first_number += '8'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        eight_number_button = Button(text='8', font=('Arial, 40'), fg='black', command=eight_button_function)
        eight_number_button.place(x=100, y=300, width=100, height=100)

        # Число 9

        def nine_button_function():
            global first_number
            first_number += '9'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        nine_number_button = Button(text='9', font=('Arial, 40'), fg='black', command=nine_button_function)
        nine_number_button.place(x=200, y=300, width=100, height=100)

        # Число 0

        def zero_button_function():
            global first_number
            first_number += '0'
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        zero_number_button = Button(text='0', font=('Arial, 40'), fg='black', command=zero_button_function)
        zero_number_button.place(x=100, y=400, width=100, height=100)













    #Второй ввод

    def second_main():
        global first_number
        global option
        global second_number
        #AC-Очищаем first_number
        def ac_button_function():
            global first_number
            first_number = 0
            main_label = Label(text=first_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        ac_button = Button(text='AC', font=('Arial, 40'), fg='black', command=ac_button_function)
        ac_button.place(x=0, y=0, width=100, height=100)

        # ЧИСЛА

        # Число 1
        def one_button_function():
            global second_number
            second_number += '1'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        one_number_button = Button(text='1', font=('Arial, 40'), fg='black', command=one_button_function)
        one_number_button.place(x=0, y=100, width=100, height=100)

        # Число 2

        def two_button_function():
            global second_number
            second_number += '2'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        two_number_button = Button(text='2', font=('Arial, 40'), fg='black', command=two_button_function)
        two_number_button.place(x=100, y=100, width=100, height=100)

        # Число 3

        def three_button_function():
            global second_number
            second_number += '3'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        three_number_button = Button(text='3', font=('Arial, 40'), fg='black', command=three_button_function)
        three_number_button.place(x=200, y=100, width=100, height=100)

        # Число 4

        def four_button_function():
            global second_number
            second_number += '4'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        four_number_button = Button(text='4', font=('Arial, 40'), fg='black', command=four_button_function)
        four_number_button.place(x=0, y=200, width=100, height=100)

        # Число 5

        def five_button_function():
            global second_number
            second_number += '5'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        five_number_button = Button(text='5', font=('Arial, 40'), fg='black', command=five_button_function)
        five_number_button.place(x=100, y=200, width=100, height=100)

        # Число 6

        def six_button_function():
            global second_number
            second_number += '6'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        six_number_button = Button(text='6', font=('Arial, 40'), fg='black', command=six_button_function)
        six_number_button.place(x=200, y=200, width=100, height=100)

        # Число 7

        def seven_button_function():
            global second_number
            second_number += '7'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        seven_number_button = Button(text='7', font=('Arial, 40'), fg='black', command=seven_button_function)
        seven_number_button.place(x=0, y=300, width=100, height=100)

        # Число 8

        def eight_button_function():
            global second_number
            second_number += '8'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        eight_number_button = Button(text='8', font=('Arial, 40'), fg='black', command=eight_button_function)
        eight_number_button.place(x=100, y=300, width=100, height=100)

        # Число 9

        def nine_button_function():
            global second_number
            second_number += '9'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        nine_number_button = Button(text='9', font=('Arial, 40'), fg='black', command=nine_button_function)
        nine_number_button.place(x=200, y=300, width=100, height=100)

        # Число 0

        def zero_button_function():
            global second_number
            second_number += '0'
            main_label = Label(text=second_number, font=('Arial, 50'), fg='black', anchor=E)
            main_label.place(x=100, y=0, width=300, height=100)
        zero_number_button = Button(text='0', font=('Arial, 40'), fg='black', command=zero_button_function)
        zero_number_button.place(x=100, y=400, width=100, height=100)
    first_main()
    window.mainloop()


#Решил немного заморочиться