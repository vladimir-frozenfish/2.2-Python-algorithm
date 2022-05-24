quantity = int(input()) 						# количество карточек
moves = int(input()) 							# количество ходов
cards_list = list(map(int, input().split()))	# список карточек

summa = 0										# сумма выбранных карточек
left = 0
right = quantity-1

right_summa = sum(cards_list[-1:-moves-1:-1])
summa = max(sum(cards_list[:moves]), right_summa)
left_summa = 0
for i in range(1, moves):
    left_summa += cards_list[i-1]
    right_summa -= cards_list[-(moves-i+1)]
    summa = max(summa, left_summa + right_summa)

print(summa)