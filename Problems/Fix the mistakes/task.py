text = input()
words = text.split()
for word in words:
    search = word.lower()
    if search.startswith("https://") or search.startswith("http://") or search.startswith("www."):
        print(word)
