# O(n*m)
def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            return i 
    return -1 
print(naive_search("hello world", "world"))  # 6


# O(n+m) или O(n*m)
def rabin_karp(text, pattern, base=256, prime=101):
    n, m = len(text), len(pattern)
    hpattern = 0
    htext = 0
    h = 1

    for i in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        hpattern = (base * hpattern + ord(pattern[i])) % prime
        htext = (base * htext + ord(text[i])) % prime

    for i in range(n - m + 1):
        if hpattern == htext:
            if text[i:i + m] == pattern:
                return i  

        if i < n - m:
            htext = (base * (htext - ord(text[i]) * h) + ord(text[i + m])) % prime
            if htext < 0:
                htext += prime

    return -1

print(rabin_karp("hello wwowrld and world", "ld")) 

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    j = 0

    for i in range(1, m):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1]

        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j

    return pi

print(compute_prefix_function("ababc")) 

def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    pi = compute_prefix_function(pattern)
    j = 0

    for i in range(n):
        while j > 0 and text[i] != pattern[j]:
            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1
            if j == m:
                return i - m + 1 

    return -1

print(kmp_search("hello world", "world"))  




