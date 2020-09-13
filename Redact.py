def redact_string(arr1, arr2):
    indices = []
    for i in arr1:
        for j in arr2:
            if i == j:
                indices.append(arr1.index(i))
    return indices


text = input("Enter the text you want to be browsed through: ")
redact = input("Enter the terms to be redacted separated by commas(e.g item1,item2...): ")
text = text.lower()
redact = redact.lower()
redact_arr = redact.split(",")
words_arr = text.split(" ")

indices = redact_string(words_arr, redact_arr)

for i in indices:
    words_arr[i] = "REDACTED"

for i in words_arr:
    print(i, end = " ")


