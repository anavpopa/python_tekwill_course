#Ex 1 Write a program that will count number of lines in a file
count = 0
with open('Jingle_Bells.txt', 'r') as f:
    for line in f:
        count += 1
print(count)


#Ex 2 Write a program that will count frequency of a word in a file
word='is'
count_word=0
with open('Jingle_Bells.txt', 'r') as f:
    for line in f:
        count_word=count_word+line.count(word)
    print(count_word)


#Ex 3 Write a program that will append new content to the end of a file
with open('Jingle_Bells.txt', 'a') as f:
    f.write('\n \nSongwriters: BRION JON / Traditional / DP')
    f.close()


#Ex 4 Write a program that will remove newline character from a file.
with open('Jingle_Bells.txt', 'r') as f1:
    content=f1.read()
    with open('Jingle_Bells.txt', 'w') as f2:
        f2.write(content.replace('\n',' '))
    