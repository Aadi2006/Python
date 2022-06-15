from tkinter import *
import pandas

df1 = pandas.read_csv('time.csv')

window = Tk()

def calc():
    dayToday = dayToday_string.get()
    periodToday = int(periodToday_string.get())
    print(periodToday)
    dat = list(df1[dayToday])
    period = dat[periodToday-1]
    answer.insert(END, period)

print(df1)
what_day_today_label = Label(window, text="What day is it today?")
what_day_today_label.grid(row=0,column=0)

dayToday_string = StringVar()
what_day_today_q = Entry(window, textvariable=dayToday_string)
what_day_today_q.grid(row=0, column=1)

what_period_today = Label(window, text="What period do you have?")
what_period_today.grid(row=1,column=0)

periodToday_string = StringVar()
what_day_today_q = Entry(window, textvariable=periodToday_string)
what_day_today_q.grid(row=1, column=1)

calculate = Button(window, text="Calculate period", command=calc)
calculate.grid(row=2, column=0)

answer = Text(window, height=1, width=20)
answer.grid(row=3, column=0)





window.mainloop()