# BOJ_1283
# 단축키 지정

def solution():
    n = int(input())
    word_list = [input().rstrip() for _ in range(n)]
    used_char = list()
    used_word_index = list()

    for i in range(n):
        if ' ' in word_list[i]:
            space_index = [idx for idx, char in enumerate(word_list[i]) if char == ' ']
            space_index.insert(0, -1)
            for j in space_index:
                j += 1
                if word_list[i][j].isupper():
                    if (word_list[i][j] not in used_char) and (word_list[i][j].lower() not in used_char):
                        used_char.append(word_list[i][j])
                        used_word_index.append(i)
                        word_list[i] = word_list[i][:j] + '[' + word_list[i][j] + ']' + word_list[i][j+1:]
                        break
                else:
                    if (word_list[i][j] not in used_char) and (word_list[i][j].upper() not in used_char):
                        used_char.append(word_list[i][j])
                        used_word_index.append(i)
                        word_list[i] = word_list[i][:j] + '[' + word_list[i][j] + ']' + word_list[i][j + 1:]
                        break

        for k in range(len(word_list[i])):
            if i in used_word_index:
                break
            elif word_list[i][k] == ' ':
                continue
            elif word_list[i][k].isupper():
                if (word_list[i][k] not in used_char) and (word_list[i][k].lower() not in used_char):
                    used_char.append(word_list[i][k])
                    word_list[i] = word_list[i][:k] + '[' + word_list[i][k] + ']' + word_list[i][k+1:]
                    break
            else:
                if (word_list[i][k] not in used_char) and (word_list[i][k].upper() not in used_char):
                    used_char.append(word_list[i][k])
                    word_list[i] = word_list[i][:k] + '[' + word_list[i][k] + ']' + word_list[i][k + 1:]
                    break

    for i in range(n):
        print(word_list[i])


if __name__ == "__main__":
    solution()
