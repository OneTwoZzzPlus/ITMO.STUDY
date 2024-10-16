f = lambda s: [max(k for k in range(i) if s[:k] == s[i-k:i]) for i in range(1, len(s)+1)]

# Tests
for test in ["AAAAA", "qqqwwgg", "IO"]:
    print(test, f(test))
