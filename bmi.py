def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight/(height * height)
    print("BMI:", round(bmi,2))

    if bmi < 18.5:
        print("Under Weight")
        return -1
    elif bmi >= 18.5 and bmi <= 25:
        print("Normal Weight")
        return 0
    elif bmi > 25:
        print("Over Weight")
        return 1
calculate_bmi(weight=120, height=1.90)