# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
#60 -> 10 40 10
s = int(input("Введите кол-во журавликов: "))
a=int(s/3) # сколько каждый следал жур-в
b=int(a/2) # сколько жур-в сделали петя и сережа
c=int(b*4) 
print (f'Петя сделал {b} Катя сделала {c} сережа сделал {b}')



