'''
This is the code that will control the hands-free switching off/on of light bulbs

x. The Sound sensor input on the microcontroller has to be confirmed

x. Take readings from the sensor so you can get the actual sequence(if clapping) or intensity(loudness of snapping fingers) and both options too
   (the date.time module can be used to create a time frame condition for sound repitition)


x. now create the logic using the generated sequence/intensity and the output has to be the switch

#CONDITIONS
-if two sounds(of clapping intensity) come in the space of two seconds(Thus, the two claps): Turn on/off.
-(after first test)if power comes on and the bulb is on..after ten seconds, switch beeps, if ten seconds after the switch beeps there's no clap, bulb goes off/

#TIPS
-ignore fan sounds.
-claps cannot exceed a certain loudness. somewhere in between the loudness of fan and < loudness of fan.
-precode microprocessor for commercial use after this has been concluded.
'''


