#Kate Anderson U21933376
#Victoria Alvarez U25145694
#Driver: Victoria
#Navigator: Kate

#This program stores morse code translation in a dictionary. It takes in a string from a user and translates the string back in morse code

morse = { #dictionary called morse is created storing the morse code translation
    ' ' : ' ',
    ',' : '--..--',
    '.' : '.-.-.-',
    '?' : '..--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.',
    'A' : '.-',
    'B' : '-..',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '. ...',
    'I' : '. .',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.---.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
     'a' : '.-',
    'b' : '-..',
    'c' : '-.-.',
    'd' : '-..',
    'e' : '.',
    'f' : '..-.',
    'g' : '--.',
    'h' : '. ...',
    'i' : '. .',
    'j' : '.---',
    'k' : '-.-',
    'l' : '.-..',
    'm' : '--',
    'n' : '-.',
    'o' : '---',
    'p' : '.---.',
    'q' : '--.-',
    'r' : '.-.',
    's' : '...',
    't' : '-',
    'u' : '..-',
    'v' : '...-',
    'w' : '.--',
    'x' : '-..-',
    'y' : '-.--',
    'z' : '--..'
}

new_string = ' ' #initialize new string which will hold the translation
string = input('Enter the string to be converted to Morse code: ' ) #takes in string from user

for character in string: #for loop iterates over each character in the string
    new_string += morse[character] #adds each character of translation into new string

print (new_string) #prints the morse code translation
    
    
    
    
