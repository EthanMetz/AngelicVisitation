print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.
#drawioUhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
#Ifs go under what they corralate with. But what their outcome would be if true gets an indent (on the next line)
choice1 = input('''You\'re an adventurer travelling through a bueatiful dreamland where every possible place and realm is
instantly imaginable and all that they contain flow to your. Type: "stroll" to stroll through the land. ---> ''').lower()
if choice1 == "stroll":
    choice2 = input('''You\'ve come to a lake, all around you are the beautiful green hills, and forests, but you\'ve settled down near this painting-esque
lake. It begins to glow. Rivers of life come out of it onto the bank shore, and surge across the ground into you. You take it
all in and decide to explore the forest, where Wisdom, Might, Goodness and mercy can be found. Who do you want to be blessed by, Wisdom, or Might?

Enter one of their names to recieve an impartation of knowledge. ---> ''').lower()
    
    if choice2 == "wisdom":
        wants_might = input('''The Spirit of Wisdom turns to you and says "My son, love is the greatest of all. Love was not created by God for love is God. From the
moment God was, love was. To deny love is to deny the entire universe; it is to deny God Himself, His purpose, His heart, and the very core of His being." You feel a
melding of your spirit with the spirit of wisdom and gain the knowledge that love seeks to understand that it may heal all that is broken.
                                
Type "might" to hear from might ---> ''').lower()
        
        if wants_might == "might":
            print('''"The Spirit of might speaks. "“To be filled with joy is not to be skipping through the valley shouting
‘woohoo’ all day. Though we love  it when people are affected in such a wonderful way, that is not what we refer to.
Joy is a PERMANENT state of gratitude.
It is a disciplined awareness of all that is good in your life. Absent gratefulness, a man will never see 
the hand of God or angel at work. You spend the rest of the day taking in what the Spirit said, and relaxing outside. "''')
        
        
        
    elif choice2 == "might":
        
    
        wants_wisdom = input('''The Spirit of Might speaks: “To be filled with joy is not to be skipping through the valley shouting ‘woohoo’ all day.
Though we love it when people are affected in such a wonderful way, that is not what we refer to. Joy is a permanent state of gratitude.
It is a disciplined awareness of all that is good in your life. Absent gratefulness, a man will never see 
the hand of God or angel at work" If you\d like you can still type "wisdom" to hear from Wisdom. ---> ''').lower()
        if wants_wisdom == "wisdom":
            print('''The Spirit of Wisdom turns to you and says "My son, love is the greatest of all. Love was not created by God for love is God.
From the moment God was, love was. To deny love is to deny the entire universe; it is to deny God Himself, His purpose, His heart, and the very core of His being."
You feel a melding of your spirit with the spirit of wisdom and gain the knowledge that love seeks to understand that it may heal all that is broken. You spend the rest of the day relaxing.''')
        

