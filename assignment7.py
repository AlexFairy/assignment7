
# 1. Product Review Analysis 
# 
# Task 1: Keyword Highlighter

#Write a program that searches through reviews list and 
# looks for keywords such as "good", "excellent", 
# "bad", "poor", and "average". 
# We want you to capitalize those keywords then 
# print out each review. 
# Print out each review with the keywords in 
# uppercase so they stand out.

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

def update_list(final_review):
  global reviews
  for i in final_review:
    i1 = i.replace("good", "GOOD")
    i2 = i1.replace("excellent", "EXCELLENT")
    i3 = i2.replace("bad", "BAD")
    i4 = i3.replace("Poor", "POOR")
    i5 = i4.replace("average", "AVERAGE")
    print(i5)
  
#empty = [] #new data has to go through somewhere so it goes through here

update_list(reviews)


# So for the first string in the reviews list, we want it to say: 
# "This product is really GOOD. 
# I'm impressed with its quality."

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review.  
# The function should return the total count of positive and negative words.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]

for r in reviews:
  positive_count = 0
  print(f"{r}")
  for p_word in positive_words:
    if p_word in r:
      print(f"A positive word: {p_word} was found in the review")
      positive_count += 1
  print(positive_count)

for x in reviews:
  negative_count = 0
  print(f"{x}")
  for n_word in negative_words:
    if n_word in x:
      print(f"A negative word: {n_word} was found in the review")
      negative_count += 1
  print(negative_count)


#Task 3:

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."]

sentence1 = reviews[0][0:33] + "..." + ","
sentence2 = reviews[1][0:35] + "..." + ","
sentence3 = reviews[2][0:33] + "..." + ","
sentence4 = reviews[3][0:31] + "..." + ","
sentence5 = reviews[4][0:33] + "..." + ","

#print(reviews[0][0:33] + "..." + ",") #Version1
print(sentence1)
print(sentence2)
print(sentence3)
print(sentence4)
print(sentence5)


#Task 1: 
# Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

user_input = input("Type first name: ")
first_name_length = len(user_input) 
user_input2 = input("Type last name: ")
last_name_length = len(user_input2)

if first_name_length > 2 and last_name_length > 2:
  print(f"First name count is {first_name_length} and last name count is {last_name_length}")
else:
  print("Error!")