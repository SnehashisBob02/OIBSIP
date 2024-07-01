height = float(input('Enter the height in m: '))
weight = float(input('Enter the weight in kg: '))

the_BMI=weight/(height)**2

print('Your Body Mass Index is: ',the_BMI)

if (the_BMI<16):
    print('Oh my god!You are severly underweight.Please take well care and visit a Doctor')

elif(the_BMI>=16 and the_BMI<18.5):
    print('Oops!You are underweight.please take care of yourself')

elif(the_BMI>=18.5 and the_BMI<25):
    print('Congratulations!You are completely Healthy')

elif(the_BMI>=25 and the_BMI<30):
    print('Eeee!You are overweight')

elif(the_BMI>=30):
    print('Shees!You are Obese')