#text based adventure game
#autor Kirubel Mekonen Lemu
#the game has additional levels on tow of the first scenarios
#the game is played by tow pepols and they enjoid it
#the game has tow additional games to be relesd on the next version

choise = input("choose which game do you want to play DRIVING or STORY or NUMBERS: ")
if choise.lower() == "driving":
    choise2 = input("choose what you will do if i gave you a new brand ferrari--- RACE, ROD, CHASING---: ")
    if choise2.lower() == "race":
        choise3 = input("choose a driver --- SCHUMACHER, HAMILTON, LECLERC---: ")
        if choise3.lower() == "schumacher":
            print("if you are Schumacher, you dominated the sport formula 1 \nfor five seasons between 2000 and 2004, winning five consecutive drivers' championships with Ferrari")
        elif choise3.lower() == "hamilton":
            print("if you were Hamilton you became the first driver to secure triple-digit pole positions and \nwin 7 Championships	2008, 2014, 2015, 2017, 2018, 2019, 2020")
        elif choise3.lower() == "leclerc":
            print("if you were Leclerc you are now the highest rated young driver of the current era")
        else:
            print("you enterd a wrong word, in put only words writen in capital letter")  
    elif choise2.lower() == "rod":
        choise3 = input("while you driving on country rod you drive by SPEED or SLOW: ")
        if choise3.lower() == "speed":
            choise4 = input("while you are driving on a speed a wild animal leaping crossing the rod \nwhat are you going to do BREAK the speed, TURN the weel or SMASH the animal: ")
            if choise4.lower() == "break":
                choise5 = input("if you choose to break the speend and stop the car what are you going to do with the animal \npick the animsl and CARE, help CROSS or PASS behind: ")
                if choise5.lower() == "care":
                     print ("you choose to care for the animal and heal the woond for that you will be happy in your life ")
                elif choise5.lower() == "cross":
                    print ("you did a great job for that you will have a peace of mind")
                elif choise5.lower() == "pass":
                    print ("not far whene you are out of feule and stop on the road")
                else:
                    print ("you enterd a wrong word, in put only words writen in capital letter")
            elif choise4.lower() == "turn":
                choise5 = input("i am sorry you are in a very high speed i cant do anything exept giving to choose how you endup \nfail in to the DITCH, CLIF or over FANCE: ")
                if 	choise5.lower() == "ditch":
                    print ("you sustain a damage on you car suspention and break your neck")
                elif choise5.lower() == "clif":
                    print ("you sustain a heavy damage complet damage on your car and prbably you lost your life")
                elif choise5 == "fance":
                    print ("you sustain a heavy damage on you car but you are saved becous you wear a seatbelt")
                else: 
                    print ("you enterd a wrong word, in put only words writen in capital letter")
            elif choise4.lower() == "smash":
                choise5 = input("what would you expect hapen to you  chose one \n the BLOOD of the animal sprinkel on your window, \nlose the BALANCE of your weel, you herd GROGLING soud and continue your rod: ")
                if 	choise5.lower() == "blood":
                    print ("unfortunatly the blood of the animal cover your site and heat the track coming in front and sufer damage")
                elif choise5.lower() == "balance":
                    print ("your car fleeped 3 times and trown to the other side of the road")
                elif choise5.lower() == "grogling":
                    print ("smashing the helpless animal hanting you the rest of your life")
                else: 
                    print ("you enterd a wrong word, in put only words writen in capital letter")
            else: 
                print ("you enterd a wrong word, in put only words writen in capital letter")
        elif choise3.lower() == "slow":
            choise4 = input("while you are driving slow pepole ask you to give them a ride which one of the do you choose a \nbueatiful LADY, an OLD man or a man with SUIT and breifcase: ")
            if choise4.lower() == "lady":
                choise5 = input("she invite you to satay with her in the mottel ovrnight \nwhat you will say to her YES, only for a caple of DRINK or NO: ")
                if choise5.lower() == "yes":
                    print ("she turned in to vampire in the middel of the night and suck out your blood")
                elif choise5.lower() == "drink": 
                    print("she robed you and left while you are drinking")
                elif choise5.lower() == "no":
                    print ("safly arived at your home and enjoyed a good evening")
                else: print ("you enterd a wrong word, in put only words writen in capital letter")
            elif choise4.lower() == "old":
                choise5 = input("the old man starts telling story while you are driving what is your response to that \ntell him to keep QUITE, open your RADIO to the maximum volume or LISTEN to his stort:  ")
                if choise5.lower() == "quite":
                    print ("you endured the worst driveway of your life and get home with bad mood")
                elif choise5.lower() == "radio":
                    print ("you arrived to your home with bad headeck")
                elif choise5.lower() == "litsen":
                    print("find out the old headn tresure")
                else: print("you enterd a wrong word, in put only words writen in capital letter")
            elif choise4.lower() == "suit":
                choise5 = input(" accidentaly the man open the briefcase and you see a banch of money a gun and several passport \nwhat is you action stop the car and GRAB his brife case to chase him out, \nstop the car and RUN away to hte woods or polietly ASK him what is going on: ")
                if choise5.lower() == "grab":
                    print("the man puled the gun and shot you three times")
                elif choise5.lower() == "run":
                    print ("the man took your car and run awy while you are looking from the woods")
                elif choise5.lower() == "ask":
                    print ("he replayed he is a marshal agent on a mission and promised you will be awarded for copration")
                else: 
                    print("you enterd a wrong word, in put only words writen in capital letter")
            else: print ("you enterd a wrong word, in put only words writen in capital letter")
        else: 
            print ("you enterd a wrong word, in put only words writen in capital letter")
    elif choise2.lower() == "chasing":
        choise3 = input("you had the brand new Ferrari which i gave you and you stoped by a gass station \nsuddenly a fujitive come bay and  he showed you a gan forcing you to take him on drive way \nwhat you will do, you let him in ONBORD or quickliy DRIVE your car with out him: ")
        if choise3.lower() == "onbord":
            choise4 = input("the police starting chasing after your car what are you going to do \nSLOW the car, SPEED the car with maximum gear or strugle to UPRHEND the fujitive: ")
            if choise4.lower() == "slow":
                print ("the fujitive shoot you with the gan and throw you out and took your car and run away")
            elif choise4.lower() == "speed":
                print ("you heat the police fance on the rod and your car wreak sent to jail with the fujitive")
            elif choise4.lower() == "uprhend":
                print ("the fujitive try to shoot you but you used the gas and the break easly able to uprhend the fujitive")
            else: print ("you enterd a wrong word, in put only words writen in capital letter")
        elif choise3.lower() == "drive":
            choise4 = input("the gas cable detach with your car and  spel the gas along side on the rod \nthe fujitive light a mach and throw the fire and the fire cout your car \nwhat are you going to do \nstop the car and RUN away, CONTINUE driving while your car is burning or stop the car and use \nyour fire distingusher and try ELIMINATE the fire: ")
            if choise4.lower() == "run":
                print ("the fujtive came by and fire the gun at you and wond your leg you fell down on the rod cry out loud")
            elif choise4.lower() == "continue":
                print ("eventualy the fire reach your car gas tanker and blow up your car wile you are inside")
            elif choise4.lower() == "eliminate":
                print ("the fire gose off and able to drive away before the fujitive caths you heating him with the fire destingusher")
            else: print ("you enterd a wrong word, in put only words writen in capital letter")
        
    else:
        print ("you enterd a wrong word, in put only words writen in capital letter")
elif choise.lower() == "story":
    print ("This game is on the making will be relesed on the next virsion")
elif choise.lower() == "numbers":
    print ("This game is on the making will be relesed on the next virsion")
else: 
    print ("you enterd a wrong word, in put only words writen in capital letter")