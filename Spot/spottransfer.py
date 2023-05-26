#mobile money transaction for a network called SPOT.
#It only shows the process of sending money from one user to another.
#and also checking the remaining balance.


#we import time to slow down the point where the image is shown
#import subprocess to open the image and close the display

import time, subprocess

#Creating a fake database with a dictionary
#Each is a dictionary with {name: [number, amount of money, filename]}
#the amount of money will not be used in this process.
#Let us assume that only 4 other people are using this network worldwide.
Database = {
    'Yaa Asantewaa': ['S184021921', 1000, 'yaaasantewaa.jpg'],
    'J. J. Rawlings': ['S194722020', 1000, 'jjrawlings.jpg'],
    'Kwame Nkrumah': ['S190921972', 2000, 'kwamenkrumah.jpg'],
    'Theodosia Okoh': ['S192222015', 1000, 'theodosia.jpg']
}
# a funny this info is that they are people who are dead 
#and the phone shows when they were born 2 when they died

#My password to access my money
mypword = '2billioncedis'

#The amount of money in my account
mymoney = 2000000000
remaining = format(mymoney, ',')

# E levy is the tax that is deducted from each transaction above 100 cedis
Elevy = 0
def tax(money):
    if money > 100:
        global Elevy
        Elevy = round(money/100,2)
        return Elevy
    else:
        return Elevy

   
#This is the user's number which you can dial to send the money to.
#It takes its values from the "def code()" where the transaction process begins.
def digits(user_network):
    if int(user_network) == 1:
        phonenumber = input("Enter User's number\n")
        name, phone, balance, picture = "", "", "", ""  # Initialize the variables outside the loop
        found = False  # Flag variable to track if a matching phone number is found

        #Here we separate the items in the dictionary into key and values
        for key, values in Database.items():
            name, phone, balance, picture = key, values[0], values[1], values[2]

            if phonenumber == phone:
                found = True  # Set the flag to True indicating a match is found
                confirmation = input("Confirm Number \n")

                #We confirm the phone number to see if it is still the same
                if confirmation == phone:
                    print(f"You are about to send money to {name}. Please check the picture to confirm")

                    #This is the part where the picture of the person is shown.
                    #First, a few seconds is given for the user to read the prompt
                    time.sleep(2)
                    
                    #Next we open the image who's filename is stored in the last element of the dictionary
                    subprocess.Popen(picture, shell=True)

                    #The picture is shown for ten seconds and then the exe is closed.
                    time.sleep(10) 
                    subprocess.call(['taskkill', '/F', '/IM', 'Microsoft.Photos.exe'])

                    #The user is expected to confirm if the picture is the same as the person
                    #he or she desires to send the money to.
                    picconfirmation = input(f'''Is that the same {name}? \n1.Yes \n2. No\n''')
                    if picconfirmation == '1':
                        
                        #If it is the same person, we enter the anount and reference.
                        amount = round(int(input("Enter Amount \n")), 2)
                        reference = input("Enter Reference \n")
                        tax(amount)
                        pword = input(f'''You are sending GHS {format(amount, ',')} to {name}, whose number is: {phone}, with reference '{reference}'. Tax amount is {format(Elevy, ',')}. Total amount is {format(amount+Elevy, ',')}
Enter your password to send. \n1. to Cancel \n''')

                        #The password is checked with the provided one to see if it matches
                        if pword == mypword:
                            #remaining is declared as a global variable, so that it can
                            #be returned when the user wants to check the balance.
                            global remaining
                            remaining = format(mymoney - amount - Elevy, ',')
                            print(f"{format(amount, ',')} sent on the Spot to {name}. Current balance is {remaining}")
                            another = input("Do you want to perform another transaction? \n1. Yes \n2. No \n")
                            if another == '1':
                                #if another transaction, the process is repeated.
                                code()
                            else:
                                print("Thank you for using Spot.")

                        elif pword == '1':
                            print("Thank you for using Spot.")
                            
                        else:
                            print("Wrong Password. Try again later.")
                    else:
                        print("Please check the number and try again.")
                else:
                    print("Please check the number and try again.")

        if not found:
            print("This number does not exist. Please try again.")


def code():
    #this begins the transaction process.
    response = input('''Welcome to Spot Cash
1. Transfer
2. Pay Bill
3. Approve Withdrawal
4. Airtime & Bundles
5. My Pocket
6. Help & Info
''')
    #Note that only options "1. Transfer" and "5. My pocket" are made to work.
    if int(response) ==1:
        user_network = input('''Transfer Cash
1. Spot user
2. Other Network
3. Bank Account
''')
        #we call the function which continues to perform the transaction
        digits(user_network)                      
         
     
    elif int(response) == 5:
        #this is to check the amount available in the users wallet.
        pocket = input('My Pocket \n1. Check balance\n2. Change or reset password \n3. Statements\n4. Report Issue \n')
        if pocket == '1':
            pword = input('Enter your password \n')
            if pword == mypword:
                print(f"Your Current Balance: GHS {remaining}")
                transaction = input("Do you want to perform another transaction? \n1.Yes \n2.No\n")
                if transaction == '1':
                    code()
                else:
                    print("Thank you for using Spot")
            else:
                print("Wrong Password. Try again.")
        
    else:
        print('Invalid Response')
        
code()

