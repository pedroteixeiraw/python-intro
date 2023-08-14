"""
Sleep in:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

example:
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def spleep_in(weekday, vacation):
    if not (weekday) or vacation:
        return True
    else:
        return False   

"""
Another option: 

def spleep_in(weekday,vacation):
    return(not weekday or vacation)
"""
