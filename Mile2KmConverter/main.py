from tkinter import *

# Set screen
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# class for convert mile to Kilometer
def cal_mile2km():
    mile = float(entry_mile.get())
    km = mile * 1.609
    # send result to show
    km_result_label.config(text=f"{km:.2f}")


# entry mile value
entry_mile = Entry(width=7, justify="center")
entry_mile.insert(END, string="0")
entry_mile.grid(column=1, row=0)

# label 1
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

# label 2
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# label 3
km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

# label 4
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# button
cal_button = Button(text="Calculate", command=cal_mile2km)
cal_button.grid(column=1, row=2)

window.mainloop()
