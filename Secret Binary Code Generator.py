# Disclaimer: Copyright code by Samarth Talawar, all rights reserved...

print("Decoding is not case sensitive\nEnter numbers in words\nno special characters... ")
m = input("Enter text :      ")

int_convertor = {"A":"1", "B":"2", "C":"3", "D":"4", "E":"5", "F":"6", "G":"7", "H":"8", "I":"9", "J":"10", 
"K":"11", "L":"12", "M":"13", "N":"14", "O":"15", "P":"16", "Q":"17", "R":"18", "S":"19", "T":"20", "U":"21", 
"V":"22", "W":"23", "X":"24", "Y":"25", "Z":"26", "a":"1", "b":"2", "c":"3", "d":"4", "e":"5", "f":"6", 
"g":"7","h":"8", "i":"9", "j":"10", "k":"11", "l":"12","m":"13", "n":"14", "o":"15", "p":"16", "q":"17", 
"r":"18","s":"19", "t":"20", "u":"21", "v":"22", "w":"23", "x":"24", "y":"25", "z":"26"," ":" "}

def convert(m): 
	convertor = "" 
	for letter in m: 
		if letter in "0123456789": 
			convertor = convertor + letter + " "
		else : 
			convertor = convertor + int_convertor[letter] + " "

	return convertor

k = convert(m)

def bin_convertor(n): 
	bin_con = "" 
	for letter in n:
		if letter in "0123456789":		
			bin_con = bin_con + bin(int(letter)) + "."
		else:
			bin_con = bin_con + "__"

	return bin_con

r = bin_convertor(k)

print(f"Code for {m} is:\n{r}")