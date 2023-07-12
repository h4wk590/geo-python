
''' This function stores a temp_fahrenheit variable
    to hold the value of the temperature to convert.
    It returns the converted temperature'''
def fahr_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) * 5/9


''' Function defined as temp_classifier
    and takes a parameter to hold the temperature value
    goes through conditions to return an int value as 
    the temp_celsius'''
def temp_classifier(temp_celsius):
    if temp_celsius < -2:
        return int(0) # returns value from condition as int
    elif temp_celsius >= -2 and temp_celsius < 2:
        return int(1)
    elif temp_celsius >= 2 and temp_celsius < 15:
        return int(2)
    else: 
        return int(3) # once all other conditions are met it will return int of 3