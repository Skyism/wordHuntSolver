def main():
    from trie import Node, Trie
    from board import Board
    #change size here
    sidelength = 4

    #opens file
    words = open("newdict.txt", "rt")

    #creates new trie
    trie = Trie()

    for x in words:
        word = x.strip().lower()
        trie.insert(word)

    #creates new Board
    letters = input("Insert Word Hunt Board Here")
    board = Board()
    board.createBoard(letters, sidelength)
    final = board.findallpath(trie)

    #sorting final
    final = sorted(final, key=len, reverse=False)
    for x in final:
        print(x)

main()


