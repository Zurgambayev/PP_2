def count_upper(text):
    upper_count = 0
    for i in text:
        if i.isupper():
            upper_count += 1
    return (upper_count)

# Example usage
text = input()
upper = count_upper(text)
print(upper)
