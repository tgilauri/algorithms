def valid_palindrome(s: str):
    left = 0
    right = len(s) - 1
    middle = int(len(s) / 2) if len(s) % 2 != 0 else (len(s) / 2) + 0.5
    removals = 0

    valid = True

    while left < middle < right and removals < 2:
        left_char = s[left]
        right_char = s[right]
        if left_char != right_char:
            if s[left + 1] == s[right] and s[left + 2] == s[right - 1]:
                left += 1
                removals += 1
                continue
            if s[left] == s[right - 1] and s[left + 1] == s[right - 2]:
                right -= 1
                removals += 1
                continue
            else:
                valid = False
                break
        else:
            left += 1
            right -= 1
    return False if removals > 1 else valid


print(valid_palindrome('aba'))  # True
print(valid_palindrome('abba'))  # True
print(valid_palindrome('acbca'))  # True
print(valid_palindrome('succus'))  # True

print('')

print(valid_palindrome('abca'))  # True
print(valid_palindrome('abcca'))  # False
print(valid_palindrome('succuss'))  # True

print('')

print(valid_palindrome('succusss'))  # False
print(valid_palindrome('abcdefg'))  # False
