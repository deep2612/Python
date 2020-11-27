def bubble_sort(demo_data):
   
   for i in range(len(demo_data)):
       
       for j in range(0,len(demo_data) - i - 1):

           if(demo_data[j] > demo_data[j + 1]):

               (demo_data[j], demo_data[j + 1]) = (demo_data[j+1], demo_data[j])


data = input().split()
bubble_sort(data)

print(data)