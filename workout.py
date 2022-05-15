def workout_one():
    """Take max rep and print 3 sets of 5 with weight percentages"""


week_one = [0.65, 0.75, 0.85]
while True:
    print("enter 'quit' to quit the program")
    rep_max = input("what is your one rep max?")

    try:
        rep_max = int(rep_max)
    except:
        print("Try entering a whole number")
        continue

    if rep_max == 'quit':
        break
    break
for percentage in week_one:
    reps = int(rep_max * percentage)
    print("5 reps of " + str(reps))
working_set = int(week_one[0]*rep_max)
working_set = str(working_set)
print ("5 sets of 5 reps @ " + working_set)