def count_invalid_parenthesis(string):
    return abs(string.count("(") - string.count(")"))


if __name__ == '__main__':
    print(count_invalid_parenthesis("()())()"))
