import time
import pandas as pd
from datetime import datetime
from csv import writer
import sys

def realized_h():
    # Does the CSV file exist??
    file_csv = input("Create a new CSV file? 1 - Yes, 0 - No: ")
    if file_csv == '1':
        columns = ['DATE','Project name', 'Time', 'Unit']
        df = pd.DataFrame(columns = columns)  
        df.to_csv('Realized_hours.csv', index=False)
    elif file_csv == '0':
        pass
    else:
        sys.exit()

    shortDate = datetime.today().strftime('%Y-%m-%d')
    project_name = input("ENTER project name: ")


    while True:

        input("Press ENTER to continue and ENTER again to exit the TIMER")
        start_time=time.time()
        print("Timer is running")

        data = [shortDate,project_name]

        if input() == '':
            print("Timer has stopped")
            end_time=time.time()

            time_sec = round(end_time-start_time,2)
            time_mins = round(time_sec/60,2)
            time_hours = round(time_sec/3600,2)

            if time_sec <= 60:
                print("The time elapsed:",time_sec,'secs')
                data.append(time_sec)
                data.append('sec(s)')
            elif 60 < time_sec < 3600:
                print("The time elapsed:",time_mins,'mins')
                data.append(time_mins)
                data.append('min(s)')
            elif time_sec > 3600:
                print("The time elapsed:",time_hours,'hours')
                data.append(time_hours)
                data.append('hour(s)')
        #print(df)
        break

    #print(data)
    df1 = pd.DataFrame(columns=['DATE','Project name', 'Time', 'Unit']) 
    #writer = pd.ExcelWriter('Realized_hours.xlsx')
    df1_length = len(df1)
    df1.loc[df1_length] = data
    print(df1)
    #df.to_excel("Realized_hours.xlsx")
    df1.to_csv('Realized_hours.csv', mode='a', index=False, header=None)
    print('\n DONE. Type 2 to restart. Press ENTER to exit.')

realized_h()

while input() == '2':
    realized_h()
else:
    sys.exit()
    
# Below for later maybe
#if input() == 'X'.casefold():
        #sys.exit()