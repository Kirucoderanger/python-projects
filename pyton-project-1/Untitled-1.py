choise = input("choose which game do you want to play DRIVING a or b or c")
if choise.lower() == "driving":
    choise2 = input("choose what you will do if i gave you a new brand ferrari--- RACE, ROD, CHASING---")
    if choise2.lower() == "race":
        choise3 = input("choose a driver --- SCHUMACHER, HAMILTON, LECLERC---")
        if choise3.lower() == "schumacher":
            print("if you are Schumacher, you dominated the sport formula 1 for five seasons between 2000 and 2004, winning five consecutive drivers' championships with Ferrari")
        elif choise3.lower() == "hamilton":
            print("if you were Hamilton you became the first driver to secure triple-digit pole positions and win 7 Championships	2008, 2014, 2015, 2017, 2018, 2019, 2020")
        elif choise3.lower() == "leclerc":
            print("if you were Leclerc you are now the highest rated young driver of the current era")
        else:
            print("trouble")  
    elif choise2.lower() == "rod":
        choise3 = input("while you driving on country rod you drive by SPEED or SLOW")
        if choise3.lower() == "speed":
            choise4 = input("while you are driving on a speed a wild animal leaping crossing the rod what are you going to do BREAK the speed, TURN the weel or SMASH the animal")
            if  choise4.lower == "break":
                choise5 = input("if you choose to break the speend and stop the car what are you going to do with the animal pick and CARE, help CROSS or PASS behind")
                if choise5.lower() == "care":
                     print ("you choose to care for the animal and heal the woond for that you will be happy in your life ")
                elif choise5.lower() == "cross":
                    print ("you did a great job for that you will have a peace of mind")
                elif choise5.lower() == "pass":
                    print ("not far whene you are out of feule and stop on the road")
                else:
                    print ("troble5")
            elif choise4.lower() == "turn":
                choise5 = input("i am sorry you are in a very high speed i cant do anything exept giving to choose how you endup fail in to the DITCH, CLIF or over FANCE ")
                if 	choise5.lower() == "ditch":
                    print ("you sustain a damage on you car suspention and break your neck")
                elif choise5.lower() == "CLIF":
                    print ("you sustain a heavy damage complet damage on your car and prbably you lost your life")
                elif choise5 == " fance":
                    print ("you sustain a heavy damage on you car but you are saved becous you wear a sitbelt")
                else: 
                    print ("trouble5")
            elif choise4.lower() == "smash":
                choise5 = input("what would you expect hapen to you  chose one the BLOOD of the animal sprinkel on your window, lose the BALANCE of your weel, you herd GROGLING soud and continue your rod ")
                if 	choise5.lower() == "blood":
                    print ("unfortunatly the blood of the animal cover your site and heat the track coming in front and sufer damage")
                elif choise5.lower() == "balance":
                    print ("your car fleeped 3 times and trown to the other side of the road")
                elif choise5.lower == " grogling":
                    print ("smashing the helpless animal hanting you the rest of your life")
                else: 
                    print ("trouble5")
            else: 
                print ("troble4")
        elif choise3.lower() == "slow":
            choise4 = input("while you are driving slow pepole ask you to give them a ride which one of the do you choose a bueatiful LADY, an OLD man or a man with SUIT and breifcase")
            if choise4.lower == "lady":
                choise5 = input("she invite you to satay with her in the mottel ovrnight what you will say to her YES, only for a caple of DRINK or NO ")
                if choise5.lower == "yes":
                    print ("she turned in to vampire in the middel of the night and suck out your blood")
                elif choise5.lower() == "drink": 
                    print("she robed you and left while you are drinking")
                elif choise5.lower() == "no":
                    print ("safly arived at your home and enjoyed a good evening")
                else: print ("troble")
            elif choise4.lower == "old":
                choise5 = input("the old man starts telling story while you are driving what is your response to that tell him to keep QUITE, open your RADIO to the maximum volume or LISTEN to his stort  ")
                if choise5.lower() == "QUITE":
                    print ("you endured the worst driveway of your life and get home with bad mood")
                elif choise5.lower() == "RADIO":
                    print ("you arrived to your home with bad headeck")
                elif choise5.lower() == "LISTEN":
                    print("find out the old headn tresure")
                else: print("trouble")
            elif choise4.lower == "SUIT":
                choise5 = input(" accidentaly the man open the briefcase and you see a banch of money a gun and several passport what is you action stop the care and GRAB his brife case to chase him out, stop the care and RUN away to hte woods or polietly ASK him what is going on  ")
                if choise5.lower == "grab":
                    print("the man puled the gun and shot you three times")
                elif choise5.lower() == "run":
                    print ("the man took your car and run awy while you are looking from the woods")
                elif choise5.lower() == "ASK":
                    print ("he replayed he is a marshal agent on a mission and promised you will be awarded for copration")
                else: 
                    print("trouble")
            else: print ("trouble7")
        else: 
            print ("troble3")
    else:
        print ("troble2")
else: 
    print ("troble1")