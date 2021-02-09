def task_1(two_dim_words):
    """
        Здесь должен быть ваш код.
        Переменная two_dim_words - ваш двумерный список.
        Заполнять список значениями не нужно.
        Финальное значение должно быть помещено в переменную sorted_words.
        """
    
    pass

def task_3(numbers):
    """
        Здесь должен быть ваш код.
        Переменная numbers - ваша строка чисел.
        Финальное значение должно быть помещено в переменную dict_min.
        """
  
    print(numbers)
    numbers.isdigit()
    i = 0
    for i in range(len(numbers)):
        numbers.split()
        w = numbers.count('1')
        q = numbers.count('2')
        e = numbers.count('3')
        r = numbers.count('4')
        t = numbers.count('5')
        y = numbers.count('6')
        u = numbers.count('7')
        o = numbers.count('8')
        p = numbers.count('9')
        i += 1
    nums = dict([(1, w),
                 (2,q),
                 (3,e),
                 (4,r),
                 (5,t),
                 (6,y),
                 (7,u),
                 (8,o),
                 (9,p)])
    for m in nums.values():
        i+1
    v=max(nums.values())
    list(nums.values())
    nums.values().pop(v)
    l=max(nums.values())
    nums.values().pop(l)
    a=max(nums.values())

    pass


def task_4_1(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_2(words):  # можно сделать тесты
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_4_3(words):
    """
        Здесь должен быть ваш код.
        Переменная words - ваш кортеж слов из задания.
        Финальное значение должно быть помещено в переменную res.
        """

    return res


def task_5(lst1, lst2):
    """
        Здесь должен быть ваш код.
        Переменные lst1 и lst2 - два данных списка.
        Финальное значение должно быть помещено в переменную diff.
        """
    
    s_f_l=set(lst1)
    s_f_l_1=set(lst2)
    con = s_f_l.symmetric_difference(s_f_l_1)
    a=list(con)
    a.sort(reverse=False)
    return a


def task_6(lst):
    """
        Здесь должен быть ваш код.
        Переменная lst - ваш список.
        Финальное значение должно быть помещено в переменную res.
        """

    m=set(lst)
    n=list(m)
    n.sort(reverse=True)
    n=tuple(n)

    return n

