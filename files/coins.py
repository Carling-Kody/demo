

def sum_pennies(user_input):
    #converting "user_input" to int ex user_input = "100" then int(user_input) = 100
    sum_of_pennies = int(user_input)
    return sum_of_pennies


def sum_nickles(user_input):
    num_of_nickles = int(user_input)
    sum_of_nickles = num_of_nickles * 5
    return sum_of_nickles


def sum_dimes(user_input):
    num_of_dimes = int(user_input)
    sum_of_dimes = num_of_dimes * 10
    return sum_of_dimes


def sum_quarters(user_input):
    num_of_quarters = int(user_input)
    sum_of_quarters = num_of_quarters * 25
    return sum_of_quarters


def sum_all_coins(pennies, nickles, dimes, quarters):
    sum_of_all_coins  = sum_pennies(pennies) + sum_nickles(nickles) + sum_dimes(dimes) + sum_quarters(quarters)
    return sum_of_all_coins


def get_total_message(total: int):
    if total == 100:
            message = 'You win!'
    elif total > 100:
        diff = total-100
        message = f'You Lose! You were over by {diff}'
    else:
        diff = 100 - total
        message = f'You Lose! You were under by {diff}'

    return message



