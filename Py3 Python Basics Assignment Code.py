#####################################################################################################################
#
#
#
# Week 2
#
#
#
#####################################################################################################################

# python 3 specialization graded tools
# week 2
let = "z"
let_two = "p"
c = let_two + let
m = c * 5
print(m)

# Write one for loop to print out each character of the string my_str on a separate line.
my_str = "MICHIGAN"

for chr in my_str:
    print(chr)

# Write one for loop to print out each element of the list several_things.
# Then, write another for loop to print out the TYPE of each element of the list several_things.
# To complete this problem you should have written two different for loops,
# each of which iterates over the list several_things, but each of those 2 for loops should have a different result.

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]

for thing in several_things:
    print(thing)

for thing in several_things:
    print(type(thing))

# Write code to count the number of characters in original_str using the accumulation pattern
# and assign the answer to a variable num_chars.
# Do NOT use the len function to solve the problem
# (if you use it while you are working on this problem, comment it out afterward!)

original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0

for word in original_str:
    num_chars = num_chars + 1
print(num_chars)

# addition_str is a string with a list of numbers separated by the + sign.
# Write code that uses the accumulation pattern to take the sum of all of the numbers and assigns it to sum_val (an integer).
# (You should use the .split("+") function to split by "+" and int() to cast to an integer).

addition_str = "2+5+10+20"
addition_str = addition_str.split("+")
# print(addition_str)

sum_val = 0

for num in addition_str:
    sum_val = sum_val + int(num)
print(sum_val)

# week_temps_f is a string with a list of fahrenheit temperatures separated by the , sign.
# Write code that uses the accumulation pattern to compute the average (sum divided by number of items) and assigns it to avg_temp.
# Do not hard code your answer (i.e., make your code compute both the sum or the number of items in week_temps_f)
# (You should use the .split(",") function to split by "," and float() to cast to a float).

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
week_temps_f = week_temps_f.split(",")

temps = 0

for temp in week_temps_f:
    temps = temps + float(temp)
# print(temps)
# print(len(week_temps_f))

avg_temp = temps / len(week_temps_f)
print("Average temperature:", avg_temp)

# Write code to create a list of numbers from 0 to 67 and assign that list to the variable nums. Do not hard code the list.

nums = [0]
for n in range(67):
    x = n + 1
    nums.append(x)
print(nums)

# Write code to create a list of word lengths for the words in original_str using the accumulation pattern and assign the answer to a variable num_words_list.
# (You should use the len function).

original_str = "The quick brown rhino jumped over the extremely lazy fox"
original_str = original_str.split(" ")
print(original_str)
num_words_list = []

for word in original_str:
    x = len(word)
    num_words_list.append(x)
print(num_words_list)

# Create an empty string and assign it to the variable lett.
# Then using range, write code such that when your code is run, lett has 7 b’s ("bbbbbbb").
lett = ""

for i in range(7):
    lett = lett + "b"
    # print(i)
print(lett)

# Write a program that uses the turtle module and a for loop to draw something. It doesn’t have to be complicated,

import turtle

wn = turtle.Screen()
wn.bgcolor("teal")
tess = turtle.Turtle()
tess.color("grey")
tess.shape("turtle")

dist = 2
tess.up()  # this is new
for _ in range(69):  # start with size = 5 and grow by 2
    tess.stamp()  # leave an impression on the canvas
    tess.forward(dist)  # move tess along
    tess.right(24)  # and turn her
    dist = dist + 2

######################################################################################################################
#
#
#
# Week 3
#
#
#
#######################################################################################################################

# rainfall_mi is a string that contains the average number of inches of rainfall in Michigan for every month (in inches) with every month separated by a comma.
# Write code to compute the number of months that have more than 3 inches of rainfall.
# Store the result in the variable num_rainy_months. In other words, count the number of items with values > 3.0.

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
rainfall_mi = rainfall_mi.split(",")
num_rainy_months = 0

for rain in rainfall_mi:
    rainfall = float(rain)
    if rainfall > 3.0:
        num_rainy_months = num_rainy_months + 1
print(num_rainy_months)

# The variable sentence stores a string. Write code to determine how many words in sentence start and end with the same letter,
# including one-letter words. Store the result in the variable same_letter_count.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"

# Write your code here.
same_letter_count = 0
sentence = sentence.split()

for word in sentence:
    if word[0] == word[-1]:
        same_letter_count += 1

print(same_letter_count)

# Write code to count the number of strings in list items that have the character w in it. Assign that number to the variable acc_num.

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama", "tumultuous", "owing"]

acc_num = 0

for item in items:
    if "w" in item:
        acc_num += 1

print(acc_num)

# Write code that counts the number of words in sentence that contain either an “a” or an “e”.
# Store the result in the variable num_a_or_e.

sentence = "python is a high level general purpose programming language that can be applied to many different classes of problems."
sentence = sentence.split(" ")

num_a_or_e = 0

for word in sentence:
    if "a" in word:
        num_a_or_e += 1
    elif "e" in word:
        num_a_or_e += 1
print(num_a_or_e)

# Write code that will count the number of vowels in the sentence s and assign the result to the variable num_vowels. For this problem, vowels are only a, e, i, o, and u.
# Hint: use the in operator with vowels.

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a', 'e', 'i', 'o', 'u']
num_vowels = 0

for letter in s:
    if letter in vowels:
        num_vowels += 1
print(num_vowels)

######################################################################################################################
#
#
#
# Week 4
#
#
#
######################################################################################################################

# Currently there is a string called str1. Write code to create a list called chars which should contain the characters from str1.
# Each character in str1 should be its own element in the list chars.

str1 = "I love python"
# HINT: what's the accumulator? That should go here.
chars = []
for char in str1:
    chars.append(char)
print(chars)

# For each character in the string saved in ael, append that character to a list that should be saved in a variable app.

ael = "python!"
app = []

for char in ael:
    app.append(char)

# For each string in wrds, add ‘ed’ to the end of the word (to make the word past tense).
# Save these past tense words to a list called past_wrds.

wrds = ["end", 'work', "play", "start", "walk", "look", "open", "rain", "learn", "clean"]
past_wrds = []

for wrd in wrds:
    past = wrd + "ed"
    past_wrds.append(past)
print(past_wrds)

######################################################################################################################
#
#
#
# Python Basics Final Assignment
#
#
#
######################################################################################################################

# Below are a set of scores that students have received in the past semester.
# Write code to determine how many are 90 or above and assign that result to the value a_scores.

scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
scores = scores.split()
a_scores = 0

for score in scores:
    if int(score) >= 90:
        a_scores += 1
print(a_scores)

# Write code that uses the string stored in org and creates an acronym which is assigned to the variable acro.
# Only the first letter of each word should be used, each letter in the acronym should be a capital letter,
# and there should be nothing to separate the letters of the acronym.
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if org was assigned the string “hello to world” then the resulting acronym should be “HW”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
org = org.split()

acro = ""

for word in org:
    if word not in stopwords:
        a = word[0]
        a = a.upper()
        acro = acro + a
print(acro)

# Write code that uses the string stored in sent and creates an acronym which is assigned to the variable acro.
# The first two letters of each word should be used, each letter in the acronym should be a capital letter,
# and each element of the acronym should be separated by a “. ” (dot and space).
# Words that should not be included in the acronym are stored in the list stopwords.
# For example, if sent was assigned the string “height and ewok wonder” then the resulting acronym should be “HE. EW. WO”.

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sent = sent.split()

acro = ""

# for word in sent:
#    if word not in stopwords:
#        a = word[0:2]
#        a = a.upper()
#        acro = acro + a
#        if a != sent[-1]:
#            acro += ". "
# print(acro)

acro = '. '.join(word[:2].upper() for word in sent if word not in stopwords)
print(acro)

# A palindrome is a phrase that, if reversed, would read the exact same.
# Write code that checks if p_phrase is a palindrome by reversing it and then checking if the reversed version is equal to the original.
# Assign the reversed version of p_phrase to the variable r_phrase so that we can check your work.

p_phrase = "was it a car or a cat I saw"
r_phrase = "was it a car or a cat I saw"[::-1]
print(r_phrase)

# Just for fun
p_holes = "stanley yelnats"
r_holes = "stanley yelnats"[::-1]
print(r_holes)

# Provided is a list of data about a store’s inventory where each item in the list represents the name of an item,
# how much is in stock, and how much it costs.
# Print out each item in the list with the same formatting, using the .format method (not string concatenation).
# For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.

inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]

for item in inventory:
    item_desc, number, cost = item.split(", ")
    print("The store has {} {}, each for {} USD.".format(number, item_desc, cost))