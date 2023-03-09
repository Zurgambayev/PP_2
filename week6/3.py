def reverse(text):
    if text[::-1] == text:
        return 'Good'
    else:
        return 'Baad'
print(reverse(input()))
    