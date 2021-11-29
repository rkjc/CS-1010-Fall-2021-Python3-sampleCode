my_list = ['earth', 'exciting', 'day', 'laptop', 'electrochemical', 'blue', 'up']
print("Run #1")
longest_word = ""
for temp_word in my_list:
    temp_word_len = len(temp_word)
    print(temp_word, temp_word_len)
    if temp_word_len > len(longest_word):
        longest_word = temp_word

print("Longest word is", longest_word)
print("--------------------------")

my_list = ['indistinguishable', 'acorn', 'soap', 'ladder', 'cheese', 'disillusioned', 'pit', 'monday', 'placeholder', 'teleconference']
print("Run #2")
longest_word = ""
for temp_word in my_list:
    temp_word_len = len(temp_word)
    print(temp_word, temp_word_len)
    if temp_word_len > len(longest_word):
        longest_word = temp_word

print("Longest word is", longest_word)
print("--------------------------")

my_list = ['fixture', 'dangerous', 'humanitarianism', 'trip', 'orange', 'cat', 'triskaidekaphobia', 'nominal', 'and', 'atomic']
print("Run #3")
longest_word = ""
for temp_word in my_list:
    temp_word_len = len(temp_word)
    print(temp_word, temp_word_len)
    if temp_word_len > len(longest_word):
        longest_word = temp_word

print("Longest word is", longest_word)
print("--------------------------")