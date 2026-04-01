import random # importing random so it can pick random characters for password
print ('Your password is : ') # display this message  to user

characters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*?' # letters and numbers to create the password you can add more which is better

password = '' # leave string empty to build password
for x in range(8): # this will loop 8 times to create a password with 8 characters in it ( you can make it longer if you like )

    password += random.choice(characters)
    # this will randomly pick out 8 random charaters in characters and place it into the empty password string

print (password) # prints out the new random password  after the loop :)