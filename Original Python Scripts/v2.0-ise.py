print("Welcome to Fota Island Golf Club: Deerpark Course")
yard = int(input("What yardage do you have? "))
wind = int(input("What is the wind speed? (mph)  "))
temp = int(input("What is the temperature? (*Celsius)  "))
hole = int(input("Which hole are you playing? "))

fa_temp = (temp * 1.8) + 32  # Converts the temperature entered into Fahrenheit

# Dictionary to add or take away distance based on the wind speed
# Tuples instead of if/elif
wind_dict = {
    (-10, 10): 0,
    (10, 20): 10,
    (20, 30): 20,
    (30, 40): 30,
    (-20, -10): -10,
    (-30, -20): -20,
    (-40, -30): -30,
}

# Determine adjusted yardage based on wind speed
adj_yard = yard + next((adj for (low, high), adj in wind_dict.items() if low < wind <= high), 0)

# Dictionary to add or take away distance based on the temperature
# Tuples instead of if/elif
temp_dict = {
    (75, 75): 0,  
    (75, 85): 2,
    (85, 95): 4,
    (95, 105): 6,
    (105, 115): 8,
    (24, 36): -10,
    (36, 46): -8,
    (46, 56): -6,
    (56, 66): -4,
    (66, 75): -2,
}

# Adjusts the yardage to include the effect of temperature
temp_adj_yard = adj_yard + next((adj for (low, high), adj in temp_dict.items() if low < fa_temp <= high), 0)

# Slope gathered on course to adjust the yardage based on distance to the hole
slope_dict = {
    200: {1: 3, 2: -3, 3: -3, 4: -6, 5: -3, 6: 3, 7: 0, 8: 6, 9: -9, 10: -3, 11: 0, 12: 3, 13: -3, 14: 6, 15: -6, 16: 3, 17: 0, 18: -9},
    150: {1: 3, 2: -3, 3: -3, 4: -3, 5: -3, 6: 6, 7: 0, 8: 6, 9: -9, 10: -3, 11: 0, 12: 3, 13: -3, 14: 3, 15: -3, 16: 6, 17: 0, 18: -9},
    100: {1: 3, 2: -3, 3: -3, 4: -3, 5: -3, 6: 3, 7: 3, 8: 6, 9: -6, 10: 0, 11: 0, 12: 6, 13: -3, 14: 3, 15: -3, 16: 6, 17: 0, 18: -6},
    50: {1: 3, 2: -3, 3: -3, 4: 0, 5: -3, 6: 3, 7: 6, 8: 6, 9: -3, 10: 0, 11: 0, 12: 6, 13: -3, 14: 0, 15: 0, 16: 6, 17: 0, 18: -3},
}

# Adjust the final yardage based on the slope and distance from hole
for distance, adjustments in slope_dict.items():
    if yard <= distance and yard >= distance - 49:
        fin_yard = temp_adj_yard + adjustments.get(hole, 0)
        print("Your final adjusted yardage is: ", fin_yard)
        break

# Using different ranges to give my clubs a yardage
clubs = {
    range(0, 90): "lob wedge",
    range(90, 110): "sand wedge",
    range(110, 130): "gap wedge",
    range(130, 145): "pitching wedge",
    range(145, 160): "9 iron",
    range(160, 170): "8 iron",
    range(170, 180): "7 iron",
    range(180, 190): "6 iron",
    range(190, 200): "5 iron",
    range(200, 210): "4 iron",
    range(210, 500): "3 wood",
}

# Tells me what club to hit based on the final adjusted yardage
for yardage_range, club in clubs.items():
    if fin_yard in yardage_range:
        print(f"You should hit your {club}")
        break