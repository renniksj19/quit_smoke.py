"""
Please follow my website for more programming projects and articles.
URL: https://newfiecoder.wordpress.com/
Licensed under MIT License
"""



# Total cigarettes not smoked = days quit smoking * how many you smoked a day
# Money saved = packs smoked a day * price of one pack
from datetime import datetime
from datetime import date
import math

"""
1. Ask when they quit smoking
2. Ask how many cigarettes they smoke a day
3. Ask how many packs a day
4. Ask price of one pack
5. Total cost = packs a day * price of one pack
6. Print number of days total quit
7. Output number of cigarettes not smoked
   Where number of cigarettes = days quit * number smoke
"""

# Date format
format_string = "%Y-%m-%d"

# Get today's date
today = date.today()

# Ask user input data
str_date_quit = input("Enter date you quit in YYYY-MM-DD Format => ")
str_cigs_smoked = input("Enter number of cigarettes you smoked a day => ")
str_price_pack = input("Enter the price of one pack ==> ")
str_smokes_in_pack = input("Enter number of cigarettes in a pack ==> ")

# Calculate number of days quit
quit_date = datetime.strptime(str_date_quit, format_string).date()
days_quit = str(today - quit_date)
days_quit_out = days_quit.split(',')
print("# Days Quit = "+str(days_quit_out[0])) # output number of days quit
days_quit = float(days_quit.split(" ")[0])

# output years, months and weeks
weeks = 0
if days_quit == 7:
	print("\t** That's one week punched! :) **")
elif days_quit > 7:
	weeks = days_quit / 7.0
	if weeks == 1:
		print("\t** That's one week punched! :) **")
	else:
		print("\t** That's "+str(int(math.floor(weeks)))+" weeks! :O **")

if weeks == 4.34524:
	print("\t** That's one month punched! :D **")
elif weeks >= 4.34524:
	months = weeks / 4.34524
	if weeks == 4.34524:
		print("\t** That's one month punched! ^_^ **")
	else:
		print("\t** That's "+str(int(months))+" months! :O **")
if days_quit == 365.25:
	print("\t************************************")
	print("\t******1 YEAR QUIT CONGRATS!*******")
	print("\t************************************")
elif days_quit > 365.25:
	years = days_quit / 365.25
	years = math.floor(years)
	years = int(years)
	print("\t************************************")
	print("\t******"+str(years)+" YEARS QUIT CONGRATS!*******")
	print("\t************************************")

# Calculate money saved
# Get number of packs a day smoked
num_packs = float(str_cigs_smoked) / float(str_smokes_in_pack)
num_packs = math.ceil(num_packs)
formatted_pack = "{:.1f}".format(num_packs)
print("# of Packs a Day = "+formatted_pack)
money_saved = num_packs * float(str_price_pack) * days_quit
money_saved_str = "{:.2f}".format(money_saved)
print("Money Saved $"+money_saved_str)

"""
License:

Copyright 2021 https://newfiecoder.wordpress.com/

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR 
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
