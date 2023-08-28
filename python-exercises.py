"""
[1] Sleep in:
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

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

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""
def diff21(n):
  if n > 21:
    return 2 * (n - 21)
  else:
    return 21 - n
  
"""
[3] Near hundred:
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
  if abs(100 - n) <= 10 or abs(200 - n) <= 10:
    return True
  else:
    return False
  
# or
def near_hundred2(n):
  return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

"""
[4] Missing char:
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).


missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
  before  = str[:n]
  after   = str[n+1:]
  return before + after

"""
[5] Monkey trouble
We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

monkey_trouble(True, True) → True
monkey_trouble(False, False) → True
monkey_trouble(True, False) → False
"""
def monkey_trouble(a_smile, b_smile):
   return a_smile == b_smile

"""
[6] Parrot trouble
We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False
"""
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

"""
[7] Makes 10

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""
def makes10(a, b):
   return (a == 10 or b == 10 or a + b == 10)


""""
[8] Sum Double
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
def sum_double(a, b):
   sum = a + b
   if a == b:
      sum = sum * 2
   return sum

"""
[9] Pos neg
Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.

pos_neg(1, -1, False) → True
pos_neg(-1, 1, False) → True
pos_neg(-4, -5, True) → True
"""
def pos_neg(a, b, negative):
  if negative:
    return (a < 0 and b < 0)
  else:
    return (a * b < 0)

"""
[10] Not String
Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
   if len(str) >= 3 and str[0:3] == 'not':
      return str
   else:
      return 'not' + str
   
"""
[11] Front back
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
"""
def front_back(str):
  if len(str) <= 1:
    return str
  else:
    return str[-1] + str[1:-1] + str[0]
  
"""
[12] Front 3
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
def front3(str):
   if len(str) <= 2:
      return str + str + str
   else:
      return str[0:3] + str[0:3] + str[0:3]
   
# or, since the slice is silent about out-of-bounds conditions.

def front3(str):
   return str[:3] + str[:3] + str[:3]


#Warm Up 2
"""
[1] Given a string and a non-negative int n, return a larger string that is n copies of the original string.

string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""
def string_times(str, n):
  result = ''
  for i in range(n):
    result = result + str
  return(result)

"""
[2] Front Times
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

front_times('Chocolate', 2) → 'ChoCho'
front_times('Chocolate', 3) → 'ChoChoCho'
front_times('Abc', 3) → 'AbcAbcAbc'
"""
def front_times(str, n):
  result = ''
  for i in range(n):
    result = result + str[:3]
  return(result)

"""
[3] String Bits
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".

string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
"""
def string_bits(str):
  result = ''
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return(result)


"""
[4] String Splosion
Given a non-empty string like "Code" return a string like "CCoCodCode".

string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab'
"""
def string_splosion(str):
  result = ''
  for i in range(len(str)+1):
    result = result + str[:i]
  return result

"""
[5] Last 2
Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).

last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2
"""
def last2(str):
  if len(str) < 2:
    return 0
  
  last2 = str[-2:]
  count = 0
  for i in range(len(str) - 2):
    if str[i:i+2] == last2:
      count += 1
  
  return count


"""
[6] Array Count 9
Given an array of ints, return the number of 9's in the array.

array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3
"""
def array_count9(nums):
  count = 0
  for i in range (len(nums)):
    if nums[i] == 9:
      count += 1
  return count

 
"""
[7] Array Font 9
Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False
"""
def array_front9(nums):
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):
    if nums[i] == 9:
      return True
  return False

"""
[8] Array 123
Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

array123([1, 1, 2, 3, 1]) → True
array123([1, 1, 2, 4, 1]) → False
array123([1, 1, 2, 1, 2, 3]) → True
"""
def array123(nums):
  if len(nums) < 3:
    return False
  for i in range(len(nums)-2):
    if [1,2,3] == nums[i:i+3]:
      return  True
  return False

"""
[9] String Match
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""
def string_match(a, b):
  end = min(len(a), len(b))
  count = 0
  for i in range(end - 1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count += 1
  
  return count

#String 1
"""
[1] Hello Name
Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

hello_name('Bob') → 'Hello Bob!'
hello_name('Alice') → 'Hello Alice!'
hello_name('X') → 'Hello X!'
"""
def hello_name(name):
    return("Hello " + name + "!")

"""
[2] Make Abba
Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi'
make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
make_abba('What', 'Up') → 'WhatUpUpWhat'
"""
def make_abba(a, b):
    return(a + b + b + a)

"""
[3] Make Tags 
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

make_tags('i', 'Yay') → '<i>Yay</i>'
make_tags('i', 'Hello') → '<i>Hello</i>'
make_tags('cite', 'Yay') → '<cite>Yay</cite>'
"""
def make_tags(tag, word):
  return('<'+tag+'>'+word+'</'+tag+'>')


"""
[4] Make out word
Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

make_out_word('<<>>', 'Yay') → '<<Yay>>'
make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
make_out_word('[[]]', 'word') → '[[word]]'
"""
def make_out_word(out, word):
  return(out[:2]+word+out[2:])

"""
[5] Extra End
Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo'
extra_end('ab') → 'ababab'
extra_end('Hi') → 'HiHiHi'
"""
def extra_end(str):
  last_2 = str[-2:]
  return(last_2+last_2+last_2)

"""
[6] First two
Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He'
first_two('abcdefg') → 'ab'
first_two('ab') → 'ab'
"""
def first_two(str):
  if len(str) == 0:
    return("")
  elif len(str)==1:
    return(str[0])
  else:
    return(str[:2])

"""
[7] First half
Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo'
first_half('HelloThere') → 'Hello'
first_half('abcdef') → 'abc'
"""
def first_half(str):
  end = len(str)/2
  return(str[:end])

"""
[8] Without end
Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'
"""
def without_end(str):
  return(str[1:-1])


"""
[9] Combo String
Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') → 'hiHellohi'
combo_string('hi', 'Hello') → 'hiHellohi'
combo_string('aaa', 'b') → 'baaab'
"""
def combo_string(a, b):
  if len(a)>len(b):
    return b + a + b
  else:
    return a + b + a

"""
[10] Non Start
Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

non_start('Hello', 'There') → 'ellohere'
non_start('java', 'code') → 'avaode'
non_start('shotl', 'java') → 'hotlava'
"""
def non_start(a, b):
  return a[1:] + b[1:]


"""
[11] Left 2
Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe'
left2('java') → 'vaja'
left2('Hi') → 'Hi'
"""
def left2(str):
    return str[2:] + str[:2]

#List 1
"""
[1] List 1
Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.

first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False
"""
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

"""
[2] Same first last
Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

same_first_last([1, 2, 3]) → False
same_first_last([1, 2, 3, 1]) → True
same_first_last([1, 2, 1]) → True
"""
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

"""
[3] Make pi
Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.

make_pi() → [3, 1, 4]
"""
def make_pi():
  return [3,1,4]

"""
[4] Common end 
Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True
"""
def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

"""
[5] Sum 3
Given an array of ints length 3, return the sum of all the elements.

sum3([1, 2, 3]) → 6
sum3([5, 11, 2]) → 18
sum3([7, 0, 0]) → 7
"""
def sum3(nums):
  return sum(nums)

#or
def sum3(nums):
  result = 0
  for i in range(len(nums)):
    result += nums[i]
  return result

"""
[6] Rotate Left 3
Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]
"""
def rotate_left3(nums):
  return nums[1:] + [nums[0]]

"""
[7] Reverse 3
Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]
"""
def reverse3(nums):
  return nums[::-1]

"""
[8] Max End 3
Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) → [3, 3, 3]
max_end3([11, 5, 9]) → [11, 11, 11]
max_end3([2, 11, 3]) → [3, 3, 3]
"""
def max_end3(nums):
  if nums[0] > nums[2]:
    max = nums[0]
  else:
    max = nums[2]
  return [max, max, max]

"""
[9] Sum 2
Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.

sum2([1, 2, 3]) → 3
sum2([1, 1]) → 2
sum2([1, 1, 1, 1]) → 2
"""
def sum2(nums):
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]

"""
[10] Middle Way
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) → [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) → [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) → [2, 4]
"""
def middle_way(a, b):
  return [a[1]] + [b[1]]

"""
[11] Make Ends
Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

make_ends([1, 2, 3]) → [1, 3]
make_ends([1, 2, 3, 4]) → [1, 4]
make_ends([7, 4, 6, 2]) → [7, 2]
"""
def make_ends(nums):
  return [nums[0]] + [nums[-1]]

"""
[12] Has 23
Given an int array length 2, return True if it contains a 2 or a 3.

has23([2, 5]) → True
has23([4, 3]) → True
has23([4, 5]) → False
"""
def has23(nums):
  return nums[0] == 2 or nums[1] == 2 or nums[0] == 3 or nums[1] == 3

# Logic 1
"""
[1] Cigar Party
When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) → False
cigar_party(50, False) → True
cigar_party(70, True) → True
"""
def cigar_party(cigars, is_weekend):
  week    = is_weekend == False and (cigars >= 40 and cigars <= 60)
  weekend = is_weekend == True and cigars >= 40
  return week or weekend

"""
[2] Date Fashion
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""
def date_fashion(you, date):
  if you <= 2 or date <= 2:
    return 0
  elif you >= 8 or date >= 8:
    return 2
  else:
    return 1

"""
[3] Squirrel Play
The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

squirrel_play(70, False) → True
squirrel_play(95, False) → False
squirrel_play(95, True) → True
"""
def squirrel_play(temp, is_summer):
  if is_summer:
    return (temp >= 60 and temp <= 100)
  else:
    return (temp >= 60 and temp <= 90)
  
"""
[4] Caught speeding
You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""
def caught_speeding(speed, is_birthday):
  error = 0
  if is_birthday:
    error = 5
  if speed <= (60 + error):
    return 0
  elif speed >= (61 + error) and speed <= (80 + error):
    return 1
  else:
    return 2

"""
[5] Sorta sum
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""
def sorta_sum(a, b):
  soma = a + b
  if soma >= 10 and soma <= 19:
    return 20
  else:
    return soma

"""
[6] Alarm clock
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""
def alarm_clock(day, vacation):
  if day in [1,2,3,4,5]:
    if vacation: 
      return "10:00" 
    else: 
      return "7:00"
  else:
    if vacation: 
      return "off" 
    else: 
      return "10:00"

"""
[7] Love 6
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""
def love6(a, b):
  if a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6:
    return True
  else:
    return False
      
"""
[8] In 1 to 10
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""
def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return n in [1,2,3,4,5,6,7,8,9,10]

"""
[9] Near ten
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""
def near_ten(num):
    return (num % 10 <= 2) or (num % 10 >= 8)

#Logic 2
""" Do again!!!
[1] Makes Bricks
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""
def make_bricks(small, big, goal):
    # Calculate the maximum number of inches that can be covered using the big bricks
    max_big_bricks = big * 5
    
    # Calculate the remaining inches to be covered using the small bricks
    remaining_inches = goal - min(max_big_bricks, goal)
    
    # Check if the remaining inches can be covered using the available small bricks
    return remaining_inches <= small

"""
[2] Lone sum
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""
def lone_sum(a, b, c):
  if a == b  and a == c:
    return 0
  elif a == b:
    return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c

"""
[3] Lucky Sum
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""
def lucky_sum(a, b, c):
  if 13 in [a, b, c]:
    if a == 13:
      return 0
    elif b == 13:
      return a
    else:
      return a + b
  else:
    return a + b + c

"""
[4] Not teen sum
Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""
def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(num):
  if num in [13, 14, 17, 18, 19]:
    return 0
  else:
    return num


"""
[5] Round Sum
For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
"""
def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  r = num % 10
  q = num / 10
  if r >= 5:
    return (q + 1) * 10
  else:
    return q * 10

"""
[6] Close Far
Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True
"""
def close_far(a, b, c):
  return (abs(b-a) <= 1 and abs(c-a) >= 2 and abs(c-b)>= 2) or (abs(c-a) <= 1 and abs(b-a) >= 2 and abs(b-c) >= 2) 

"""
[7] Make Chocolate
We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
"""
def make_chocolate(small, big, goal):
  num_big = int(goal / 5)
  if num_big <= big:
    goal = goal - num_big * 5
  else:
    goal = goal - big * 5
  
  if goal <= small:
    return goal
  else:
    return -1

#String 2
"""
[1] Double Char
Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'
"""
def double_char(str):
  result = ''
  for i in str:
    result = result + i + i
  return result

"""
[2] Count hi
Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2
"""
def count_hi(str):
  count = 0
  for i in range(len(str)):
    if str[i:i+2] == 'hi':
      count += 1
  return count


"""
[3] Cat Dog
Return True if the string "cat" and "dog" appear the same number of times in the given string.

cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
"""
def cat_dog(str):
  count_cat = 0
  count_dog = 0
  for i in range(len(str)):
    if str[i:i+3] == "cat":
      count_cat += 1
    elif str[i:i+3] == 'dog':
      count_dog += 1
  return count_cat == count_dog


"""
[4] Count code
Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

count_code('aaacodebbb') → 1
count_code('codexxcode') → 2
count_code('cozexxcope') → 2
"""
def count_code(str):
  count = 0
  for i in range(len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      count += 1
  return count

"""
[5] End other
Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True
"""
def end_other(a, b):
  a = a.lower()
  b = b.lower()
  if len(a) >= len(b):
    small = b
    big = a
    return big[-len(b):] == b
  else:
    small = a
    big = b
    return big[-len(a):] == a

"""
[6] XYZ there
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
"""
def xyz_there(str):
  for i in range(len(str)-2):
    if str[i:i+3] == 'xyz' and i == 0:
      return True
    elif str[i:i+3] == 'xyz' and str[i-1] != '.':
      return True
  return False
