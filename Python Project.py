from tkinter import *
from functools import partial

# Cash Register Application
print("\n***** PROGRAMMED BY *****")
print("*** JHERIMY S. BERNAS ***")

final1 = Tk()
final1.title("Cash Register")
final1.geometry("275x320")


def btn_click(number):
    global expression
    expression += str(number)
    main_str.set(expression)


def btn_enter():
    try:
        new_subtotal = float(expression)
    except ValueError:
        subtotal_str.set("$0.00")
        tax_str.set("$0.00")
    else:
        subtotal_str.set("${:,.2f}".format(new_subtotal))
        tax_str.set("$0.00")

        # Amounts under $100 = 5% (.05) sales tax
        if float(new_subtotal) < 100:
            tax1 = float(new_subtotal) * 0.05
            tax_str.set("${:,.2f}".format(float(tax1)))

        # Amounts between $100 and $499 = 7.5% (.075) sales tax
        elif 99 < float(new_subtotal) < 500:
            tax1 = float(new_subtotal) * 0.075
            tax_str.set("${:,.2f}".format(float(tax1)))

        # Amounts above $499 = 10% (.10) sales tax
        elif float(new_subtotal) > 499:
            tax1 = float(new_subtotal) * 0.10
            tax_str.set("${:,.2f}".format(float(tax1)))


def btn_total(one, two, three):
    two2 = (two.get())
    three3 = (three.get())
    new_total = float(two2.replace("$", "").replace(",", "")) + float(three3.replace("$", "").replace(",", ""))
    one.set("${:,.2f}".format(new_total))


def btn_delete():
    global expression
    expression = expression[:-1]
    main_str.set(expression)


def btn_clear():
    global expression
    expression = ""
    main_str.set("")
    subtotal_str.set("")
    tax_str.set("")
    total_str.set("")


expression = ""
main_str = StringVar()
subtotal_str = StringVar()
tax_str = StringVar()
total_str = StringVar()

dollar_sign = Label(final1, text="$").place(x=30, y=20)
main_box = Label(final1, width=30, textvariable=main_str, borderwidth=3, relief="sunken", anchor="w").place(x=40, y=20)

button1 = Button(final1, text="1", width=3, borderwidth=3, command=lambda: btn_click(1)).place(x=50, y=50)
button2 = Button(final1, text="2", width=3, borderwidth=3, command=lambda: btn_click(2)).place(x=83, y=50)
button3 = Button(final1, text="3", width=3, borderwidth=3, command=lambda: btn_click(3)).place(x=116, y=50)
button4 = Button(final1, text="4", width=3, borderwidth=3, command=lambda: btn_click(4)).place(x=50, y=78)
button5 = Button(final1, text="5", width=3, borderwidth=3, command=lambda: btn_click(5)).place(x=83, y=78)
button6 = Button(final1, text="6", width=3, borderwidth=3, command=lambda: btn_click(6)).place(x=116, y=78)
button7 = Button(final1, text="7", width=3, borderwidth=3, command=lambda: btn_click(7)).place(x=50, y=106)
button8 = Button(final1, text="8", width=3, borderwidth=3, command=lambda: btn_click(8)).place(x=83, y=106)
button9 = Button(final1, text="9", width=3, borderwidth=3, command=lambda: btn_click(9)).place(x=116, y=106)
button0 = Button(final1, text="0", width=3, borderwidth=3, command=lambda: btn_click(0)).place(x=83, y=134)
button_dot = Button(final1, text=".", width=3, borderwidth=3, command=lambda: btn_click(".")).place(x=116, y=134)

total_btn = partial(btn_total, total_str, subtotal_str, tax_str)

button_enter = Button(final1, text="Enter", width=7, borderwidth=3, command=btn_enter).place(x=170, y=50)
button_total = Button(final1, text="Total", width=7, borderwidth=3, command=total_btn).place(x=170, y=78)
button_delete = Button(final1, text="Delete", width=7, borderwidth=3, command=btn_delete).place(x=170, y=106)
button_clear = Button(final1, text="Clear", width=7, borderwidth=3, command=btn_clear).place(x=170, y=134)

subtotal_label = Label(final1, text="Subtotal:", anchor="w").place(x=30, y=185)
tax_label = Label(final1, text="Tax:", anchor="w").place(x=30, y=225)
total_label = Label(final1, text="Total:", anchor="w").place(x=30, y=265)

subtotal = Label(final1, textvariable=subtotal_str, width=18, borderwidth=2, relief="sunken", anchor="e")\
    .place(x=123, y=185)
tax = Label(final1, textvariable=tax_str, width=18, borderwidth=2, relief="sunken", anchor="e")\
    .place(x=123, y=225)
total = Label(final1, textvariable=total_str, width=18, borderwidth=2, relief="sunken", anchor="e")\
    .place(x=123, y=265)

final1.mainloop()