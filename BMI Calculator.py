def calculate_bmi(weight, height):

    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

def main():
    print("BMI Calculator")
    

    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))

    bmi = calculate_bmi(weight, height)
    

    if isinstance(bmi, str):
        print(bmi)
    else:
        print(f"Your BMI is: {bmi:.2f}")
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")

if __name__ == "__main__":
    main()
