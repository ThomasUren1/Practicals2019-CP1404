text = "this is a collection of words of nice words this is a fun thing it is"

text_to_count = text.split()
count_of_words = {}

for i in text_to_count:
    count = 0
    if i not in count_of_words:
        count = len([j for j in text_to_count if (j == i)])
        count_of_words[i] = count

max_length = len(max(text_to_count, key=len))
print('{}: {}'.format('Text', text))
[print("{:{}} : {}".format(name, max_length, count_of_words[name])) for name in sorted(count_of_words)]
