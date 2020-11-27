#Exercise 1: Rewrite your pay computation to give the employee 1.5
#times the hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

print("Enter hours and rate Below")

try:
    hours = float(input())
    rate = float(input())
    global pay
    pay = 0

    if(hours > 40):
        pay = ((40 * 10) + (hours - 40) * (10 * 1.5))
    else:
        pay = hours * 10
    print(pay)

except:
    print("Please Enter a number")
