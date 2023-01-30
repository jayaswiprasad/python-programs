def minion_game(string):
    string = string.upper()
    vowels = 'AEIOU'
    kevin_score, stuart_score = 0, 0
    str_len = len(string)
    
    for i in range(0, str_len):
        if string[i] in vowels:
            kevin_score += str_len-i
        else:
            stuart_score += str_len-i

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif kevin_score < stuart_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

