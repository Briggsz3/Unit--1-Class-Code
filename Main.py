'''
Name: Zachary Briggs
Date:9/16/24
Assignment: Unit 2 Lesson 1 Notes

'''
# Variables- stores information

message= "Hello there"
print(message)

# snake_case

user_name = input('Enter your name:')
user_id = int(input('Enter your id:'))

#variable type command
#print(type(user_name))

#Type 1 - strings
#can use ' or " to indicate string - be consistent

#f-strings are formatted strings that help with combining string
# Way 1 to combine string: use + (concatenation)
# Caution: all numbers have to have str() around them
message_one = 'welcome' +user_name +'with ID' + str(user_id)
print(message_one)

# Way 2 - use f strings
message_two= f"Welcome {user_name} with ID {user_id}"
print(message_two)

# Possible errors
famous_quotation = ('Its better to live a life of embarrassing moments than to live a life of regret\'s')
# apostrophes inside of single quotes
#resolution: use escape sequence \ - tells python next symbol is literally that thing,
# \no pythonic meaning

#raw strings]
moose = r""""
                                       /) \ |\    //
                                 (\\|  || \)u|   |F     /)
                                  \```.FF  \  \  |J   .'/
                               __  `.  `|   \  `-'J .'.'
        ______           __.--'  `-. \_ J    >.   `'.'   .
    _.-'      ""`-------'           `-.`.`. / )>.  /.' .<'
  .'                                   `-._>--' )\ `--''
  F .                                          ('.--'"
 (_/                                            '\
  \                                             'o`.
  |\                                                `.
  J \          |              /      |                \
   L \                       J       (             .  |
   J  \      .               F        _.--'`._  /`. \_)
    F  `.    |                       /        ""   "'
    F   /\   |_          ___|   `-_.'
   /   /  F  J `--.___.-'   F  - /
  /    F  |   L            J    /|
 (_   F   |   L            F  .'||
  L  F    |   |           |  /J  |
  | J     `.  |           | J  | |              ____.---.__
  |_|______ \  L          | F__|_|___.---------'
--'        `-`--`--.___.-'-'---
"""
print(moose)