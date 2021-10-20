def show_menu():
    print("1.Citirea unei liste de numere intregi.")
    print("2.Afisati daca cele doua liste au acelasi numar par de elemente.")
    print("3.Afisarea unei liste ce reprezinta intersectia a doua liste.")
    print("4.Afisati toate palindroamele obtinute prin concatenarea tututor elementelor de pe aceleasi pozitii din cele doua liste.")
    print("5.Cerinta 5")
    print("x.Iesire din program")


def read_date():
    lst = []
    lst_str = input("Introduceti lista cu numere intregi: ")
    lst_str_split = lst_str.split(',')
    for number in lst_str_split:
        lst.append(number)
    return lst


def convert_list_str_to_int(lst):
    """
    Converteste elementele de tip str in elemente de tipp int
    :param lst: Lista de convertit
    :return: Returneaza lista cu elementele convertite in int
    """
    list_int = []
    for i in lst:
        list_int.append(int(i))

    return list_int


def este_par(lst):
    """

    :param lst: o lista de numere intregi
    :return: numarul de numere pare din lista
    """
    nr_pare = 0
    for i in lst:
        if i % 2 == 0:
            nr_pare = nr_pare + 1
    return nr_pare


def test_este_par():
    assert este_par([3, 4, 5, 6]) == 2
    assert este_par([4, 4, 66, 8, 5]) == 4
    assert este_par([2, 3, 5, 7, 9]) == 1


def intersc_elem(lst1, lst2):
    """

    :param lst1: O lista de numere intregi
    :param lst2: O lista de numere intregi
    :return: Intersectia celor doua liste introduse ca parametrii
    """
    lst_rezult = []
    for i in lst1:
        for j in lst2:
            if i == j and i not in lst_rezult:
                lst_rezult.append(i)
    return lst_rezult


def test_intersec_elem():
    assert intersc_elem([2, 5, 7, 8], [2, 3, 4, 5]) == [2, 5]
    assert intersc_elem([1, 2, 3], [1, 2, 3, 4, 5, 6]) == [1, 2, 3]
    assert intersc_elem([12, 22, 36, 424], [22, 36, 55, 23, 424]) == [22, 36, 424]


def is_palindrome(n):
    # Determina daca un numar este palindrom dau sau nu
    copie_n = n
    oglindit = 0
    while n:
        oglindit = oglindit * 10 + n % 10
        n = n // 10
    if (copie_n == oglindit):
        return True
    return False


def palidroms_from_all_lsts(lst1, lst2):
    """

    :param lst1: O lista de numere intregi
    :param lst2: A doua lista de numere intregi
    :return: Returneaza o lista cu palindroamele formate prin concatenarea elementelor de pe aceleasi pozitii din cele doua liste
    """
    cont = 0
    rezult_lst = []
    if len(lst1) > len(lst2):
        aux = lst1
        lst1 = lst2
        lst2 = aux
    for i in range(len(lst1)):
        cont = int(str(lst1[i]) + str(lst2[i]))
        if is_palindrome(cont):
            rezult_lst.append(cont)
    return rezult_lst


def test_palidroms_from_all_lsts() :
    assert palidroms_from_all_lsts([21, 23, 63, 55, 424], [12, 22, 36, 11]) == [1221, 3663]
    assert palidroms_from_all_lsts([21, 44, 33, 5, 3], [12, 7, 3]) == [1221, 333]


def main():
    lst1 = []
    lst2 = []
    lst1_copy = []
    lst2_copy = []
    while True:
        show_menu()
        optiune = input("Introduceti optiunea dorita: ")
        if optiune == '1':
            lst1 = read_date()
            lst2 = read_date()
            lst1_copy = convert_list_str_to_int(lst1)
            lst2_copy = convert_list_str_to_int(lst2)
        if optiune == '2':
            if este_par(lst1_copy) == este_par(lst2_copy):
                print("Da")
            else:
                print("Nu")
        if optiune == '3':
            print(intersc_elem(lst1_copy, lst2_copy))
        if optiune == '4':
            print(palidroms_from_all_lsts(lst1_copy, lst2_copy))
        if optiune == '5':
            pass
        if optiune == 'x':
            break


if __name__ == '__main__':
    test_este_par()
    test_intersec_elem()
    test_palidroms_from_all_lsts()
    main()
