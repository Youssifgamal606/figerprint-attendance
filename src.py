import pandas as pd
import math
from datetime import datetime

out = []
duration = []

data = pd.read_csv("InOutData.csv")
sorted = data.sort_values("Time", na_position='last')
csv = sorted.copy()
sorted = sorted.dropna()

for employee in sorted["Time"]:
    out.append([employee.split()[0], employee.split()[-1]])

csv.drop("Time", inplace=True, axis=1)
for field in range(0, len(csv) - len(out)):
    out.append([])
csv.insert(1, "Attendance", out, True)

for time in out:
    if len(time) == 0:
        duration.append(0)
        continue
    duration.append(str(datetime.strptime(
        time[1], "%H:%M") - datetime.strptime(time[0], "%H:%M"))[0:-3])

csv.insert(2, "Duration", duration, True)
csv.to_csv(str(input("Input Date: ")) + '.csv', index=False)
