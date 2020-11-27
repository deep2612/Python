inventory = {}

print("------------Welcome to your store Inventory----------")

while(True):
    print("Enter 1 for adding new items into inventory \nEnter 2 to Display Product and stock\nEnter 0 number to exit")
    choice = int(input())
    if(choice == 1):   
        while(True):

            print("Enter Product Name :")
            key = input()

            print("Enter Product Details/Stock : ")
            value = input().split()

            inventory[key] = value

            print("If you want to enter another key and value press Y....")
            user_choice = input()

            if(user_choice != 'Y'):
                break

    elif(choice == 2):
        if(bool(inventory)):

            for product,details in inventory.items():
                print(product ," : ", details)
        else:
            print("Your Inventory is Empty... Please upload something in your inventory")

    elif(choice == 0):
        break
    
    else:
        print("Please Enter a correct choice")


