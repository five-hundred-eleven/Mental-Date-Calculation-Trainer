#!/usr/bin/env python

import sys, os
import random

random.seed()

def get_month(monthNumber):
	months = [	('January', 6, 31, "WINTER"),
				('February', 2, 28, "February is month #__"),
				('March', 2, 31, "March __ the beat"),
				('April', 5, 30, "APRIL & FOOLS"),
				('May', 0, 31, "Cinco de May__"),
				('June', 3, 30, "June BUG"),
				('July', 5, 31, "__works"),
				('August', 1, 31, "A__ Steak Sauce at the BBQ"),
				('September', 4, 30, "FALL"),
				('October', 6, 31, "__ or treat!"),
				('November', 2, 30, "__rkey"),
				('December', 4, 31, "LAST & XMAS") ]
	if monthNumber > 12 or monthNumber < 1:
		return False
	else:
		return months[monthNumber - 1]

def yearcode(year):
	yearCodes = {	0	:	0,
					4	:	5,
					8	:	3,
					12	:	1,
					16	:	6,
					20	:	4,
					24	: 	2
				}
	centuryCodes = [0, 1, 3, 5]

	year = year % 100
	centuryCode = centuryCodes[(year / 100) % 4]

	nearestLeap = year - (year % 4)
	r = year % 4
	
	if nearestLeap % 12 == 0:
		code = (nearestLeap / 12) % 7
	else:
		code = yearCodes[nearestLeap % 28]

	return code + r + centuryCode
		

def weekday(month, day, year):
	weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	if type(month) == type(''):
		month_names = [m[0] for m in months]
		month = month_names.index(month) + 1
	else:
		pass

	monthCode = get_month(month)[1]
	yearCode = yearcode(year)
	dayCode = ((day - 1) % 7) + 1
	
	return weekdays[(monthCode + yearCode + dayCode) % 7]

def walkthrough(month, day, year):
	weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	if type(month) == type(''):
		month_names = [m[0] for m in months]
		month = month_names.index(month) + 1
	else:
		pass

	tries = 0
	month = get_month(month)
	print "What is the month code for " + month[0] + "?" 
	while(True):
		response = input()
		if type(response) != type(1):
			print "Huh? We need a number. (Enter a decimal digit)"
		elif response == month[1]:
			print "Good."
			break
		elif tries == 1:
			print "Hint: " + month[3]
			tries = tries + 1
		elif tries == 2:
			print "Try once more."
		else:
			print "The month code for " + month[0] + " is " + str(month[1]) + "."
	
	print "Now we'll find the year code for " + str(year) + "."
	print "What's the closest previous leap year?"
	nearestLeap = year - (year % 4)
	if nearestLeap % 100 == 0 and nearestLeap % 400 != 0:
		nearestLeap = nearestLeap - 4
	else:
		pass
	tries = 0
	while(True):
		response = input()
		if type(response) != type(1):
			print "Huh? We need a year in decimal form, e.g. 1492"
			continue
		elif response == nearestLeap:
			print "Good!"
			break
		elif tries > 2:
			print "The nearest leap year is " + str(nearestLeap) + ". You should review the rules for leap years."
			break
		elif response % 4 != 0:
			print "Remember, leap years are multiples of 4."
		elif response > nearestLeap:
			print "Remember, we want the nearest PREVIOUS leap year."
		elif response % 100 == 0:
			print "Remember, multiples of 100 are only leap years if they're also multiples of 400."
		elif nearestLeap % 400 == 0:
			print "The rule that multiples of 100 aren't leap years DOES NOT HOLD for multiples of 400."
		elif (nearestLeap + 4) % 100 != 0 and (response + 4) % 100 != 0 and abs(nearestLeap - response) > 4:
			print "The nearest leap year is usually within 4 years."
		tries = tries + 1
	
	print "What is the code for " + str(nearestLeap) + "?"
	tries = 0

	


	monthCode = month[1]
	yearCode = yearcode(year)
	dayCode = ((day - 1) % 7) + 1
	
	return weekdays[(monthCode + yearCode + dayCode) % 7]
	
while True:
	year= random.randint(1600, 2100)
	if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
		leapyear = True 
	else:
		leapyear = False

	monthNumber = random.randint(1, 12)
	month = get_month(monthNumber)

	if leapyear and month[0] == 'February':
		daysInMonth = 29
	else:
		daysInMonth = month[2]

	day = random.randint(1, daysInMonth)

	try:
		response = raw_input( "What day of the week is " + month[0] + " " + str(day) + ", " + str(year) + "?\n" )
	except EOFError:
		print ''
		break

	response = response.lower()
	if response == '-1':
		break
	elif response == 'help' or response == 'h':
		walkthrough(monthNumber, day, year)
	elif response != weekday(monthNumber, day, year):
		print 'Nope...'
		walkthrough(monthNumber, day, year)
	else:
		print 'correct!'

