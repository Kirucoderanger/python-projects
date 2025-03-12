#Auter Kirubel Mekonen Lemu
#World wide life expectancy data analysis
#The program analysis life expectancy of world wide, contenentaly, country, yearly
#for all catagories the programe analysis the largest, lowest, average and big drop life expectancy 
with open ("c:/Users/kirub/Downloads/lifeexpectancy.csv") as life_expectancy_txt:
	next (life_expectancy_txt)
	expectancy_list = []
	for life_expectancy_list in life_expectancy_txt:
		strip_life_ecpectancy = life_expectancy_list.strip()
		splited_life_expectancy = strip_life_ecpectancy.split(",")
		expectancy_list.append(splited_life_expectancy)
	while exit != "quit":
		print ("Select one of life expectancy analysis you want to view")
		print ("1. World wide life expectancy analysis")
		print ("2. Continental life expectancy analysis")
		print ("3. Country wide life expectancy analysis")
		print ("4. Yearly life expectancy analysis")
		print ("5. World wide largest life expectancy drope")
		print ("6. to exit enter Quit")
		action = input ("Pleas enter a choies number: ")
		if action == "1":
			largest = expectancy_list[0][3]
			year_largest = expectancy_list[0][2]
			country_largest = expectancy_list[0][0]
			smalest = expectancy_list[0][3]
			year_smalest = expectancy_list[0][2]
			country_smalest = expectancy_list[0][0]
			expectancy_count = 0
			total_expectancy = 0
			big_drope = 0
			curent_expectancy1 = expectancy_list[0][3]
			next_expectancy1 = expectancy_list[1][3]
			year_curent = expectancy_list[0][2]
			year_next = expectancy_list[0][2]
			country_drope = expectancy_list[0][0]
			for i in range (len(expectancy_list)):
				expectancy_count += 1
				total_expectancy += float(expectancy_list[i][3])
				if float(expectancy_list[i][3]) > float(largest):
					largest = float(expectancy_list[i][3])
					year_largest = expectancy_list[i][2]
					country_largest = expectancy_list[i][0]
				if float(expectancy_list[i][3]) < float(smalest):
					smalest = float(expectancy_list[i][3])
					year_smalest = expectancy_list[i][2]
					country_smalest = expectancy_list[i][0]
     
			average_expectancy = total_expectancy/expectancy_count

			for i in range (len(expectancy_list) - 1):
				if expectancy_list[i][0] == expectancy_list[i+1][0]:
					curent_expectancy = float(expectancy_list[i][3])
					next_expectancy = float(expectancy_list[i+1][3])
					drope = curent_expectancy - next_expectancy
					if drope > big_drope:
						big_drope = drope
						year_curent = int(expectancy_list[i][2])
						year_next = int(expectancy_list[i+1][2])
						curent_expectancy1 = float(expectancy_list[i][3])
						next_expectancy1 = float(expectancy_list[i+1][3])
						country_drope = expectancy_list[i][0]
			print (f"World wide largest life expectancy is {largest:.2f} years, recorded in {year_largest} at {country_largest}.")
			print (f"World wide smalest life expectancy is {smalest:.2f} years, recorded in {year_smalest} at {country_smalest}.")
			print (f"World wide average life expectancy is {average_expectancy:.2f} years.")
			print (f"World wide the largest life expectancy drop in a single year is {big_drope:.2f} recorded in {country_drope.upper()} between {year_curent} and {year_next}, declined from {curent_expectancy1:.2f} to {next_expectancy1:.2f} years.")
			
		elif action == "2":
			print ("Which continent life expectancy analysis you want to view")
			print ("1. Asia")
			print ("2. Africa")
			print ("3. Americas")
			print ("4. Europ")
			continent = input ("pleas enter the choies number: ")
			choise = ""
			if continent == "1":
				choise = "Asia"
			elif continent == "2":
				choise = "Africa"
			elif continent == "3":
				choise = "Americas"
			elif continent == "4":
				choise = "Europ"
			#country_analysis = input ("Which country life expectancy analysis you want view").capitalize()
			year_count2 = 0
			total_expectancy2 = 0
			largest2 = 0
			year_largest2 = expectancy_list[0][2]
			smalest2 = 999
			year_smalest2 = expectancy_list[0][2]
			year_start = 3333
			year_end = 0
			
			big_drope1 = 0
			curent_expectancy2 = expectancy_list[0][3]
			next_expectancy2 = expectancy_list[1][3]
			year_curent1 = expectancy_list[0][2]
			year_next1 = expectancy_list[0][2]
			country_drope1 = expectancy_list[0][0]
			
			for i in range (len(expectancy_list)):
				if choise == expectancy_list[i][0]:
					#country_list = expectancy_list[i][0]
					year_count2 += 1
					total_expectancy2 += float(expectancy_list[i][3])
					if float(expectancy_list[i][3]) > float(largest2):
						largest2 = float(expectancy_list[i][3])
						year_largest2 = int(expectancy_list[i][2])
					if float(expectancy_list[i][3]) < float(smalest2):
						smalest2 = float(expectancy_list[i][3])
						year_smalest2 = int(expectancy_list[i][2])
					if float(expectancy_list[i][2]) > float(year_end):
						year_end = int(expectancy_list[i][2])
					if float(expectancy_list[i][2]) < float(year_start):
						year_start = int(expectancy_list[i][2])
						
			for i in range (len(expectancy_list) - 1):
				if choise == expectancy_list[i][0]:			
						
					if expectancy_list[i][0] == expectancy_list[i+1][0]:
						curent_expectancy1 = float(expectancy_list[i][3])
						next_expectancy1 = float(expectancy_list[i+1][3])
						drope1 = float(curent_expectancy1 - next_expectancy1)
						if drope1 > big_drope1:
							big_drope1 = drope1
							year_curent1 = int(expectancy_list[i][2])
							year_next1 = int(expectancy_list[i+1][2])
							curent_expectancy2 = float(expectancy_list[i][3])
							next_expectancy2 = float(expectancy_list[i+1][3])
							country_drope1 = expectancy_list[i][0]
						
						
			average_expectancy2 = total_expectancy2/year_count2
			all_years = (year_end - year_start) + 1
			
			print (f"This analysis based on {all_years} years recored between {year_start} - {year_end} in {choise}.")
			print (f"The largest life expectancy is {largest2:.2f} years in {year_largest2}.")
			print (f"The smalest life expectancy is {smalest2:.2f} years in {year_smalest2}.")
			print (f"The average life expectancy in {country_drope1.upper()} is {average_expectancy2:.2f}.")
			print (f"The largest life expectancy drop in a single year is {big_drope1:.2f} recorded in {country_drope1.upper()} between {year_curent1} and {year_next1}, declined from {curent_expectancy2:.2f} to {next_expectancy2:.2f} years.")

			
   
   
		elif action == "4":

   
			year = int(input ("Which year analysis do you need"))
			year_count = 0
			total_expectancy = 0
			largest1 = 0
			year_largest1 = expectancy_list[0][2]
			country_largest1 = expectancy_list[0][0]
			smalest1 = 999
			year_smalest1 = expectancy_list[0][2]
			country_smalest1 = expectancy_list[0][0]
			for i in range (len(expectancy_list)):
				if float(expectancy_list[i][2]) == year:
					year_count += 1
					total_expectancy += float(expectancy_list[i][3])
					if float(expectancy_list[i][3]) > float(largest1):
						largest1 = float(expectancy_list[i][3])
						year_largest1 = expectancy_list[i][2]
						country_largest1 = expectancy_list[i][0]
					if float(expectancy_list[i][3]) < float(smalest1):
						smalest1 = float(expectancy_list[i][3])
						year_smalest1 = expectancy_list[i][2]
						country_smalest1 = expectancy_list[i][0]
				
					
			average_expectancy = total_expectancy/year_count
			print (year_count)
			print (f"World wide average life expectancy in {year} is {average_expectancy:.2f} years.")
			print (f"world wide largest life expectancy is {largest1:.2f} years in {year_largest1} at {country_largest1}.")
			print (f"world wide largest life expectancy is {smalest1:.2f} years in {year_smalest1} at {country_smalest1}.")
			
		elif action == "5":
			big_drope = 0
			curent_expectancy1 = expectancy_list[0][3]
			next_expectancy1 = expectancy_list[1][3]
			year_curent = expectancy_list[0][2]
			year_next = expectancy_list[0][2]
			country_drope = expectancy_list[0][0]
			for i in range (len(expectancy_list) - 1):
				if expectancy_list[i][0] == expectancy_list[i+1][0]:
					curent_expectancy = float(expectancy_list[i][3])
					next_expectancy = float(expectancy_list[i+1][3])
					drope = curent_expectancy - next_expectancy
					if drope > big_drope:
						big_drope = drope
						year_curent = int(expectancy_list[i][2])
						year_next = int(expectancy_list[i+1][2])
						curent_expectancy1 = float(expectancy_list[i][3])
						next_expectancy1 = float(expectancy_list[i+1][3])
						country_drope = expectancy_list[i][0]
			print (f"World wide the largest life expectancy drop in a single year is {big_drope:.2f} recorded in {country_drope.upper()} between {year_curent} and {year_next}, declined from {curent_expectancy1:.2f} to {next_expectancy1:.2f} years.")
	
 
		elif action == "3":
 		
			country_analysis = input ("Which country life expectancy analysis you want view").capitalize()
			year_count2 = 0
			total_expectancy2 = 0
			largest2 = 0
			year_largest2 = expectancy_list[0][2]
			smalest2 = 999
			year_smalest2 = expectancy_list[0][2]
			year_start = 3333
			year_end = 0
			
			big_drope1 = 0
			curent_expectancy2 = expectancy_list[0][3]
			next_expectancy2 = expectancy_list[1][3]
			year_curent1 = expectancy_list[0][2]
			year_next1 = expectancy_list[0][2]
			
			for i in range (len(expectancy_list)):
				if country_analysis == expectancy_list[i][0]:
					#country_list = expectancy_list[i][0]
					year_count2 += 1
					total_expectancy2 += float(expectancy_list[i][3])
					if float(expectancy_list[i][3]) > float(largest2):
						largest2 = float(expectancy_list[i][3])
						year_largest2 = int(expectancy_list[i][2])
					if float(expectancy_list[i][3]) < float(smalest2):
						smalest2 = float(expectancy_list[i][3])
						year_smalest2 = int(expectancy_list[i][2])
					if float(expectancy_list[i][2]) > float(year_end):
						year_end = int(expectancy_list[i][2])
					if float(expectancy_list[i][2]) < float(year_start):
						year_start = int(expectancy_list[i][2])
						
						
			for i in range (len(expectancy_list) - 1):
				if country_analysis == expectancy_list[i][0]:			
					if expectancy_list[i][0] == expectancy_list[i+1][0]:
						curent_expectancy1 = float(expectancy_list[i][3])
						next_expectancy1 = float(expectancy_list[i+1][3])
						drope1 = float(curent_expectancy1 - next_expectancy1)
						if drope1 > big_drope1:
							big_drope1 = drope1
							year_curent1 = int(expectancy_list[i][2])
							year_next1 = int(expectancy_list[i+1][2])
							curent_expectancy2 = float(expectancy_list[i][3])
							next_expectancy2 = float(expectancy_list[i+1][3])
						
						
			average_expectancy2 = total_expectancy2/year_count2
			all_years = (year_end - year_start) + 1

			print (f"This analysis based on {all_years} years recored between {year_start} - {year_end} in {country_analysis.capitalize()}.")
			print (f"The largest life expectancy is {float(largest2):.2f} years in {year_largest2}.")
			print (f"The smalest life expectancy is {smalest2:.2f} years in {year_smalest2}.")
			print (f"The average life expectancy in {country_analysis.upper()} is {average_expectancy2:.2f}.")
			if year_curent1 == year_next1:
				print (f"No life expectancy drope register between {year_start} - {year_end} in {country_analysis.capitalize()}")
			else:
				print (f"The largest life expectancy drop in a single year is {float(big_drope1):.2f} recorded in {country_analysis.upper()} between {year_curent1} and {year_next1}, declined from {curent_expectancy2} to {next_expectancy2} years.")

		elif action == "6":
			exit = "quit"
		else:
			print ("Invalid input")
			
					
			
					
			
			
 