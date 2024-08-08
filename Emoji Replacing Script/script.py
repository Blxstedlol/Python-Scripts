import random
def EmojiScript():
    user_input = input('Enter something to convert to emoji, example: :): ')
    if user_input == ':)':
        print('🙂')
    if user_input == ':(':
        print('☹️')
    else:
        print(random.choice(['😎', '😍', '🤝']), 'Your Input was invalid')

EmojiScript()