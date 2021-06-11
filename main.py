from pprint import pprint

if __name__ == '__main__':
    # Better coding style: put constant out of the function
    SPECIAL_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    file_name = 'gem_text.txt'
    nu = []
    # freqEng = [8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2, 6.1, 7, 0.2, 0.8, 4,
    #            2.4, 6.8, 7.5, 1.9, 0.1, 6, 6.3, 9.1, 2.8, 1, 2.4, 0.2, 2, 0.1]

    freqEng_wik = [8.17, 1.49, 2.78, 4.25, 12.7, 2.23, 2.02, 6.09, 6.97, 0.15,
                   0.77, 4.03, 2.41, 6.75, 7.51, 1.93, 0.1, 5.99, 6.33, 9.06, 2.76, 0.98, 2.36, 0.15, 1.97, 0.05]

    # подсчет количества символов в тексте
    def count_symbols(filename):
        with open(filename) as infile:
            lines = 0
            words = 0
            characters = 0
            for line in infile:
                wordslist = line.split()
                lines = lines + 1
                words = words + len(wordslist)
                characters += sum(len(word) for word in wordslist)
            # print(lines)
            # print(words)
            # print(characters)
            return characters

    # функция для подсчета частоты каждой буквы в тексте и записи в файл
    def count_special_chars(filename):
        with open(filename) as f:
            content = f.read()
            d = dict([(i, content.count(i)) for i in SPECIAL_CHARS])
        with open('out.txt', 'w') as out:
            out.write('frequency of each symbol: \n')
            for key, val in d.items():
                out.write('{} : {}\n'.format(key, val))
            return d

    # функция для записи в файл суммарных частот строчных и прописных символов
    def export_all_chars(obj):
        with open('all_chars.txt', 'w') as out:
            out.write('Lowercase and uppercase character frequencies from A to Z: \n')
            for val in obj:
                out.write('{} \n'.format(val))


    def count_of_letters(obj):
        s = 0
        for j in range(len(obj)):
            s += obj[j]
        return s

    # считаем статистику
    def calculate_chi(nu_, count_, freq_):
        chi = 0
        for i in range(len(freq_)):
            chi += ((nu_[i] - count_ * (freq_[i] / 100)) ** 2) / (
                    count_ * (freq_[i] / 100))
        return chi


    dict1 = count_special_chars(file_name)

    small_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w',
                     'x', 'y', 'z']

    big_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                   'U', 'V', 'W',
                   'X', 'Y', 'Z']

    for i in range(len(small_letters)):
        nu.append(dict1[small_letters[i]] + dict1[big_letters[i]])

    count_of_letters = count_of_letters(nu)

    # Записываем в файл частоту каждой буквы в алфавитном порядке
    export_all_chars(nu)

    print('Количество букв в тексте: ' + str(count_of_letters))

    # pprint(count_special_chars(file_name))

    chi = calculate_chi(nu, count_of_letters, freqEng_wik)
    print('Статистика: ' + str(chi))

    # объединенные буквы
    freq_union = dict(zip(small_letters, nu))
    # pprint(freq_union)

    dict_freq_small_upper = dict(zip(small_letters, freqEng_wik))
    sorted_tuples = sorted(dict_freq_small_upper.items(), key=lambda item: item[1])
    # сортируем словарь по возрастанию среднестатистической частоты буквы
    sorted_dict = {k: v for k, v in sorted_tuples}

    # объединяем буквы таким образом, чтобы среднестатистическая вероятность была равна примерно 10
    d = []
    ss = []
    ss_freq = []
    summ_freq = 0
    str_ = ''
    k = 0
    summ = 0
    for i in sorted_dict:
        summ_freq += freq_union[i]
        str_ += i
        summ += sorted_dict[i]
        if summ > 7:
            d.append(str_)
            ss.append(summ)
            ss_freq.append(summ_freq)
            str_ = ''
            summ = 0
            summ_freq = 0
            k = k + 1

    # Объединяем в словари теоретические частоты и частоты букв в тексте для групп букв
    dict2_union_freq = dict(zip(d, ss))
    dict2_union_nu = dict(zip(d, ss_freq))

    # pprint(dict2_union_nu)

    chi_union = calculate_chi(list(dict2_union_nu.values()), count_of_letters, list(dict2_union_freq.values()))
    print('Статистика для объединенных букв: ' + str(chi_union))
