def multi_bracket_validation(input):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    brackets = [
        character for character in input if character in open_brackets or character in close_brackets]

    # First-glance fail conditions
    if len(brackets) < 2 or brackets[0] in close_brackets or brackets[:-1] in open_brackets:
        return False

    # Parity fail conditions
    for i in range(3):
        if brackets.count(open_brackets[i]) != brackets.count(close_brackets[i]):
            return False

    # Semantic fail conditions
    for index, bracket in enumerate(brackets):
        if bracket in open_brackets and (brackets[index+1] in close_brackets and close_brackets.index(brackets[index+1]) != open_brackets.index(bracket)):
            return False

    return True


if __name__ == '__main__':
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
