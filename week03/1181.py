import sys
input = sys.stdin.readline

n = int(input())
words = list(set([input().rstrip() for _ in range(n)]))
words.sort()
words.sort(key = len)
print('\n'.join(words))