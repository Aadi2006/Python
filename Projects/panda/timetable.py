import pandas

df1 = pandas.read_csv('time.csv')

dayToday = input("What day is today?")
periodToday = int(input("What period is going on?"))
dat = list(df1[dayToday])
period = dat[periodToday-1]
print(period)