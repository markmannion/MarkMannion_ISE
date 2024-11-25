#ISE Project Idea - Yardage Calculator#
print("Welcome to Fota Island Golf Club: Deerpark Course")
yard = int(input("What yardage do you have? "))
wind = int(input("What is the wind speed? (mph)  "))
temp = int(input("What is the temperature? (*Celsius)  "))
hole = int(input("Which hole are you playing? "))

fa_temp = (temp*1.8) +32 #Converts the temperature entered into fahrenheit)

adj_yard = 0

#If/Elif statements to determine the yardage to take off/ add on#
if wind>-10 and wind<10:
    adj_yard = yard + 0
elif wind > 9 and wind<20:
    adj_yard = yard + 10
elif wind >19 and wind< 30:
    adj_yard =  yard + 20
elif wind > 29 and wind<40:
    adj_yard = yard + 30
elif wind<0  and wind>-10:
    adj_yard = yard - 10
elif wind<-10 and wind >-20:
    adj_yard = yard -20
elif wind<-20 and wind>-30:
    adj_yard = yard - 30
elif wind<-30 and wind>-40:
    adj_yard = yard - 40
    
print(adj_yard)

temp_adj_yard = 0

#If/Elif statement to adjust yardage based on temperature#
if fa_temp == 75:
    temp_adj_yard = adj_yard+ 0
elif fa_temp > 75 and fa_temp <85:
    temp_adj_yard = adj_yard + 2
elif fa_temp > 84 and fa_temp <95:
    temp_adj_yard = adj_yard + 4
elif fa_temp > 94 and fa_temp <105:
    temp_adj_yard = adj_yard + 6
elif fa_temp > 104 and fa_temp <115:
    temp_adj_yard = adj_yard + 8
elif fa_temp > 24 and fa_temp <36:
    temp_adj_yard = adj_yard - 10
elif fa_temp > 34 and fa_temp <46:
    temp_adj_yard = adj_yard - 8
elif fa_temp > 44 and fa_temp <56:
    temp_adj_yard = adj_yard - 6
elif fa_temp > 54 and fa_temp <66:
    temp_adj_yard = adj_yard - 4
elif fa_temp > 64 and fa_temp <75:
    temp_adj_yard = adj_yard - 2

print(temp_adj_yard)

fin_yard = 0


#Functions for different distances to change the yardage based on slope#

def  dist_200(fin_yard, temp_adj_yard):
    if hole == 1:
        fin_yard = temp_adj_yard + 3
    elif hole == 2:
        fin_yard  = temp_adj_yard - 3
    elif hole == 3:
        fin_yard = temp_adj_yard - 3
    elif hole == 4:
        fin_yard = temp_adj_yard - 6
    elif hole == 5:
        fin_yard = temp_adj_yard - 3
    elif hole == 6:
        fin_yard  = temp_adj_yard + 3
    elif hole == 7:
        fin_yard  = temp_adj_yard + 0
    elif hole == 8:
        fin_yard  = temp_adj_yard + 6
    elif hole == 9:
        fin_yard = temp_adj_yard - 9
    elif hole == 10:
        fin_yard  = temp_adj_yard - 3
    elif hole == 11:
        fin_yard  = temp_adj_yard + 0
    elif hole == 12:
        fin_yard  = temp_adj_yard + 3
    elif hole == 13:
        fin_yard  = temp_adj_yard - 3
    elif hole == 14:
        fin_yard  = temp_adj_yard + 6
    elif hole == 15:
        fin_yard  = temp_adj_yard - 6
    elif hole == 16:
        fin_yard  = temp_adj_yard + 3
    elif hole == 17:
        fin_yard  = temp_adj_yard + 0
    elif hole == 18:
        fin_yard  = temp_adj_yard - 9
    
    print("Your final adjusted yardage is: ", fin_yard)
    
    if fin_yard<90:
        print("You should hit your lob wedge")
    elif fin_yard>89 and fin_yard<110:
        print("You should hit your sand wedge")
    elif fin_yard>109 and fin_yard<130:
        print("You should hit your gap wedge")
    elif fin_yard>129 and fin_yard<145:
        print("You should hit your pitching wedge")
    elif fin_yard>144 and fin_yard<160:
        print("You should hit your 9 iron")
    elif fin_yard>159 and fin_yard<170:
        print("You should hit your 8 iron")
    elif fin_yard>169 and fin_yard<180:
        print("You should hit your 7 iron")
    elif fin_yard>179 and fin_yard<190:
        print("You should hit your 6 iron")
    elif fin_yard>189 and fin_yard<200:
        print("You should hit your 5 iron")
    elif fin_yard>199 and fin_yard<210:
        print("You should hit your 4 iron")
    elif fin_yard>209:
        print("You should hit your 3 wood")

def  dist_150(fin_yard, temp_adj_yard):
    if hole == 1:
        fin_yard = temp_adj_yard + 3
    elif hole == 2:
        fin_yard  = temp_adj_yard - 3
    elif hole == 3:
        fin_yard = temp_adj_yard - 3
    elif hole == 4:
        fin_yard = temp_adj_yard - 3
    elif hole == 5:
        fin_yard = temp_adj_yard - 3
    elif hole == 6:
        fin_yard  = temp_adj_yard + 6
    elif hole == 7:
        fin_yard  = temp_adj_yard + 0
    elif hole == 8:
        fin_yard  = temp_adj_yard + 6
    elif hole == 9:
        fin_yard = temp_adj_yard - 9
    elif hole == 10:
        fin_yard  = temp_adj_yard - 3
    elif hole == 11:
        fin_yard  = temp_adj_yard + 0
    elif hole == 12:
        fin_yard  = temp_adj_yard + 3
    elif hole == 13:
        fin_yard  = temp_adj_yard - 3
    elif hole == 14:
        fin_yard  = temp_adj_yard + 3
    elif hole == 15:
        fin_yard  = temp_adj_yard - 3
    elif hole == 16:
        fin_yard  = temp_adj_yard + 6
    elif hole == 17:
        fin_yard  = temp_adj_yard + 0
    elif hole == 18:
        fin_yard  = temp_adj_yard - 9
    
    print("Your final adjusted yardage is: ", fin_yard)
    
    if fin_yard<90:
        print("You should hit your lob wedge")
    elif fin_yard>89 and fin_yard<110:
        print("You should hit your sand wedge")
    elif fin_yard>109 and fin_yard<130:
        print("You should hit your gap wedge")
    elif fin_yard>129 and fin_yard<145:
        print("You should hit your pitching wedge")
    elif fin_yard>144 and fin_yard<160:
        print("You should hit your 9 iron")
    elif fin_yard>159 and fin_yard<170:
        print("You should hit your 8 iron")
    elif fin_yard>169 and fin_yard<180:
        print("You should hit your 7 iron")
    elif fin_yard>179 and fin_yard<190:
        print("You should hit your 6 iron")
    elif fin_yard>189 and fin_yard<200:
        print("You should hit your 5 iron")
    elif fin_yard>199 and fin_yard<210:
        print("You should hit your 4 iron")
    elif fin_yard>209:
        print("You should hit your 3 wood")

def  dist_100(fin_yard, temp_adj_yard):
    if hole == 1:
        fin_yard = temp_adj_yard + 3
    elif hole == 2:
        fin_yard  = temp_adj_yard - 3
    elif hole == 3:
        fin_yard = temp_adj_yard - 3
    elif hole == 4:
        fin_yard = temp_adj_yard - 3
    elif hole == 5:
        fin_yard = temp_adj_yard - 3
    elif hole == 6:
        fin_yard  = temp_adj_yard + 3
    elif hole == 7:
        fin_yard  = temp_adj_yard + 3
    elif hole == 8:
        fin_yard  = temp_adj_yard + 6
    elif hole == 9:
        fin_yard = temp_adj_yard - 6
    elif hole == 10:
        fin_yard  = temp_adj_yard + 0
    elif hole == 11:
        fin_yard  = temp_adj_yard + 0
    elif hole == 12:
        fin_yard  = temp_adj_yard + 6
    elif hole == 13:
        fin_yard  = temp_adj_yard - 3
    elif hole == 14:
        fin_yard  = temp_adj_yard + 3
    elif hole == 15:
        fin_yard  = temp_adj_yard - 3
    elif hole == 16:
        fin_yard  = temp_adj_yard + 6
    elif hole == 17:
        fin_yard  = temp_adj_yard + 0
    elif hole == 18:
        fin_yard  = temp_adj_yard - 6
    
    print("Your final adjusted yardage is: ", fin_yard)
    
    if fin_yard<90:
        print("You should hit your lob wedge")
    elif fin_yard>89 and fin_yard<110:
        print("You should hit your sand wedge")
    elif fin_yard>109 and fin_yard<130:
        print("You should hit your gap wedge")
    elif fin_yard>129 and fin_yard<145:
        print("You should hit your pitching wedge")
    elif fin_yard>144 and fin_yard<160:
        print("You should hit your 9 iron")
    elif fin_yard>159 and fin_yard<170:
        print("You should hit your 8 iron")
    elif fin_yard>169 and fin_yard<180:
        print("You should hit your 7 iron")
    elif fin_yard>179 and fin_yard<190:
        print("You should hit your 6 iron")
    elif fin_yard>189 and fin_yard<200:
        print("You should hit your 5 iron")
    elif fin_yard>199 and fin_yard<210:
        print("You should hit your 4 iron")
    elif fin_yard>209:
        print("You should hit your 3 wood")

def  dist_50(fin_yard, temp_adj_yard):
    if hole == 1:
        fin_yard = temp_adj_yard + 3
    elif hole == 2:
        fin_yard  = temp_adj_yard- 3
    elif hole == 3:
        fin_yard = temp_adj_yard - 3
    elif hole == 4:
        fin_yard = temp_adj_yard + 0
    elif hole == 5:
        fin_yard = temp_adj_yard - 3
    elif hole == 6:
        fin_yard  = temp_adj_yard + 3
    elif hole == 7:
        fin_yard  = temp_adj_yard + 6
    elif hole == 8:
        fin_yard  = temp_adj_yard + 6
    elif hole == 9:
        fin_yard = temp_adj_yard - 3
    elif hole == 10:
        fin_yard  = temp_adj_yard + 0
    elif hole == 11:
        fin_yard  = temp_adj_yard + 0
    elif hole == 12:
        fin_yard  = temp_adj_yard + 6
    elif hole == 13:
        fin_yard  = temp_adj_yard - 3
    elif hole == 14:
        fin_yard  = temp_adj_yard + 0
    elif hole == 15:
        fin_yard  = temp_adj_yard - 0
    elif hole == 16:
        fin_yard  = temp_adj_yard + 6
    elif hole == 17:
        fin_yard  = temp_adj_yard + 0
    elif hole == 18:
        fin_yard  = temp_adj_yard - 3
    
    print("Your final adjusted yardage is: ", fin_yard)

    if fin_yard<90:
        print("You should hit your lob wedge")
    elif fin_yard>89 and fin_yard<110:
        print("You should hit your sand wedge")
    elif fin_yard>109 and fin_yard<130:
        print("You should hit your gap wedge")
    elif fin_yard>129 and fin_yard<145:
        print("You should hit your pitching wedge")
    elif fin_yard>144 and fin_yard<160:
        print("You should hit your 9 iron")
    elif fin_yard>159 and fin_yard<170:
        print("You should hit your 8 iron")
    elif fin_yard>169 and fin_yard<180:
        print("You should hit your 7 iron")
    elif fin_yard>179 and fin_yard<190:
        print("You should hit your 6 iron")
    elif fin_yard>189 and fin_yard<200:
        print("You should hit your 5 iron")
    elif fin_yard>199 and fin_yard<210:
        print("You should hit your 4 iron")
    elif fin_yard>209:
        print("You should hit your 3 wood")

if yard <=250 and yard >=151:
    dist_200(fin_yard, temp_adj_yard)
elif yard<=150 and yard >=101:
    dist_150(fin_yard, temp_adj_yard)
elif yard <=100 and yard >= 51:
    dist_100(fin_yard, temp_adj_yard)
elif yard <= 50 and yard>= 1:
    dist_50(fin_yard, temp_adj_yard)