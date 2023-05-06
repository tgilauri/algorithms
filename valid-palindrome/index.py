def valid_palindrome(s: str):
    left = 0
    right = len(s) - 1

    while left <= right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            str_1 = s[:left] + s[left + 1:]
            str_2 = s[:right] + s[right + 1:]
            return str_1 == str_1[::-1] or str_2 == str_2[::-1]
    return True


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
print(valid_palindrome('acxcybycxcxa'))  # False
