Hi, here's your problem today. This problem was recently asked by Google:

Given a string with a certain rule: k[string] should be expanded to string k times. So for example, 3[abc] should be expanded to abcabcabc. Nested expansions can happen, so 2[a2[b]c] should be expanded to abbcabbc.

Your starting point:

```
def decodeString(s):
  # Fill this in.

print decodeString('2[a2[b]c]')
# abbcabbc
```

## Solution

- [Python Solution](./Solution.py)