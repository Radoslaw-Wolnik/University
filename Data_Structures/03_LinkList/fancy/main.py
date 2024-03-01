from fancy.AddableLinkList import AddableLinkList as LinkListAdd
from fancy.ReversibleLinkList import ReversibleLinkList as LinkListRev

if __name__ == 'main':
    # test addableLinkList -----------------------------------
    Uno = LinkListAdd()
    Dos = LinkListAdd()
    Uno.add_last(2)
    Uno.add_last(4)
    Uno.add_last(3)
    Dos.add_last(5)
    Dos.add_last(6)
    Dos.add_last(4)
    Tres = Uno + Dos
    print(Tres)

    Uno = LinkListAdd()
    Dos = LinkListAdd()
    Uno.add_last(1)
    Uno.add_last(1)
    Uno.add_last(1)
    Uno.add_last(3)
    Uno.add_last(3)
    Uno.add_last(3)

    Dos.add_last(1)
    Dos.add_last(1)
    Dos.add_last(1)
    Tres = Uno + Dos
    print(Tres)

    # test reversable Link List -------------------------------
    S = LinkListRev()
    S.add_first('1')
    S.add_last('2')
    S.add_last('3')
    S.add_last('4')
    S.add_last('5')
    S.add_last('6')
    print(S)
    S.reverse_self()
    print(S)
    S.del_at_position(0)
    print(S)
    S.reverse_one()
    print(S)
