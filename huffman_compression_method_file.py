import os
from queue import PriorityQueue


class Node:
    value = 0
    right = None
    left = None
    character = ""

    def isLeaf(self):  # sprawdzenie czy są znaki
        return self.character != ""

    def __init__(self, val, ch):  # def konstruktor
        self.value = val
        self.character = ch

    # sprawdzenie czy nie ma 2 takich samych znaków i ew uporządkowanie ich
    def __lt__(self, other):
        if self.value != other.value:  # wykonujemy normalne porównanie, jeżeli liście są różne;
            return self.value > other.value
        if not self.isLeaf() and other.isLeaf():
            return True
        if self.isLeaf() and not other.isLeaf():
            return False
        if self.isLeaf() and other.isLeaf():  # jeżeli jednak oba maja znak, to decyduje kolejność alfabetyczna
            return ord(self.character[0]) > ord(other.character[0])
        return True


# zwraca korzen drzewa
def createTree(text):
    occurences = {}
    for c in text:  # zliczamy wystąpienia każdego znaku w tekście
        if occurences.__contains__(c):
            occurences[c] += 1
        else:
            occurences[c] = 1
    # PriorityQueue działa jak taki stos, zawsze na górze ma najmniejsza wartoc
    nodes = PriorityQueue()
    for c in occurences.keys():  # tworzymy liście drzewa, bazując na znakach i ich ilości wystąpień,
        node = Node(occurences[c], c)  # a następnei dodajmy do listy
        nodes.put(node)
    root_node = None  # docelowy korzen drzewa
    while nodes.qsize() > 1:  # następnie iterujemy, dopóki w nodes nie zostanie ostatni element - korzeń drzewa
        n1 = nodes.get()  # pobieramy pierwszy, najmniejszy element z PriorityQueue
        n2 = nodes.get()  # pobieramy kolejny, najmniejszy element z PriorityQueue
        # jeżeli oba liście mają tą samą wartość, a jeden z nich jest kontenerem,
        # to powinien on być traktowany jako większy element

        parent = Node(n1.value + n2.value, "")  # tworzymy liść-kontener, będzie przechowywać dwa n1, n2 i sumę
        root_node = parent  # ustawiamy go na aktualny korzen
        parent.left = n1  # i dodajemy mu dzieci
        parent.right = n2
        nodes.put(parent)  # a następnie dodajemy go do PriorityQueue
    return root_node  # nasze drzewo jest gotowe - zwracamy korzeń


# tworzy drzewo i od razu koduje każdy ze znaków
def encodeValues(n, str, txt):
    if n is None:
        return txt
    if n.isLeaf():
        print(n.character + " : " + str)
        txt = txt.replace(n.character, str)
    txt = encodeValues(n.left, str + "0", txt)
    txt = encodeValues(n.right, str + "1", txt)
    return txt


# definiujemy funkcję, która odkoduje tekst na bazie utworzonego drzewa
def decode(root, text):
    decoded = ""
    curr_node = root
    for char in text:
        if char == '0':
            if curr_node.left.isLeaf():
                decoded += curr_node.left.character
                curr_node = root
            else:
                curr_node = curr_node.left
        else:
            if curr_node.right.isLeaf():
                decoded += curr_node.right.character  # to dodajemy jego znak do zmiennej pomocniczej
                curr_node = root  # a następnie wracamy na początek drzewa
            else:
                curr_node = curr_node.right  # jeżeli trafiliśmy na kontener, to od niego zaczniemy nast. iterację
    return decoded  # zwracamy odkodowana wartosc


file_path = "1_wers.txt"
with open(file_path, 'r') as file:
    word = file.read().rstrip()

    root_node = createTree(word)
    print("Oto tablica kodowania:")
    word = encodeValues(root_node, "", word)
    print("Oto tekst po zakodowaniu: " + word)
    word = decode(root_node, word)
    print("Oto odkodowany tekst: " + word)
    print("--------------------")