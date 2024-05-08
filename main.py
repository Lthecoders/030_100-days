import os
import random
import time

print(
    "\033[34m",
    "-----------------> 30 Days Down - what did you think <------------------? ",
    "\033[0m")
print("\033[31m",
      "               <---------------------------------------->\n\n\n",
      "\033[0m")
increment = 28
while True:
  increment += 1
  if increment > 30:
    print(
        "\033[32m",
        "\n\n\n-------- THANKS FOR YOUR RESPONSE and All The Best for rest of days 👍",
        "\033[0m")
    break
  if increment > 1:
    print(
        "\033[34m",
        "-----------------> 30 Days Down - what did you think <------------------? ",
        "\033[0m")
    print("\033[31m",
          "               <---------------------------------------->\n\n\n",
          "\033[0m")
  user_day = input(f"How was Day {increment} ?  -----> ")
  print()
  print()
  answer1=(f"\n                                You thought Day {increment} was \n")
  answer2=(f"{user_day:} \n")
  print(f"{answer1}")
  print(f"{answer2: ^90}")
  print("\n\nsaving the data...")
  time.sleep(5)
  os.system("clear")
  if increment == 30:
    print("\n\n\n\nsaving your data... of day 30")
  elif increment < 30:
    print(
        f"\n\n\n\nsaving your data of day {increment} and ....getting to day {increment + 1}"
    )
  time.sleep(5)
  os.system("clear")
