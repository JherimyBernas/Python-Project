from tkinter import *
from functools import partial

# Cash Register Application
print("\n***** PROGRAMMED BY *****")
print("*** JHERIMY S. BERNAS ***")

final1 = Tk()
final1.title("Cash Register")
final1.geometry("275x320")


expression = ""
main_str = StringVar()
subtotal_str = StringVar()
tax_str = StringVar()
total_str = StringVar()

dollar_sign = Label(final1, text="$").place(x=30, y=20)
main_box = Label(final1, width=30, textvariable=main_str, borderwidth=3, relief="sunken", anchor="w").place(x=40, y=20)

button1 = Button(final1, text="1", width=3, borderwidth=3).place(x=50, y=50)
button2 = Button(final1, text="2", width=3, borderwidth=3).place(x=83, y=50)
button3 = Button(final1, text="3", width=3, borderwidth=3).place(x=116, y=50)
button4 = Button(final1, text="4", width=3, borderwidth=3).place(x=50, y=78)
button5 = Button(final1, text="5", width=3, borderwidth=3).place(x=83, y=78)
button6 = Button(final1, text="6", width=3, borderwidth=3).place(x=116, y=78)
button7 = Button(final1, text="7", width=3, borderwidth=3).place(x=50, y=106)
button8 = Button(final1, text="8", width=3, borderwidth=3).place(x=83, y=106)
button9 = Button(final1, text="9", width=3, borderwidth=3).place(x=116, y=106)
button0 = Button(final1, text="0", width=3, borderwidth=3).place(x=83, y=134)
button_dot = Button(final1, text=".", width=3, borderwidth=3).place(x=116, y=134)

button_enter = Button(final1, text="Enter", width=7, borderwidth=3).place(x=170, y=50)
button_total = Button(final1, text="Total", width=7, borderwidth=3).place(x=170, y=78)
button_delete = Button(final1, text="Delete", width=7, borderwidth=3).place(x=170, y=106)
button_clear = Button(final1, text="Clear", width=7, borderwidth=3).place(x=170, y=134)

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


