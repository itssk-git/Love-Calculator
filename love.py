def loveCalculate():
    f_name = input("Enter your name: ")
    l_name = input("Enter your partner's name: ")

    love_array = f_name + "loves" + l_name
    result_counts = []

    while love_array:
        first_char = love_array[0]
        count = love_array.count(first_char)
        result_counts.append(count)
        love_array = love_array.replace(first_char, "")

    while len(result_counts) > 2:
        temp = []
        for i in range((len(result_counts) + 1) // 2):
            if i == len(result_counts) - 1 - i:
                temp.append(result_counts[i])
            else:
                s = result_counts[i] + result_counts[len(result_counts) - 1 - i]
                temp.append(s)  # Add the sum directly without splitting
        result_counts = temp

    if len(result_counts) == 2:
        final_number = str(result_counts[0]) + str(result_counts[1])
    else:
        final_number = str(result_counts[0])

    print("Final two-digit number:", final_number)


def playGames():
    user_input = input("""Do you want to calculate how much your partner loves you?
          Press Y for Yes
          Press N for No
          """)
    
    if user_input == "Y" or user_input == "y":
        loveCalculate()
    elif user_input == "N" or user_input == "n":
        sys.exit()  # Gracefully exit the program
    else:
        print("Please enter Y or N.")
        playGame()  # Call playGame again to prompt the user for valid input


# Start the game
#Start
playGames()
