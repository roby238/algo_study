# BOJ_1713
# 후보 추천하기

def solution():
    frame_num = int(input())
    rec_num = int(input())
    rec = [int(i) for i in input().split()]
    # key = 후보 번호, value = [추천 수, 추천된 시각]
    frame = dict()

    for i in range(rec_num):
        if rec[i] in frame:
            frame[rec[i]][0] += 1
        else:
            if len(frame) < frame_num:
                frame[rec[i]] = [1, i]
            else:
                # 정렬(nlogn)하는 것보다 반복문(n)으로
                # 삭제할 key를 찾는 것이 빠를 것 같아서 수정했으나 백준 결과는 차이 없음
                # 사진틀의 수가 최대 20개로 작은 수 이므로 nlogn과 n의 차이가 미세하기 때문?
                # frame = dict(sorted(frame.items(), key=lambda x: (x[1][0], x[1][1])))
                # target_key = list(frame.keys())[0]
                target_key = None
                for key in frame:
                    if (target_key is None or
                            frame[target_key][0] > frame[key][0] or
                            (frame[target_key][0] == frame[key][0] and frame[target_key][1] > frame[key][1])):
                        target_key = key
                del frame[target_key]
                frame[rec[i]] = [1, i]

    frame = dict(sorted(frame.items()))
    for key in frame:
        print(key, end=" ")


if __name__ == "__main__":
    solution()
