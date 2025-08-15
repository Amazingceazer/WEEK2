# This python script acts as a micro-wave
 import time
 print(
 '''****
 Welcome to Cohort III Micro-wave App
 ********
 Open the micro-wave
 2. Put the Rice
 3. Set time''')
 customer = {}
 name = input("Enter your name: \n>>>")
 customer["name"] = name
 time_to_micro_wave = input("Duration: \n>>>")
 convert_to_int=float (time_to_micro_wave)
 customer["duration"] = convert_to_int
 price_to_pay = convert_to_int * 1000
 customer["amount"] = price_to_pay
 print("You are charged: N", price_to_pay, "only")
 print(f"Your Rice will read in {convert_to_int} min(s) {name}")
 print("4. I will let you know when it is ready...")
 minutes_in_seconds =60
 time.sleep(convert_to_int * minutes_in_seconds)
 print("5. Your food is ready.")
 customer.append (customer)
 print(customer)
