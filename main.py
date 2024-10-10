import numpy as np
import matplotlib.pyplot as plt

def study_tracker():
    study_hours = {
        "CS": {day: 0 for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]}, 
        "Econ": {day: 0 for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]}, 
        "Math": {day: 0 for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]}, 
        "Physics": {day: 0 for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa","Su"]} 
    }

    keep_going = True 
    while keep_going:
        user_input = input("Input, Display, or Exit? ")
        if user_input == "Exit": 
            keep_going = False
        elif user_input == "Input":
            input_the_day_of_the_week = input("What day is it today? ")
            if input_the_day_of_the_week[:2] in ["Mo", "Tu", "We", "Th", "Fr","Sa","Su"]:
                name_of_curriculum = input("Enter CS, Econ, Math, or Physics: ")
                if name_of_curriculum in study_hours:
                    input_study_hours = int(input("Please enter the study hours: "))
                    study_hours[name_of_curriculum][input_the_day_of_the_week[:2]] += input_study_hours
                else:
                    print("Invalid curriculum. Please enter a valid curriculum.")
            else:
                print("Invalid day. Please enter a valid day.")
        
        elif user_input == "Display":
            new_graph = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            CS = np.array([study_hours["CS"][day] for day in ["Mo", "Tu", "We", "Th","Fr", "Sa", "Su"]])
            Econ = np.array([study_hours["Econ"][day] for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]])
            Math = np.array([study_hours["Math"][day] for day in ["Mo", "Tu","We", "Th", "Fr", "Sa", "Su"]])
            Physics = np.array([study_hours["Physics"][day] for day in ["Mo", "Tu", "We", "Th", "Fr", "Sa", "Su"]])

            fig = plt.figure(figsize=(8, 5))
            plt.bar(new_graph, CS, color='b', width=0.4)
            plt.bar(new_graph, Econ, bottom=CS, color='g', width=0.4)
            plt.bar(new_graph, Math, bottom=CS + Econ, color='r', width=0.4)
            plt.bar(new_graph, Physics, bottom=CS + Econ + Math,color='purple', width=0.4)
            plt.xlabel("The day of the week")
            plt.ylabel("Study Hours")
            plt.title("Study Tracker")
            plt.legend(["CS", "Econ", "Math", "Physics"])
            plt.show()

study_tracker()