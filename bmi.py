def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)
    print("BMI:", round(bmi,2))

    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi >= 18.5 or bmi <= 25:
        print("Normal Weight")
        return 1
    else:
        print("Over Weight")
        return 0
calculate_bmi(weight=57, height=1.73)