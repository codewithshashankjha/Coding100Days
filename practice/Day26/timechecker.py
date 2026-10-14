import time
timestamp=time.strftime('%H:%M:%S')


# hours=int(time.strftime('%H'))
hours=int(input("Enter the time "))



# print("Hello Sir/ma'am")
# input()

# print("CurrentTime ",timestamp)
# print(hours)

if(hours>6 and hours<12):
    print("Good Morning")
elif(hours>=12 and hours<18):
    print("Good Evening")
else:
    print("Good Night")
