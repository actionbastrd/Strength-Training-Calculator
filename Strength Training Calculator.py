# Your Code Here
"""A script that determines number of sets, reps, and weight for workout to hit one rep max. Takes a target of some
positive number greater than starting weight. Calculations designed with expectation that 30 * max = volume needed
to achieve one rep max. Uses 4 X 12 as a base"""

# initialize: this should probably be its own function
# def Start()
def workout():
    """Returns a dictionary with integers as keys. Value is a list with element 0 = reps, element 1 = weight.
    Restrictions: Higher weight should always precede lighter weight"""
    wk = {}
    xtra = .75  # later used to append extra set, I feel this should be modified to be less arbitrary
    start_reps = 5
    sets = 4
    i = 0
    for _set in range(sets):
        wk[i] = [start_reps, current_weight]
        if wk[i][0] < rep_limit:
            wk[i][0] += 3
        elif (i + 1) == sets and wk[i][0] > rep_limit:
            wk[i][0] = rep_limit
            sets = sets + 1
            if len(wk) > set_limit:
                wk[i][1] = current_weight + add_weight
                sets = start_sets
        i += 1
    return wk




exercise = "squat" #input("Workout: ").lower()  #ideally a drop down menu selection(would be cool to include autocomplete)
current_max = 275 #int(input("Current max: "))
target_max = 600 #int(input("Target max: "))
target_volume = target_max * 30
start_weight = int(current_max * .75)  # weight/rep
total_reps_current_strength = target_volume / start_weight
days_aweek = 3
start_sets = 4
rep_limit = 12
add_weight = 5
set_limit = 8
difficulty = 'medium'

if difficulty == 'medium':
    modifier = 1
elif difficulty == 'hard':
    modifier = 2

print(total_reps_current_strength)




week = 0
current_weight = start_weight
# def UserInterface()
flag = True
while flag:
    print("Week", week + 1) # week + 1 used for readability and avoid errors due to count offset
    volume_week = 0
    for day in range(days_aweek):
        print(day + 1) # day + 1 used for readability and avoid errors due to count offset
        wkout = workout()
            print("Sets check", sets)
            volume_week += _set * current_weight

        if day + 1 == days_aweek:  # +1 to account for count at 1 vs count at 0 offset
            print("Volume for Week:", volume_week, "\nAverage Daily Volume", volume_week/days_aweek)

    if (volume_week/days_aweek) >= target_volume:
        flag = False
        print("Target Volume", target_volume)
    week += 1

