# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Пример:
# Входные данные:
# 'ываабв лповап абвцукв алоабвабв ываываыв'
# Выходные данные:
# 'лповап ываываыв'


def f(word):
    if word.find('абв') == -1:
        return True
    else:
        return False


st = 'ываабв лповап абвцукв алоабвабв ываываыв'
st = st.split(' ')

total = list(filter(f, st))
print(total)
