# 큰 수부터 몫을 구하라
# 나머지 값으로 규칙을 반복하라

coin_list = [500, 100, 50, 10]
target = 1730
cnt = 0

for coin in coin_list:
    possible_cnt = target // coin

    cnt += possible_cnt
    target -= coin * possible_cnt

print(cnt)