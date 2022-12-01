#The task is to generate a random story every time user runs the program.
# Importing the required modules
import random
when = ['Once upon a time','A few years ago', 'Tomorrow', 'Last night', 'A long time ago','Since 2005','Everyday','Once a long ago']
who = ['Rahul and Meena', 'a stranger', 'some friends', 'Relatives','some animals','a boy and a girl','students','some engineer and doctors']
went = ['went to cinema hall', 'went to their university','go to seminar', 'go to water park', 'gone to ammusement park']
happened = ['made a lot of memories','ate some junk food', 'found a secret key', 'enjoyed a lot', 'seen the future']
# Defining the main function
def main():
#This is the main function.
    print(random.choice(when), random.choice(who), random.choice(went), random.choice(happened))
# Calling the main function
if __name__  == '__main__':
    main()


    