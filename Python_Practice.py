print("Hello World")

counties = ["Arapahoe", "Denver", "Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("what is the temperature outside?"))
if temperature > 80:
    print("Turn on the AC")
else:
    print("Open the windows.")


score = int(input("What is your test score?"))

if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

x = 0
while x <= 5:
    print(x)
    x = x + 1

for county in counties:
    print(county)


for i in range(len(counties)):
    print(i)  


import datetime
now = datetime.datetime.now()
print("The time right now is ", now)
