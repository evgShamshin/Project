s = input()

'''data'''
s_len = len(s)# общее количество символов в строке
s_t3 = s * 3 # исходную строку повторенную 3 раза
s_1 = s[0]# первый символ строки
s_p3 = s[:3]# первые три символа строки
s_m3 = s[-3:]# последние три символа строки
_s = s[::-1]# строку в обратном порядке
s_0 = s[1:s_len - 1]# строку с удаленным первым и последним символом

print(s_len, s_t3, s_1, s_p3, s_m3, _s, s_0, sep = '\n')