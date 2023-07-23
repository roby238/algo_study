n = int(input()) # 사진틀 갯수
v = int(input()) # 총 추천 횟수
result = [] # 후보 넣을 리스트
vote = [] # 추천 수 넣을 리스트
candidate = list(map(int,(input().split()))) # 추천받기

for c in candidate:
  if c not in result: # 추천 안 받았던 학생이라 추가해야하는 경우
    if len(result) >= n: # 이미 사진틀이 꽉 차 있으면
      for i in range(n):
        if min(vote) == vote[i]: # 가장 작은 추천 수에 해당하는 최초 인덱스를 찾아서
          del result[i] # 후보 삭제
          del vote[i] # 추천 수 삭제
          break # 최초 삭제했으면 빠져나오기
    result.append(c) # 새로운 학생후보 추가
    vote.append(1) # 추천 수 1 추가
  else: # 이미 사진틀에 존재하는 경우
    vote[result.index(c)] += 1 # 해당 후보학생의 추천수만 1 증가
      
result.sort() #정렬
print(' '.join(map(str,result))) # 출력
