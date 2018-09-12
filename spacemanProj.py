import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
secret_word = "" 
underscore = ""
guess = 6
fail = False
word = []

right_guess = []
wrong_guess = []
all_guess = []

def load_word():
  global secret_word
  f = open('words.txt', 'r')
  words_list = f.readlines()
  f.close()

  words_list = words_list[0].split(' ')
  secret_word = random.choice(words_list)
  print("The secret word is " + secret_word)
  return secret_word




def user_input(prompt):
  user_input = input(prompt)
  while user_input.lower() not in letters:
    print("{} is not a valid letter please try agian: ".format(user_input))
    user_input = input(prompt)
  return user_input


def fill_secret_word(user_input):
  # adds an underscore to each letter in the secret_word it loops through.
  # global secret_word
  global guess
  global secret_word
  global fail
  global word
  guess_letter = []
  guess_letter.append(user_input)
  

  for i in list(secret_word):
    if i in guess_letter:
      word.append(i)
      fail = False
    else:
      word.append("_")
  print(word)


  #     fail = True 

  # if fail:
  #   guess -= 1

  # fail = False

      

  


# fill_secret_word(user_input("input a letter you have {} tries: ".format(guess)))
 





  # hidden_word = []
  # global secret_word
  # for letter in range(0,len(secret_word)):
  #   temp_Str = temp_Str.append("_ ")
  # print(temp_Str)


def search_guessed_letter_in_word():
  letter1 = user_input("guess a letter! : ")
  letter = ""
  for lets in secret_word:
    letter = letter + lets
  # for letter in secret_word:
  #   letters = letters + letter


  for letter1 in secret_word:
    if letter1 == letter:
      print("letter is in secret word.")
    else:
      print("no such letter in the secret word ):")

  # if letter1 == letters:
  #   print("letter input is in the secret word.")
  # else:
  #   print("guessed letter is not in the secret word.")










def is_word_guessed(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    global right_guess
    global wrong_guess
    global all_guess
    global guess

    # FILL IN YOUR CODE HERE...
    for i in list(secret_word):
      if i in letters_guessed:
        right_guess.append(i)

      elif letters_guessed not in list(secret_word):
        wrong_guess.append(letters_guessed)
        if letters_guessed not in all_guess:
          guess -= 1
        break
    all_guess = wrong_guess + right_guess
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
    lettersGuessed: list of letters that have been guessed so far.
    returns: string, of letters and underscores.  For letters in the word that the user has
    guessed correctly, the string should contain the letter at the correct position.  For letters
    in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    # FILL IN YOUR CODE HERE...
    right_guess = []
    for i in list(secret_word):
      if i in letters_guessed:
        right_guess.append(i)
      else:
        right_guess.append("_")
    print(right_guess)

    if right_guess == list(secret_word):
      print("you won! the word is " + secret_word + "!")
      global guess 
      guess = 0






def get_available_letters(letters_guessed):
    '''
    lettersGuessed: list of letters that have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''





def spaceman(secret_word):
    '''
    secretWord: string, the secret word to guess.
    Starts up a game of Spaceman in the command line.
    * At the start of the game, let the user know how many
      letters the secretWord contains.
    * Ask the user to guess one letter per round.
    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...
    print("The secret word has {} letters".format(len(secret_word)))
    print("You have 7 guesses.")

    while guess > 0:
      is_word_guessed(secret_word, user_input("please eneter a letter you have {} guesses left: ".format(guess)))

      get_guessed_word(secret_word, right_guess)
    get_available_letters(all_guess)
    print("All guesses: ", all_guess)



# user_input("enter a letter \n")
# load_word()

#
secret_word = load_word()
spaceman(load_word())
