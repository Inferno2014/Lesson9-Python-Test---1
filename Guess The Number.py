import random
num = random.randint(1,100)
att = 0
while att<=5:
    guess = int(input('Guess a number from 1 to 100 in five attempts. You will be given clues on where is the number.: '))
    att+=1
    if guess > num:
        print('The number is less than',guess)
    elif guess < num:
        print('The number is greater than',guess)
    elif guess == num:
        print('Correct guess! The number was',num)
        break
    if att>=5:
        print('You lost all your attempts! The number was',num)
        break
