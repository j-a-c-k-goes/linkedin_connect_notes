'''
    • take name as an input OR generate message for list of names
    • generate connect message
    • (example: Hey Ikenna! Connecting with you from GSUProgClub discord.) 
    • store message in let's connect array
'''
''' module imoprt '''
import pyperclip
''' store names '''
names = [] # 'Furqann', 'Jenny', 'Chloe', 'Ravier', 'Faizon', 'Bonk', 'Karan'

''' store connect messages '''
connect_messages = [] # 'Furqann', 'Jenny', 'Chloe', 'Ravier', 'Faizon', 'Bonk', 'Karan'

''' user input function '''
def input_name():
	name = str(input('enter name of person to connect with: '))
	return name
''' input place of interaction ''' 
def place_of_interaction():
	poi = str(input('enter location, circumstance, et al. where you met this person (or people): '))
	return poi
''' generate my message '''
def generate_message(name, place_of_interaction):
	message = f'Hey {name}! Connecting with you from {place_of_interaction}.'
	print(f'your message\t{message}')
	return message
''' print program options '''
def program_options():
	print ('--- welcome to my let\'s connect program for LinkedIn! ---')
	print('OPTIONS')
	print('1\t\ti want to connect with one person')
	print('2\t\ti need to connect with multiple people')
''' on run '''
if __name__ == '__main__':
    program_options()
    print('------')
    option_choice = int(input('enter number (1 or 2) to represent your option choice: '))
    
    if option_choice == '':
    	print('no option selected. exiting')
    	exit()

    elif option_choice == 1:
    	name = input_name()
    	poi = place_of_interaction()
    	message = generate_message(name,poi)
    	print('--- copying to clipboard ---')
    	pyperclip.copy(message)

    elif option_choice == 2:
    	poi = place_of_interaction()

    	print('--- enter names of connections ---')
    	n_names = int(input('enter how many people you are aiming to connect with? '))
    	
    	print('--- saving your entries ---')
    	for i, index in enumerate(range(n_names)):
    		print(f'--- person {index + 1} ---')
    		name = input_name()
    		names.append(name)

    	print('--- building correspondence ---')
    	for name in names:
    		connect_messages.append(generate_message(name, poi))

    	print('--- writing correspondence to text file ---')
    	for message in connect_messages:
    		with open('generated_messages.txt', 'a') as file:
    			file.write(message)

    else: 
    	print('you did not enter a valid option. please restart program.')
    	exit()