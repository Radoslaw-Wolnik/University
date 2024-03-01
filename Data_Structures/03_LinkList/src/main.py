from LinkList import LinkList


if __name__ == '__main__':

    # test LinkList -----------------------------------------------------
    Lista01 = LinkList()
    Lista01.add_first('abc')
    Lista01.add_first('123')
    Lista01.add_first('zz')
    print(Lista01)
    Lista01.remove_first_el()
    print(Lista01)
    Lista01.del_last_el()
    print(Lista01)
    Lista01.add_first('12')
    Lista01.add_first('zz')
    print(Lista01)
    Lista01.insert_at_position('drugi', 1)
    print(Lista01)
    Lista01.del_at_position(1)
    print(Lista01)
