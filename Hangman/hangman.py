# import random

# words = ("apple","banana","pineapple","orange","pear","mango")

# hangman_art = {0:("   ",
#                   "   ",
#                   "   "),
#                1:(" o ",
#                   "   ",
#                   "   "),
#                2:(" o ",
#                   " | ",
#                   "   "),
#                3:(" o ",
#                   "/| ",
#                   "   "),
#                4:(" o ",
#                   "/|\\",
#                   "   "),
#                5:(" o ",
#                   "/|\\",
#                   "/  "),
#                6:(" o ",
#                   "/|\\",
#                   "/ \\")}

# def display_man(wrong_guess):
#     print("*"*20)
#     for man in hangman_art[wrong_guess]:
#         print(man)
#     print("*"*20)

# def display_hint(hint):
#     print(" ".join(hint))

# def dis_answer(answer):
#     print(" ".join(answer))

# def main():
#     answer = random.choice(words)
#     hint = ["_"] * len(answer)
#     wrong_guesses = 0
#     guessed_letter = set()
#     is_running = True

#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Guess the letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input!")
#             continue

#         if guess in guessed_letter:
#             print(f"{guess} this is alredy guessed.")

#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#                     guessed_letter.add(guess)
#         else:
#             wrong_guesses += 1
        
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             dis_answer(answer)
#             print("You Win!!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art)-1:
#             display_man(wrong_guesses)
#             dis_answer(answer)
#             print("You loss!!")
#             is_running = False


# if __name__ == '__main__':
#     main()

import random

words = ["apple","banana","pineapple","orange","pear","mango"]

hang_man = {0:("   ",
                  "   ",
                  "   "),
               1:(" o ",
                  "   ",
                  "   "),
               2:(" o ",
                  " | ",
                  "   "),
               3:(" o ",
                  "/| ",
                  "   "),
               4:(" o ",
                  "/|\\",
                  "   "),
               5:(" o ",
                  "/|\\",
                  "/  "),
               6:(" o ",
                  "/|\\",
                  "/ \\")}

# for man in hang_man[6]:
#     print(man)

def dis_hangman(wrong_guess):
    print("*"*20)
    print("If you see full man you lose.")
    for man in hang_man[wrong_guess]:
        print(man)
    print("*"*20)

def dis_hint(hint):
    print(" ".join(hint))
    # print(hint) #This will just print list

def dis_asn(answer):
    print("The answer is " + " ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guess = 0
    guessed_letter = set()
    is_run = True

    while is_run:
        dis_hangman(wrong_guess)
        dis_hint(hint)
        guess = input("Enter the letter: ").lower()

        if len(guess) != 1 or guess.isdigit():
            print("Invalid input!")
            continue
        
        if guess in guessed_letter:
            print("letter alredy guessed....")
            continue

        guessed_letter.add(guess)
    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guess += 1

        if "_" not in hint:
            dis_hangman(wrong_guess)
            dis_asn(answer)
            print("You won!")
            is_run = False

        if wrong_guess >= len(hang_man)-1:
            dis_hangman(wrong_guess)
            dis_asn(answer)
            print("You lost!!")
            is_run = False        


if __name__ == "__main__":
    main()