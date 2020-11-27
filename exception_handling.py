while True:
    try:
        number = int(input("Please enter a number :"))
        break
    except ValueError:
        print("You have not entered a number")
    except:
        print("Unexpected")

print("Thank you")
