def show_menu():
      print("1.Citirea unei liste de numere intregi.")
      print("2.Afisati daca cele doua liste au acelasi numar par de elemente.")
      print("3.Afisarea unei liste ce reprezinta intersectia a doua liste.")
      print("4.Afisati toate palindroamele obtinute prin concatenarea tututor elementelor celor doua liste.")
      print("5.Cerinta 5")
      print("x.Iesire din program")


def read_date() :
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


def este_par(lst) :
    """

    :param lst: o lista de numere intregi
    :return: numarul de numere pare din lista
    """
    nr_pare = 0
    for i in lst :
        if i % 2 ==0 :
            nr_pare = nr_pare + 1
    return nr_pare


def test_este_par() :
    assert este_par([3,4,5,6]) == 2
    assert este_par([4,4,66,8,5]) == 4
    assert este_par([2,3,5,7,9]) == 1

def main() :
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
            if este_par(lst1_copy) == este_par(lst2_copy) :
                print("Da")
            else :
                print("Nu")
        if optiune == '3':
            pass
        if optiune == '4':
            pass
        if optiune == '5':
            pass
        if optiune == 'x':
            break


if __name__ == '__main__':
    test_este_par()
    main()