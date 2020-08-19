from collections import Counter


def longest_substring_with_k_distinct_characters(s, k):
    longest = []
    if len(Counter(s)) == k:
        return len(s), s

    for i in range(len(s)):
        d = []
        count = 0
        for j in range(i, len(s)):
            c = s[j]
            if c not in d:
                count += 1
            if count > k:
                break
            d.append(c)

        if len(d) > len(longest):
            longest = d

    t = ""
    for i in longest:
        t += i

    return len(t), t


if __name__ == '__main__':
    print(longest_substring_with_k_distinct_characters('aabcdefff', 6))
    # aabcdefff

    print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
    # 5 (because 'defff' has length 5 with 3 characters)
