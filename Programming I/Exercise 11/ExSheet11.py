# This program will determine an employee's salary, it will do so by asking the employee how many hours he/she works in a week and calculating it.

#hours = int(input("Hours worked?: "))
#overtimeWorked = int(input("Overtime Worked?:"))
hours_in_week = 40 
basicRate = 12
overtimeHour = 20
#basic_pay = basicRate * hours_in_week
#overtimePay = (hours - hours_in_week) * overtimeHour
#total = basic_pay + overtimePay

def calcPay(hours, overtimeWorked):
    BasicPay=hours * basicRate
    OvertimePay=overtimeWorked * overtimeHour
    TotalPay=BasicPay+OvertimePay
    return TotalPay

Pay=calcPay(40, 10)
print(Pay)



raceMinutes=42.42
raceSeconds=42%raceMinutes
raceMinutes_into_seconds=int(raceMinutes)*60
int_raceSeconds=int(raceSeconds)
#print(int_raceSeconds)
#print(raceMinutes_into_seconds)
Seconds_in_Race=int_raceSeconds+raceMinutes_into_seconds
RealraceMinutes=Seconds_in_Race/60
#print("Total Seconds Run:",Seconds_in_Race)
race_in_km=10
km_in_Miles=1.61
race_in_Miles=race_in_km/km_in_Miles
#print("Miles:", race_in_Miles)
average=RealraceMinutes/race_in_Miles
seconds=average%6
average_seconds=seconds*60
#print(average_seconds)
averageminutes=int(average)
#print("my average time per mile was:", averageminutes, "m", round(average_seconds, 2),"s")
speed=race_in_Miles/(RealraceMinutes/60)
#print("speed (mph)", round(speed,2))

def postRaceAnalysis(minutes_ran, seconds_ran, race_in_Miles):
    raceMinutes=minutes_ran*60
    totalraceSeconds=raceMinutes+seconds_ran
    totalraceMinutes=totalraceSeconds/60
    average=totalraceMinutes/race_in_Miles
    seconds=average%6
    average_seconds=seconds*60
    round(average_seconds, 2)
    average_minutes=int(average)
    speed=race_in_Miles/(totalraceMinutes/60)
    print("Total Seconds:", totalraceSeconds)
    print("Miles:", race_in_Miles)
    print("My average time per mile was:", average_minutes, "m", round(average_seconds, 2),"s")
    print("speed (mph):", round(speed, 2))
    return average_minutes, average_seconds, speed

postraceanalysis=postRaceAnalysis(42, 42, race_in_Miles)
    

