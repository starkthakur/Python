from collections import Counter

text = "The class attribute is often used to point to a class name in a style sheet."  \
       "In the following example we have three <div> elements with a class attribute with the value of city." \
       "All of the three <div> elements will be styled equally according to the .city style definition in the head section:" \
       "solution to the test problem"

words = text.split()
print(words)

counter = Counter(words)
top_three = counter.most_common(3)
print("These are the Top 3", top_three)