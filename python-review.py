"""
[1] Sleep in:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

Example:
sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""

def spleep_in(weekday, vacation):
    if not (weekday) or vacation:
        return True
    else:
        return False   
 
# or
def spleep_in2(weekday,vacation):
    return(not weekday or vacation)


"""
[2] Diff21

Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

Example:
diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""
def diff21(n):
  if n > 21:
    return 2 * (n - 21)
  else:
    return 21 - n
