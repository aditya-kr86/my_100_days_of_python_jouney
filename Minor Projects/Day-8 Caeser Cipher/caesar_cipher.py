import random
import string
from ascii import logo


def encoded_message(message):
    Message_words = Message.split(" ")
    for i in range(len(Message_words)):
        word = Message_words[i]
        if len(word) <= 2:
            word = word[::-1]
        else:
            # Generating word of 3 random letters
            random_chars1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            random_chars2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            # Move the first character to the end
            word = word[1:] + word[0]
            word = random_chars1 + word + random_chars2
        Message_words[i] = word
    print("Encoded message is:", " ".join(Message_words))
    print()


def decode_message(encoded_message):
    encoded_words = encoded_message.split(" ")
    decoded_words = []
    
    for word in encoded_words:
        if len(word) <= 2:
            decoded_word = word[::-1]
        else:
            # Remove the first 3 and last 3 random characters
            core_word = word[3:-3]
            # Move the last character to the front
            decoded_word = core_word[-1] + core_word[:-1]
        decoded_words.append(decoded_word)
    print("Decoded message is:", " ".join(decoded_words))
    print()


if __name__ == '__main__':
    print(logo)
    game_start = True
    while game_start :
        Action = str(input("Enter Which Action You want to Perform - ENCODE/DECODE  or Enter EXIT to skip this:"))
        Message = str(input("Enter the message: "))
        if(Action.lower() == "exit"):
            print("The For Playing Caeser cipher")
            game_start = False

        if(Action.lower() == "encode"):
            encoded_message(Message)
            print()
        elif(Action.lower() == "decode"):
            decode_message(Message)
            print()
