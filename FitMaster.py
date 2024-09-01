import os
import keyboard
import time

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    clearscreen()
    print("\t[FitMaster]")
    print("1. BMR Calculator")
    print("2. TDEE Calculator")
    print("3. Nutrition Calculator")
    print("4. What is BMR & TDEE?")
    print("\nPress ESC to end the program.")
    selection()

def selection():
    while True:
        if keyboard.is_pressed('1'):
            BMR_Calculator()
            break
        elif keyboard.is_pressed('2'):
            TDEE()
            break
        elif keyboard.is_pressed('3'):
            nutrition_calculator()
            break
        elif keyboard.is_pressed('4'):
            information()
            break
        elif keyboard.is_pressed('esc'):
            print("Exiting the program...")
            time.sleep(1)
            print("Done")
            break

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def BMR_Calculator():
    clearscreen()
    print("\t[BMR-Calculator]\n")
    
    weight = get_float_input("Enter Weight (kg): ")
    height = get_float_input("Enter Height (cm): ")
    age = get_int_input("Enter Age: ")
    
    gender = None
    print("Enter Gender:")
    print("1. Male")
    print("2. Female")
    
    while True:
        if keyboard.is_pressed('1'):
            gender = 'm'
            break
        elif keyboard.is_pressed('2'):
            gender = 'f'
            break
        elif keyboard.is_pressed('esc'):
            menu()
            return

    if gender == 'm':
        result = Male(weight, height, age)
    elif gender == 'f':
        result = Female(weight, height, age)

    print(f"Your BMR is: {result:.2f} calories/day")
    input("\nPress Enter to return to the menu...")
    menu()

def Male(W, H, A):
    return 88.362 + (13.397 * W) + (4.799 * H) - (5.677 * A)

def Female(W, H, A):
    return 447.593 + (9.247 * W) + (3.098 * H) - (4.330 * A)

def TDEE():
    clearscreen()
    print("\t[TDEE-Calculator]\n")
    
    weight = get_float_input("Enter Weight (kg): ")
    height = get_float_input("Enter Height (cm): ")
    age = get_int_input("Enter Age: ")
    
    gender = None
    print("Enter Gender:")
    print("1. Male")
    print("2. Female")
    
    while True:
        if keyboard.is_pressed('1'):
            gender = 'm'
            break
        elif keyboard.is_pressed('2'):
            gender = 'f'
            break
        elif keyboard.is_pressed('esc'):
            menu()
            return

    if gender == 'm':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'f':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    print("\nSelect your activity level:")
    print("1. Sedentary (little or no exercise)")
    print("2. Lightly active (light exercise/sports 1-3 days/week)")
    print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
    print("4. Very active (hard exercise/sports 6-7 days a week)")
    print("5. Super active (very hard exercise/sports & physical job)")
    
    activity_level = None
    while True:
        if keyboard.is_pressed('1'):
            activity_level = 1.2
            break
        elif keyboard.is_pressed('2'):
            activity_level = 1.375
            break
        elif keyboard.is_pressed('3'):
            activity_level = 1.55
            break
        elif keyboard.is_pressed('4'):
            activity_level = 1.725
            break
        elif keyboard.is_pressed('5'):
            activity_level = 1.9
            break
        elif keyboard.is_pressed('esc'):
            menu()
            return

    tdee = bmr * activity_level
    print(f"\nYour TDEE is: {tdee:.2f} calories/day")
    input("\nPress Enter to return to the menu...")
    menu()

def nutrition_calculator():
    clearscreen()
    print("\t[Nutrition Calculator]\n")
    
    weight = get_float_input("Enter your weight (kg): ")
    
    print("\nSelect your goal:")
    print("1. Muscle Gain")
    print("2. Fat Loss")
    print("3. Muscle Maintenance")

    goal = None
    while True:
        if keyboard.is_pressed('1'):
            goal = 'gain'
            break
        elif keyboard.is_pressed('2'):
            goal = 'loss'
            break
        elif keyboard.is_pressed('3'):
            goal = 'maintenance'
            break
        elif keyboard.is_pressed('esc'):
            menu()
            return

    if goal == 'gain':
        protein = 2.2 * weight
        fat = 1.0 * weight
        carbs = 5.0 * weight
    elif goal == 'loss':
        protein = 2.5 * weight
        fat = 0.8 * weight
        carbs = 2.0 * weight
    elif goal == 'maintenance':
        protein = 2.0 * weight
        fat = 1.0 * weight
        carbs = 3.0 * weight
    
    print(f"\nYour daily macronutrient requirements are:")
    print(f"Protein: {protein:.2f} grams")
    print(f"Carbs: {carbs:.2f} grams")
    print(f"Fat: {fat:.2f} grams")
    input("\nPress Enter to return to the menu...")
    menu()

def information():
    clearscreen()
    print("\t[INFORMATION]\n")
    print("BMR (Basal Metabolic Rate) \nis the number of calories your body needs to perform basic functions like breathing, circulation, and cell production.\n")
    print("TDEE (Total Daily Energy Expenditure) \nis the number of calories your body needs to maintain your current weight, including all activities throughout the day.\n")
    input("\nPress Enter to return to the menu...")
    menu()

menu()