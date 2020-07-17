def index_search(i, c):
    try:
        return matrix[i].index(c)
    except:
        None


def word_search_in_matrix(matrix, word, array):
    w_len = len(word)
    r_row = True
    r_column = True

    for i in array:
        if i[1] + w_len - 1 <= len(matrix[i[0]]):
            for x in range(w_len):
                if word[x] != matrix[i[0]][x]:
                    r_row = False

    for j in array:
        if j[1] + w_len - 1 <= len(matrix[j[0]]):
            for y in range(w_len):
                if word[y] != matrix[y][j[1]]:
                    r_column = False

    return r_row or r_column


def word_search(matrix, word):
    w_list = list(word)
    w_len = len(word)

    l = []
    for i in range(len(matrix)):
        a = index_search(i, w_list[0])
        if a is not None:
            l.append([i, a])

    if word_search_in_matrix(matrix, word, l):
        return True
    return False


if __name__ == '__main__':
    matrix = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
    print(word_search(matrix, 'FOAM'))
    # True
