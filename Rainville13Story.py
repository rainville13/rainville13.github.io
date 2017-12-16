import turtle
import time 
def greeting():
    print("Hello!")
    response=input("Would you like to play? (yes/no): ")
    return response

def second_choice():
    time.sleep(2)
    print("Okay, You're living in a post apocolyptic world where you will inevitably die and your a mormon named James...")
    response=input("Do you still believe in your mormon ways (yes) or have you given up on them? (no)?")
    return response

def deny():
    time.sleep(1)
    print("Get outa here u thotticus rex")
    input("Enter any key to begone thot")
def opened():
    time.sleep(1)
    print("Your first task is to go grab a mormon outfit and live among the beasts in the sewers until you convert them to mormon beliefs")
     
    m = turtle.Turtle()
    m.speed(0)
    for i in range(4):
        m.forward(100)
        m.right(90)

def not_opened():
    time.sleep(1)
    print("Well i mean hey in this new world who could blame ya... sike... your a disgrace fam!")
     
    m = turtle.Turtle()
    m.speed(0)
    m.circle(30)
      
def record_deal():
    time.sleep(1)
    print("Go now and be swift?")
    response=input("Are you okay with living like this now? (Yes/No)")
    return response
def rip():
    print("You're friends and family would of been so dissappointed in your decision!")
    time.sleep(1)
    print("You should rethink ur life u pleb")
    response=input("Do you wish to choose a new path because you are obviously a looser and cannot do simple tasks? (Yes/No)")
    return response

def end():
    time.sleep(1)
    print("Living as a civilian becomes too hard and you eventually die")
    input("Enter any key to leave scrub")
def thug_life():
    time.sleep(1)
    print("There is no other path for you in life James, you die. ")
    input("Enter any key to leave scrub")
def cat():
    time.sleep(1)
    print("You think about life as you slowly drink poison and end your anguish.")
    input("Enter any key to leave scrub")
x = greeting()
if x=="yes":


     
    y = second_choice()
    if y=="yes":
        opened()
    else:
        
        not_opened()

    if x=="yes":

        y = record_deal()
    if y=="yes":
    
        end()
        



    else:

        if x=="yes":
            y = rip()
    if y=="yes":
        thug_life()
    else:
            cat()


        
   
         
else:
        deny()



    

 
