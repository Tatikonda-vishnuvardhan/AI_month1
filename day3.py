# guess the number game
import random
import numpy as np
rng = np.random.default_rng()
guess = rng.integers(1, 100)
guess = random.randint(1, 100)
user_guess = None

attempt = 0
while guess != user_guess:
    user_guess = int(input("guess the number:"))
    attempt += 1
    if user_guess < guess:
        print("a little higher")
    elif user_guess > guess:
        print("a litle lower")
    else:
        print(f"correct number, you have guessed in {attempt} attempts ")
