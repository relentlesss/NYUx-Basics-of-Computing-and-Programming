weight_pounds = input('Please enter weight in pounds: ')
height_inches = input('Please enter height in inches: ')

weight = float(weight_pounds) * 0.453592
height = float(height_inches) * 0.0254

bmi = weight / height**2

print('BMI is:', bmi)