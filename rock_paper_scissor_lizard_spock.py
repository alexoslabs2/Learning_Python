import random
list = ["rock","paper","scissors","spock","lizard"]
computer_choice = (random.choice(list))
user_choice = input('Do you want - rock, paper, scissors, spock, or lizard?\n')
if computer_choice == user_choice:
    print('Tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'rock' and computer_choice == 'lizard':
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'lizard' and computer_choice == 'spock':    
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'spock' and computer_choice == 'scissors':    
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'lizard':    
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'lizard' and computer_choice == 'paper':    
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'spock':    
    print('Win, the computer had ' + computer_choice)
elif user_choice == 'spock' and computer_choice == 'rock':    
    print('Win, the computer had ' + computer_choice) 
else:
    print('You lose :( Computer wins :D it has ' + computer_choice)
