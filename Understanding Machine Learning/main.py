import nltk 
from nltk.chat.util import Chat,reflections

reflections ={
    "I am":"You are",
     "I was":"I were",
     "I" : "You",
     "Your": "My",
     "I will": "You will",
     "me":"you"    
}
pairs =[
   [
       r"My name is (.*)",
       ["Hello %1, How are you today?"]
   ],
   [
        r"I am fine what about you?",
        ["I am fine too!"]
   ],
   [
         r"What is your name?",
     ["My name is EthanBot"]
   ],
   [
         r"quit",
     ["Bye! %1 have a wonderful day!"]
   ],
]
def my_chat():
    print("Welcome, Chat with EthanBot")
    chatbot = Chat(pairs,reflections)
    chatbot.converse()

if __name__ =="__main__":
    my_chat()