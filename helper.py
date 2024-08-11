def unit_calc(number_of_days):
    units = "minutes"
    minutes_in_days = 60 * number_of_days * 24
    second_in_days = minutes_in_days * 60
    #print (f"number of {units} days in {number_of_days} is {minutes_in_days}")
    try:
        if isinstance(number_of_days,int):
            if number_of_days > 0 and number_of_days < 365 :
                return f"number of {units} days in {number_of_days} is {minutes_in_days}"
            else:
                 return f"number of days entered is {number_of_days} out of a range , the day range is  from 1 and 365"
        else:
            return f"number of days entered {number_of_days} is not a valid integer"
    except:
            return f"something is wrong with input {number_of_days}"

user_input_message = "I will be called in main and the other python file"
