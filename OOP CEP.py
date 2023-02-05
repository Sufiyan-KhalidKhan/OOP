print("\n\n****************\t\tLET'S PLAY A GAME OF SCRABBLE!!!\t\t****************\n\n")

#importing 'textblob' module
from textblob import Word

checking = "True"

#initializing spell checking function
def checkSpelling(word):
    global checking
    word = Word(word)
    result = word.spellcheck()
    if(word == result [0][0]):
        checking = "True"
        print("Spelling of \"" + word.upper() + "\" is correct")
    else:
        print("Spelling of \"" + word.upper() + "\" is not correct")
        print("Your Score = 0")
        checking = "False"

#initializing main() function
def main():

#creating a list
    letter_list = []

#creating a dictionary
    letter_dictionary = {}

#taking input from the user
    n = input("How many letters would you like to play with? (Should be between '03' and '15'): ")
#checking if the input is integer or string
    while(n.isdigit() == True):

    #checking if n is between 3 to 15
        while((int(n) < 3) or (int(n) > 15)):
            print("Please enter a number between 3 and 15.")
            n = int(input("How many letters would you like to play with?  "))
        
        while (3 <= int(n) <= 15):
            for i in range(0, int(n)):
                x = input("\nEnter the letter: ")
                y = int(input("Enter the score for the letter  (Should be between '01' and '09'): "))
            
            #checking if score is negative or zero or greater than 10
                while((y < 1) or (y > 9)):
                    print("Score out of range.\nPlease enter a valid score.")
                    y = int(input("Enter the score for the letter  (Should be between '01' and '09'): "))
                letter_list.append(x)
                letter_dictionary[x] = y
            print("\nThe entered letters are:  ", [i.upper() for i in letter_list])
            
        #taking input word from the user
            word = input("\nConstruct a word out of the letters: ")
            print("\nYou made \"" + word.upper() + "\" from the entered letters.")
            
        #checking if the input letter is in the letter list
            for i in range (0, len(word)):
                if (word[i]) not in (letter_list):
                    print(word[i].upper() + " is INVALID LETTER.")
                    break
            else: 
                checkSpelling(word)
        
        #summing the values of the letters    
            if(checking == "True"):
                if(len(word) < len(letter_list)):
                    print("Your score = ", sum([letter_dictionary.get(i, 0) for i in word]))
                elif(word[i] in letter_list):
                        print("Your score = ", sum([letter_dictionary.get(i, 0) for i in word]) + 50)
                else:
                    print("Your input word is greater than the letters mentioned.\nYou scored zero.")
        
        #asking to play again!!!
            ans = input("\nDo you want to play again? (Y/N):  ")
            while((ans == 'y') or (ans == 'Y') or (ans == 'n') or (ans == 'N') or (ans != 'y' or 'Y' or 'n' or 'N')):
                if((ans == 'y') or (ans == 'Y')):
                    main()
                elif((ans == 'n') or (ans == 'N')):
                    print("THANK YOU FOR PLAYING!!!\nQUITING...\n\n")
                    quit()
                else:
                    print("Please enter appropriate option.")
                    ans = input("\nDo you want to play again? (Y/N):  ")
    
    else:
        print("Number of letters should be a positive integer.\nSTARTING OVER...\n\n")
        main()


#Executing the main() function
main()