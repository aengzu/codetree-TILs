str = input()
n = int(input())

leng = len(str)
cnt = 0


#인덱스 lenng-1 부터 0까지 역순으로 .
for i in range(leng - 1, -1, -1):
	# 주어진 개수만큼 출력했을 경우 for문을 나갑니다.
	if cnt >= n:
		break
	print(str[i], end="")
	cnt += 1