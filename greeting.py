# import modules
import random

# create a list with multiple items

greetings = ["Hello!", "What's up?!", "Howdy!", "Greetings!"]
goodbyes = ["Bye!", "Goodbye!", "See you later!", "See you soon!"]

# create keywords and reponsese that the chatbot will know

keywords = ["music", "pet", 'book', 'game']
responses = ["Music is so relaxing!", "Dogs are man's best friend!", "I know about a lot of books.", "I like to play video games."]

print(random.choice(greetings))

user = input("Say something (or type bye to quit): ")
user = user.lower()

# lower() converts the user's response to lowercase

# keep interacting with the user until they say "bye"

while (user != "bye"):
    for index in range (len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])

# in python a colon is requied at the beginning of every block of code

# teach the AI chatbot a new keyword and response

while (user != "bye"):
    keyword_found = False

    for index in range(len(keywords)):
        if (keywords[index] in user):
            print("Bot: " + responses[index])
            keyword_found = True

    if (keyword_found == False):
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to?")
        keywords.append(new_keyword)
        new_reponse = input("How should I repond to " + new_keyword + "? ")
        responses.append(new_reponse)

# if the responses is not trained when we will ask for it to learn it

# ask the user for another reponse

while (user != 'bye'):
    
