#Ex 1
# count = 0
# with open('Jingle_Bells.txt', 'r') as f:
#     for line in f:
#         count += 1
# print(count)


#Ex 2
# word='is'
# count_word=0
# with open('Jingle_Bells.txt', 'r') as f:
#     for line in f:
#         count_word=count_word+line.count(word)
#     print(count_word)


#Ex 3
# with open('Jingle_Bells.txt', 'a') as f:
#     f.write('\n \nSongwriters: BRION JON / Traditional / DP')
#     f.close()


#Ex 4
# with open('Jingle_Bells.txt', 'r') as f1:
#     content=f1.read()
#     with open('Jingle_Bells.txt', 'w') as f2:
#         f2.write(content.replace('\n',''))
    