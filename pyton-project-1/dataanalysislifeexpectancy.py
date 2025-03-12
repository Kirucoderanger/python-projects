with open ("c:/Users/kirub/Downloads/life-expectancy.csv") as life_expectancy_csv:
    next(life_expectancy_csv)
    highest = 0
    lowest = 999
    for life_expectancy in life_expectancy_csv:
        life_expectancy = life_expectancy.strip()
        life_expectancy_list = life_expectancy.split(",")
        if float(life_expectancy_list[3]) > highest:
            highest = float(life_expectancy_list[3])
        if float(life_expectancy_list[3]) < lowest:
            lowest = float(life_expectancy_list[3])
    print (highest)
    print (lowest)
