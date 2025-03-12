'''
Author: Dominic Wanjau
Project: Analyzing data
'''


lowest_life_expectancy = 99999
highest_life_expectancy = -9999
data =[]


with open('life-expectancy.csv') as life_data:
    next(life_data)

  

    for line in life_data:
        oldline = line.strip()
        newline = oldline.split(',')

        countries = newline[0]
        codes = newline[1]
        years = int(newline[2])
        ages = float(newline[3])
        
        data.append((countries, codes, years, ages))

        
        if ages < lowest_life_expectancy:
            lowest_life_expectancy = ages
            least_in_country = countries
    


        if ages > highest_life_expectancy :
            highest_life_expectancy = ages
            highest_in_country = countries

    print(f'The highest life expectancy is: {highest_life_expectancy} in {highest_in_country}')
    print(f'The overal lowest life expectancy is: {lowest_life_expectancy} in {least_in_country}')

maxi_life = -1
mini_life = 9999
ave_life = 0
count = 0
maxi_country = ''
mini_country = ''
max_code = ''
min_code = ''

user_year = int(input('Enter the year: '))

for country,code,year,age in data:
    if user_year == year:
        ave_life += age 
        count += 1

        if age > maxi_life:
            maxi_life = age
            maxi_country = country
            max_code = code

print(f'The maximum life expectancy is {maxi_life} for {maxi_country}- {max_code}')


        # if age < mini_life:
        #     mini_life = age
        #     mini_country = country
        #     min_code = code

#if count > 0 :
    #sum_life = ave_life / count
    #print(f'The average life is {sum_life:.2f}')
    #print(f'The maximum life expectancy is {maxi_life} for {maxi_country}- {max_code}')
    #print(f'The minimum life expectancy is {mini_life} for {mini_country}- {min_code}')

#else:
    #print(f'Data not available for the year: {user_year}')

    
    


