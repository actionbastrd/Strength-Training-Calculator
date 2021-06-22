# Your Code Here
"""A script that determines number of sets, reps, and weight for workout to hit one rep max. Takes a target of some
positive number greater than starting weight. Calculations designed with expectation that 30 * max = volume needed
to achieve one rep max. Uses 4 X 12 as a base"""

# initialize: this should probably be its own function
# def Start()
workout = "squat" #input("Workout: ").lower()  #ideally a drop down menu selection(would be cool to include autocomplete)
current_max = 275 #int(input("Current max: "))
target_max = 600 #int(input("Target max: "))
target_volume = target_max * 30
start_weight = int(current_max * .75)  # weight/rep
total_reps_current_strength = target_volume / start_weight
days_aweek = 3
limit = 12

difficulty = 'medium'

if difficulty == 'medium':
    modifier = 1
elif difficulty == 'hard':
    modifier = 2

print(total_reps_current_strength)


xtra = .75   # later used to append extra set, I feel this should be modified to be less arbitrary
start_reps = 5
sets = [start_reps] * 4

week = 0
current_weight = start_weight
# def UserInterface()
flag = True
while flag:
    print("Week", week + 1) # week + 1 used for readability and avoid errors due to count offset
    volume_week = 0
    for day in range(days_aweek):
        print(day + 1) # day + 1 used for readability and avoid errors due to count offset
        i = 0
        if week > 0:
            if start_reps < limit:
                start_reps += 2 * modifier     #  might use a for loop here to pyramid each set down as a % of first set in series
                sets = [start_reps] * 4
            elif len(sets) < 7:
                sets.append(int(start_reps * xtra))
                if len(sets) > 6:
                    start_reps = 5 #  reset
                    current_weight += 5 * modifier
                    sets = [start_reps] * 4


        for _set in sets:
            i += 1 # could avoid use of counter if using len(sets) and notation sets[_set](+ 1 to start count from 1)
            day_volume = 0



    #        elif _set < limit:  #  if a set is less than the limit add 3 more according to week
   #             start_reps += 3 * week
     #           sets = [start_reps] * 4



            print("Set:", i,  workout, "weight", current_weight,  "reps", _set)
            print("Sets check", sets)
            volume_week += _set * current_weight

        if day + 1 == days_aweek:  # +1 to account for count at 1 vs count at 0 offset
            print("Volume for Week:", volume_week, "\nAverage Daily Volume", volume_week/days_aweek)

    if (volume_week/days_aweek) >= target_volume:
        flag = False
        print("Target Volume", target_volume)
    week += 1

