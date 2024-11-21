from Abilities import dateandtime
greetings = {'Assalamualaikum' : 'Walaikumassalam',
             'Salamunalaikum' : 'Salamunalaika',
             'Hi' : 'Hi 😀 How can I help you?',
             'Hey' : 'Hey 😀 How can I help you?',
              'Hello' : 'Hello 😀 How can I assist you?'
                }

asking_condition = {"What's up" : "I'm only a bot. But thanks for asking I'm doing alright",
                    "What's up?" : "I'm only a bot. But thanks for asking I'm doing alright",
                    'How are you' : "I'm Fine. What about you?",
                    'How are you?' : "I'm Fine. What about you",
                    'How are you doing' : "I'm good. What about you?",
                    'How are you doing?' : "I'm good. What about you?"
                    }
mathematics = {'Can you do math?' : 'Yes',
               'Can you do math' : 'Yes'
               }
other_resposnse = {"Ok" : "If you need any help you can tell me",
                   "Okay" : "If you need any help you can tell me",
                    "Thanks" : "Pleasure to help 😊",
                     "Thank you" : "Pleasure to help 😊",
                      "Good" : "😊",
                       "well done" : "😊" }

time_date = {"Time?" : f"Now time is {dateandtime.Time()}", "Time" : f"Now time is {dateandtime.Time()}",
             "what's the time now?" : f"Now time is {dateandtime.Time()}",
             "what's the time now" : f"Today {dateandtime.Time()}",
             "Date?" : f"Today {dateandtime.Date()}", "Date" : f"Today {dateandtime.Date()}",
             "What's the date today?" : f"Today {dateandtime.Date()}", "What's the date today" : f"Today {dateandtime.Date()}"
             }