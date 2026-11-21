#While loops
# i = 1
# while i<=10:
#     print(i)
#     i+=1
#
# print("Done with loop")

#Guessing game
# secret_word = "Giraffe"
# guess = ""
# tries = 0
# guess_limit = 3
# out_of_guesses = False
#
# while guess !=secret_word and not out_of_guesses:
#     if tries < guess_limit:
#         guess = input("Guess the word: ")
#         guess = guess[:1].upper() + guess[1:]
#         tries +=1
#     else:
#         out_of_guesses = True
#
# if out_of_guesses:
#     print("Out of guesses :(")
# else:
#     print('You guessed the secret word!')

#For loops
for letter in "Giraffe Academy":
    print(letter)

friends = ["Jim", "Karen", "Kevin"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(index)