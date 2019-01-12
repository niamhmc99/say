
#converting 2 lists into one dictionary object
num2words = ({1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',\
                 6: 'six', 7: 'Seven', 8:'eight', 9:'nine', 10: 'ten', \
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
                15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', \
                19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', \
                50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', \
                90: 'ninety', 0: 'zero'})


def say(number):
    if number == 0:
        return "zero" 
    try:
        return (num2words[number])
    except KeyError:
        try:
            return (num2words[number-number%10] + num2words[number%10].lower())
        except KeyError:
            return ('Number out of range')

def say_error(number):
    if number >= 1e12:
        raise ValueError

    if number < 0:
        raise ValueError
    
    return say_error(number)

    

    


   