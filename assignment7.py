
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
  for i in reviews:
    i1 = i.replace("good", "GOOD")
    i2 = i1.replace("excellent", "EXCELLENT")
    i3 = i2.replace("bad", "BAD")
    i4 = i3.replace("Poor", "POOR")
    i5 = i4.replace("average", "AVERAGE")
    print(i5)
  
empty = [] #new data has to go through somewhere so it goes through here

update_list(empty)


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


#Task 3: Review Summary I'M STUCK. I'LL RESUBMIT THE ASSIGNMNET LATER

#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word.

#Example: "This product is really good. I'm...",

reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
for review in reviews:
  sliced_reviews = review[0:30]
  if review > len(30):
    summary = review[30:]

  print(total)


# 2. User Input Data Processor

#Objective: The aim of this assignment is to process and format user input data.

#Task 1: I'M STUCK. I'LL RESUBMIT THE ASSIGNMNET LATER

# Input Length Validator Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

first_name = input("Please type a first name: ")
last_name = input("Please type a last name: ")

for x in range(int(first_name and last_name)) > 2:
  print("Good job!")
else:
  print("Error")