from colorama import Fore


def print_happy():
	happy=\
"""
───█───▄▀█▀▀█▀▄▄───▐█──────▄▀█▀▀█▀▄▄
──█───▀─▐▌──▐▌─▀▀──▐█─────▀─▐▌──▐▌─█▀
─▐▌──────▀▄▄▀──────▐█▄▄──────▀▄▄▀──▐▌
─█────────────────────▀█────────────█
▐█─────────────────────█▌───────────█
▐█─────────────────────█▌───────────█
─█───────────────█▄───▄█────────────█
─▐▌───────────────▀███▀────────────▐▌
──█──────────▀▄───────────▄▀───────█
───█───────────▀▄▄▄▄▄▄▄▄▄▀────────█

"""


	print( Fore.RED+happy)

	print("####---Enter 'q' to exit the game---###")

print(print_happy())

while True: 
	try:
		firstNum = input("What is your first number")
		if firstNum == 'q':
			break

		secondNum = input("What is you second number")
		if secondNum =='q':
			break

	except ValueError:
		print ("Try again...!") 

	else:
		total = int(firstNum) / int(secondNum) *2
		print (f" the total -----> {total} ")


