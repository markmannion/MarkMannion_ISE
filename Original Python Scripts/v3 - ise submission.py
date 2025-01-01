print("\033[1m Welcome to Fota Island Golf Club: Deerpark Course \033[0m")
valuesEnteredCorrectly = False
while(not valuesEnteredCorrectly):
    try:
        yard = int(input("\033[1m What yardage do you have? \033[0m"))
        wind = int(input("\033[1m What is the wind speed? Negative if downwind (mph)  \033[0m"))
        temp = int(input("\033[1m What is the temperature? (*C) \033[0m"))
        hole = int(input("\033[1m Which hole are you playing? \033[0m"))
    except:
        print("Please enter your values again")
        continue
    valuesEnteredCorrectly = True

fa_temp = (temp * 1.8) + 32  # Converts the temperature entered into Fahrenheit

# Dictionary to add or take away distance based on the wind speed
wind_dict = {
    (-30, -25): -25,
    (-24, -20): -20,
    (-19, -15): -15,
    (-14, -10): -10,
    (-9, -5): -5,
    (-4,0): 0,
    (0,4): 0,
    (5, 9): 5,
    (10, 14): 10,
    (15, 19): 15,
    (20, 24): 20,
    (25, 30): 25,
}

# Determine adjusted yardage based on wind speed
wind_adj_yard = yard + next((adj for (low, high), adj in wind_dict.items() if low < wind <= high), 0)

# Dictionary to add or take away distance based on the temperature
temp_dict = {
    (24, 36): -10,
    (36, 46): -8,
    (46, 56): -6,
    (56, 66): -4,
    (66, 75): -2,
    (75, 75): 0,  
    (75, 85): 2,
    (85, 95): 4,
    (95, 105): 6,
    (105, 115): 8,
}

# Adjusts the yardage to include the effect of temperature
temp_adj_yard = wind_adj_yard + next((adj for (low, high), adj in temp_dict.items() if low < fa_temp <= high), 0)

# Slope gathered on course to adjust the yardage based on distance to the hole
slope_dict = {
    200: {1: 3, 2: -3, 3: -3, 4: -6, 5: -3, 6: 3, 7: 0, 8: 6, 9: -9, 10: -3, 11: 0, 12: 3, 13: -3, 14: 6, 15: -6, 16: 3, 17: 0, 18: -9},
    150: {1: 3, 2: -3, 3: -3, 4: -3, 5: -3, 6: 6, 7: 0, 8: 6, 9: -9, 10: -3, 11: 0, 12: 3, 13: -3, 14: 3, 15: -3, 16: 6, 17: 0, 18: -9},
    100: {1: 3, 2: -3, 3: -3, 4: -3, 5: -3, 6: 3, 7: 3, 8: 6, 9: -6, 10: 0, 11: 0, 12: 6, 13: -3, 14: 3, 15: -3, 16: 6, 17: 0, 18: -6},
    50: {1: 3, 2: -3, 3: -3, 4: 0, 5: -3, 6: 3, 7: 6, 8: 6, 9: -3, 10: 0, 11: 0, 12: 6, 13: -3, 14: 0, 15: 0, 16: 6, 17: 0, 18: -3},
}

# Adjust the final yardage based on the slope and distance from hole
for distance, adjustments in slope_dict.items():
    if yard in range(distance - 49, distance + 1):
    #if yard <= distance and yard >= distance - 49:
        fin_yard = temp_adj_yard + adjustments.get(hole, 0)
        print("\n")
        print("\033[1m Your final adjusted yardage is:  \033[0m", fin_yard)
        break

# Using different ranges to give my clubs a yardage
clubs = {
    range(0, 90): "Lob Wedge",
    range(90, 110): "Sand Wedge",
    range(110, 130): "Gap Wedge",
    range(130, 145): "Pitching Wedge",
    range(145, 160): "9 Iron",
    range(160, 170): "8 Iron",
    range(170, 180): "7 Iron",
    range(180, 190): "6 Iron",
    range(190, 200): "5 Iron",
    range(200, 210): "4 Iron",
    range(210, 500): "3 Wood",
}

# Tells me what club to hit based on the final adjusted yardage
for final_yardage_range, club in clubs.items():
    if fin_yard in final_yardage_range:
        print(f"\033[1m You should hit your {club}\033[0m")
        print("\n")
        break
    
    
    
    
    
    
    