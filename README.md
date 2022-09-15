# monopoly_junior

```
$ python3 monopoly_junior.py -h
usage: monopoly_junior.py [-h] [-p PLAYERS [PLAYERS ...]] [-m] [-v] [-g GAMES]

optional arguments:
  -h, --help            show this help message and exit
  -p PLAYERS [PLAYERS ...], --players PLAYERS [PLAYERS ...]
                        2-4 players
  -m, --monopoly-rules  This will enable regular Monopoly rules (not "Monopoly Junior")
  -v, --verbose
  -g GAMES, --games GAMES
                        The number of games to simulate

$ python3 monopoly_junior.py -p Chad Katie Tyree Lysol -v
##########Lysol has $31 and properties []
Lysol rolled a 4. Lysol is now at board spot 4
Lysol has landed on Chance
Lysol drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Orange properties: (Longview Ferris Wheel, Bend 'Em Bumper Cars)
Lysol is getting a free ticket booth on Longview Ferris Wheel
##########Chad has $31 and properties []
Chad rolled a 1. Chad is now at board spot 1
Chad has landed on Chance
Chad drew the Go to the Fireworks and PAY $2 Chance card
Chad is going to the spot "Pay $2 to see the Fireworks"
Chad has landed on Pay $2 to see the Fireworks
Chad must Pay $2 to see the Fireworks
##########Katie has $31 and properties []
Katie rolled a 4. Katie is now at board spot 4
Katie has landed on Chance
Katie drew the Go to Go - Collect $2 allowance as you pass Chance card
Katie is going to the spot "Go"
Katie passed Go. Katie will collect $2
Katie has landed on Go
##########Tyree has $31 and properties []
Tyree rolled a 6. Tyree is now at board spot 6
Tyree has landed on Safari Cruise
Tyree bought Safari Cruise for $2
##########Lysol has $31 and properties [Longview Ferris Wheel]
Lysol rolled a 3. Lysol is now at board spot 7
Lysol has landed on Cartoon Village
Lysol bought Cartoon Village for $2
##########Chad has $29 and properties []
Chad rolled a 5. Chad is now at board spot 13
Chad has landed on Green Line Railroad
Chad is rolling again...
##########Chad has $29 and properties []
Chad rolled a 5. Chad is now at board spot 18
Chad has landed on Mystery Mansion
Chad bought Mystery Mansion for $3
##########Katie has $33 and properties []
Katie rolled a 4. Katie is now at board spot 4
Katie has landed on Chance
Katie drew the Take a Ride on the Green Line Railroad Chance card
Katie is going to the spot "Green Line Railroad"
Katie has landed on Green Line Railroad
Katie is rolling again...
##########Katie has $33 and properties []
Katie rolled a 2. Katie is now at board spot 15
Katie has landed on Bend 'Em Bumper Cars
Katie bought Bend 'Em Bumper Cars for $3
##########Tyree has $29 and properties [Safari Cruise]
Tyree rolled a 4. Tyree is now at board spot 10
Tyree has landed on Lunch
##########Lysol has $29 and properties [Cartoon Village, Longview Ferris Wheel]
Lysol rolled a 2. Lysol is now at board spot 9
Lysol has landed on Chance
Lysol drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Blue properties: (Supersonic Space Flight, Echo Canyon Coaster)
Lysol is getting a free ticket booth on Supersonic Space Flight
##########Chad has $26 and properties [Mystery Mansion]
Chad rolled a 2. Chad is now at board spot 20
Chad has landed on Chance
Chad drew the Go to the Echo Canyon Coaster Chance card
Chad is going to the spot "Echo Canyon Coaster"
Chad has landed on Echo Canyon Coaster
Chad bought Echo Canyon Coaster for $5
##########Katie has $30 and properties [Bend 'Em Bumper Cars]
Katie rolled a 3. Katie is now at board spot 18
Katie has landed on Mystery Mansion
Katie must pay Chad $3 because Chad owns Mystery Mansion
##########Tyree has $29 and properties [Safari Cruise]
Tyree rolled a 5. Tyree is now at board spot 15
Tyree has landed on Bend 'Em Bumper Cars
Tyree must pay Katie $3 because Katie owns Bend 'Em Bumper Cars
##########Lysol has $29 and properties [Cartoon Village, Longview Ferris Wheel, Supersonic Space Flight]
Lysol rolled a 6. Lysol is now at board spot 15
Lysol has landed on Bend 'Em Bumper Cars
Lysol must pay Katie $3 because Katie owns Bend 'Em Bumper Cars
##########Chad has $24 and properties [Mystery Mansion, Echo Canyon Coaster]
Chad rolled a 4. Chad is now at board spot 3
Chad passed Go. Chad will collect $2
Chad has landed on Sweet Treats Snack Shack
Chad bought Sweet Treats Snack Shack for $1
##########Katie has $33 and properties [Bend 'Em Bumper Cars]
Katie rolled a 6. Katie is now at board spot 24
Katie has landed on Pay $2 For the Water Show
Katie must Pay $2 For the Water Show
##########Tyree has $26 and properties [Safari Cruise]
Tyree rolled a 1. Tyree is now at board spot 16
Tyree has landed on Free Time
##########Lysol has $26 and properties [Cartoon Village, Longview Ferris Wheel, Supersonic Space Flight]
Lysol rolled a 6. Lysol is now at board spot 21
Lysol has landed on Blue Line Railroad
Lysol is rolling again...
##########Lysol has $26 and properties [Cartoon Village, Longview Ferris Wheel, Supersonic Space Flight]
Lysol rolled a 5. Lysol is now at board spot 26
Lysol has landed on Go To Lunch - Pay $3
Lysol must Go To Lunch - Pay $3
Lysol does not collect $2
##########Chad has $25 and properties [Sweet Treats Snack Shack, Mystery Mansion, Echo Canyon Coaster]
Chad rolled a 1. Chad is now at board spot 4
Chad has landed on Chance
Chad drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Blue properties: (Supersonic Space Flight, Echo Canyon Coaster)
##########Katie has $31 and properties [Bend 'Em Bumper Cars]
Katie rolled a 4. Katie is now at board spot 28
Katie has landed on Whirlwind Water Slide
Katie bought Whirlwind Water Slide for $4
##########Tyree has $26 and properties [Safari Cruise]
Tyree rolled a 3. Tyree is now at board spot 19
Tyree has landed on Nitro Speed Track
Tyree bought Nitro Speed Track for $3
##########Lysol has $23 and properties [Cartoon Village, Longview Ferris Wheel]
Lysol rolled a 1. Lysol is now at board spot 11
Lysol has landed on Palace Of Mirrors Carousel
Lysol bought Palace Of Mirrors Carousel for $2
##########Chad has $25 and properties [Sweet Treats Snack Shack, Mystery Mansion, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 6. Chad is now at board spot 10
Chad has landed on Lunch
##########Katie has $27 and properties [Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 3. Katie is now at board spot 31
Katie has landed on Echo Canyon Coaster
Katie must pay Chad $10 because Chad owns both Blue properties
##########Tyree has $23 and properties [Safari Cruise, Nitro Speed Track]
Tyree rolled a 4. Tyree is now at board spot 23
Tyree has landed on Ultimate Idol Grandstand
Tyree bought Ultimate Idol Grandstand for $4
##########Lysol has $21 and properties [Cartoon Village, Palace Of Mirrors Carousel, Longview Ferris Wheel]
Lysol rolled a 1. Lysol is now at board spot 12
Lysol has landed on Clown Around Fun House
Lysol bought Clown Around Fun House for $2
##########Chad has $35 and properties [Sweet Treats Snack Shack, Mystery Mansion, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 4. Chad is now at board spot 14
Chad has landed on Longview Ferris Wheel
Chad must pay Lysol $3 because Lysol owns Longview Ferris Wheel
##########Katie has $17 and properties [Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 1. Katie is now at board spot 0
Katie passed Go. Katie will collect $2
Katie has landed on Go
##########Tyree has $19 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 5. Tyree is now at board spot 28
Tyree has landed on Whirlwind Water Slide
Tyree must pay Katie $4 because Katie owns Whirlwind Water Slide
##########Lysol has $22 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Longview Ferris Wheel]
Lysol rolled a 4. Lysol is now at board spot 16
Lysol has landed on Free Time
##########Chad has $32 and properties [Sweet Treats Snack Shack, Mystery Mansion, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 2. Chad is now at board spot 16
Chad has landed on Free Time
##########Katie has $23 and properties [Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 1. Katie is now at board spot 1
Katie has landed on Chance
Katie drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Purple properties: (Penny Arcade, Sweet Treats Snack Shack)
Katie is getting a free ticket booth on Penny Arcade
##########Tyree has $15 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 3. Tyree is now at board spot 31
Tyree has landed on Echo Canyon Coaster
Tyree must pay Chad $10 because Chad owns both Blue properties
##########Lysol has $22 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Longview Ferris Wheel]
Lysol rolled a 4. Lysol is now at board spot 20
Lysol has landed on Chance
Lysol drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Red properties: (Mystery Mansion, Nitro Speed Track)
Lysol is getting a free ticket booth on Nitro Speed Track
Tyree owned Nitro Speed Track before Lysol took it
##########Chad has $42 and properties [Sweet Treats Snack Shack, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 3. Chad is now at board spot 19
Chad has landed on Nitro Speed Track
Chad must pay Tyree $3 because Tyree owns Nitro Speed Track
##########Katie has $23 and properties [Penny Arcade, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 4. Katie is now at board spot 5
Katie has landed on Yellow Line Railroad
Katie is rolling again...
##########Katie has $23 and properties [Penny Arcade, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 4. Katie is now at board spot 9
Katie has landed on Chance
Katie drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Orange properties: (Longview Ferris Wheel, Bend 'Em Bumper Cars)
##########Tyree has $8 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 5. Tyree is now at board spot 4
Tyree passed Go. Tyree will collect $2
Tyree has landed on Chance
Tyree drew the Go to the Whirlwind Water Slide Chance card
Tyree is going to the spot "Whirlwind Water Slide"
Tyree has landed on Whirlwind Water Slide
Tyree must pay Katie $4 because Katie owns Whirlwind Water Slide
##########Lysol has $22 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 6. Lysol is now at board spot 26
Lysol has landed on Go To Lunch - Pay $3
Lysol must Go To Lunch - Pay $3
Lysol does not collect $2
##########Chad has $39 and properties [Sweet Treats Snack Shack, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 6. Chad is now at board spot 25
Chad has landed on Chance
Chad drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Green properties: (Free Zone Drop, Whirlwind Water Slide)
Chad is getting a free ticket booth on Free Zone Drop
##########Katie has $27 and properties [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 3. Katie is now at board spot 12
Katie has landed on Clown Around Fun House
Katie must pay Lysol $4 because Lysol owns both Pink properties
##########Tyree has $6 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 1. Tyree is now at board spot 29
Tyree has landed on Red Line Railroad
Tyree is rolling again...
##########Tyree has $6 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 3. Tyree is now at board spot 0
Tyree passed Go. Tyree will collect $2
Tyree has landed on Go
##########Lysol has $23 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 4. Lysol is now at board spot 14
Lysol has landed on Longview Ferris Wheel
Lysol must pay Katie $6 because Katie owns both Orange properties
##########Chad has $39 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 4. Chad is now at board spot 29
Chad has landed on Red Line Railroad
Chad is rolling again...
##########Chad has $39 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 2. Chad is now at board spot 31
Chad has landed on Echo Canyon Coaster
Chad already owns Echo Canyon Coaster
##########Katie has $29 and properties [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 4. Katie is now at board spot 16
Katie has landed on Free Time
##########Tyree has $8 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 2. Tyree is now at board spot 2
Tyree has landed on Penny Arcade
Tyree must pay Katie $1 because Katie owns Penny Arcade
##########Lysol has $17 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 1. Lysol is now at board spot 15
Lysol has landed on Bend 'Em Bumper Cars
Lysol must pay Katie $6 because Katie owns both Orange properties
##########Chad has $39 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 5. Chad is now at board spot 4
Chad passed Go. Chad will collect $2
Chad has landed on Chance
Chad drew the Take a Ride on the Red Line Railroad Chance card
Chad is going to the spot "Red Line Railroad"
Chad has landed on Red Line Railroad
Chad is rolling again...
##########Chad has $41 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 5. Chad is now at board spot 2
Chad passed Go. Chad will collect $2
Chad has landed on Penny Arcade
Chad must pay Katie $1 because Katie owns Penny Arcade
##########Katie has $37 and properties [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 1. Katie is now at board spot 17
Katie has landed on Chance
Katie drew the Go to the Water Show and PAY $2 Chance card
Katie is going to the spot "Pay $2 For the Water Show"
Katie has landed on Pay $2 For the Water Show
Katie must Pay $2 For the Water Show
##########Tyree has $7 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 2. Tyree is now at board spot 4
Tyree has landed on Chance
Tyree drew the Free Ticket Booth Chance card
The Free Ticket Booth Chance card is for the Pink properties: (Palace Of Mirrors Carousel, Clown Around Fun House)
Lysol already owns both Pink properties.  Tyree will draw another Chance card
Tyree drew the Go to the Longview Ferris Wheel Chance card
Tyree is going to the spot "Longview Ferris Wheel"
Tyree has landed on Longview Ferris Wheel
Tyree must pay Katie $6 because Katie owns both Orange properties
##########Lysol has $11 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 5. Lysol is now at board spot 20
Lysol has landed on Chance
Lysol drew the Go to the Palace of Mirrors Carousel Chance card
Lysol is going to the spot "Palace Of Mirrors Carousel"
Lysol passed Go. Lysol will collect $2
Lysol has landed on Palace Of Mirrors Carousel
Lysol already owns Palace Of Mirrors Carousel
##########Chad has $42 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 1. Chad is now at board spot 3
Chad has landed on Sweet Treats Snack Shack
Chad already owns Sweet Treats Snack Shack
##########Katie has $41 and properties [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 1. Katie is now at board spot 25
Katie has landed on Chance
Katie drew the Pay $3 and go to Lunch Chance card
Katie is going to the spot "Lunch"
Katie has landed on Lunch
##########Tyree has $1 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 2. Tyree is now at board spot 16
Tyree has landed on Free Time
##########Lysol has $13 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 2. Lysol is now at board spot 13
Lysol has landed on Green Line Railroad
Lysol is rolling again...
##########Lysol has $13 and properties [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Lysol rolled a 1. Lysol is now at board spot 14
Lysol has landed on Longview Ferris Wheel
Lysol must pay Katie $6 because Katie owns both Orange properties
##########Chad has $42 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 1. Chad is now at board spot 4
Chad has landed on Chance
Chad drew the Take a Ride on the Blue Line Railroad Chance card
Chad is going to the spot "Blue Line Railroad"
Chad has landed on Blue Line Railroad
Chad is rolling again...
##########Chad has $42 and properties [Sweet Treats Snack Shack, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Chad rolled a 1. Chad is now at board spot 22
Chad has landed on Fun Food Picnic Grove
Chad bought Fun Food Picnic Grove for $4
##########Katie has $44 and properties [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Katie rolled a 4. Katie is now at board spot 14
Katie has landed on Longview Ferris Wheel
Katie already owns Longview Ferris Wheel
##########Tyree has $1 and properties [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand]
Tyree rolled a 2. Tyree is now at board spot 18
Tyree has landed on Mystery Mansion
Tyree must pay Lysol $3 because Lysol owns Mystery Mansion
Tyree can only pay $1, because they are out of cash!
################################################## Tyree is out of the game! ##################################################
The game is over.  Results:
Lysol finished with $8
Lysol owns spots: [Cartoon Village, Palace Of Mirrors Carousel, Clown Around Fun House, Mystery Mansion]
Chad finished with $38
Chad owns spots: [Sweet Treats Snack Shack, Fun Food Picnic Grove, Free Zone Drop, Supersonic Space Flight, Echo Canyon Coaster]
Katie finished with $44
Katie owns spots: [Penny Arcade, Longview Ferris Wheel, Bend 'Em Bumper Cars, Whirlwind Water Slide]
Tyree finished with $0
Tyree owns spots: [Safari Cruise, Nitro Speed Track, Ultimate Idol Grandstand] 
```
