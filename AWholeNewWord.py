from collections import defaultdict
from itertools import product

T = int(input())
for i in range(1, T + 1):
    [N, L] = [int(i) for i in input().split()]
    words = []
    for j in range(N):
        words.append(input())
    
    letters_position = list()
    letters_count_position = list()
    for j in range(L):
        letters_position.append(set())
        letters_count_position.append(defaultdict(lambda: 0))

    for j in range(L):
        for word in words:
            letters_position[j].add(word[j])
            letters_count_position[j][word[j]] += 1
    
    all_possible_combinations = 1
    set_sizes = []
    for pos in letters_position:
        all_possible_combinations *= len(pos)
    
    if all_possible_combinations == N:
        print("Case #{}: {}".format(i, '-'))
        continue
    
    else:
        word = ""
        pos_words = letters_position[0]
        done = False
        for j in range(1, L):
            if done:
                word += list(letters_position[j])[0]
            else:
                pos_words = [''.join(p) for p in product(pos_words, letters_position[j])]
                word_starts = []
                for pw in pos_words:
                    found = False
                    for w in words: 
                        if w.startswith(pw):
                            found = True
                            break
                    if found == False:
                        word_starts.append(pw)
                if len(word_starts) > 0:
                    done = True
                    pos_words = word_starts
                    word = pos_words[0]

        if not done:
            final = set(pos_words) - set(words)
            print("Case #{}: {}".format(i, final.pop()))
        else:
            print("Case #{}: {}".format(i, word))
