import statistics
# Mohamed Bagayoko
# October 14 2019
# Hartwick Barkey (Cookies and Candy)

# Cookie and Candy list holders
cookies = []
candy = []


# User inputs cookie values
def cookie_input():
    print("Please print how many cookies you need per month-")
    for i in range(0, 6):
        value = int(input("Cookie input:"))
        cookies.append(value)
    print(f"Your list is {cookies} per month")

# Average
def cookie_avg():
    average = statistics.mean(cookies)
    print(f"Your average is {average} cookies per month.")
    return average

# Maximum
def cookie_max():
    c = max(cookies)
    print(f"Your month's maximum cookies is {c}.")

# Minimum
def cookie_min():
    e = min(cookies)
    print(f"Your month's minimum cookies is {e}.")


cookie_input()
cook_avg = cookie_avg()
cookie_max()
cookie_min()


# User inputs candy values
def candy_input():
    print("Please print how much candy you want per month-")
    for i in range(0, 6):
        bvalue = int(input("Candy input:"))
        candy.append(bvalue)
    print(f"Your list is {candy} per month")

# Average
def candy_avg():
    b = statistics.mean(candy)
    print(f"Your average is {b} candy per month.")
    return b

# Maximum
def candy_max():
    d = max(candy)
    print(f"Your month's maximum candy is {d}.")


# Minimum
def candy_min():
    f = min(candy)
    print(f"Your month's minimum candy is {f}")


candy_input()
can_avg = candy_avg()
candy_max()
candy_min()

# Which bake good is best by average
if cook_avg > can_avg:
    print("Cookies are more popular!")
elif cook_avg < can_avg:
    print("Candy is more popular!")
else:
    print("Both cookie and candy are popular!")




