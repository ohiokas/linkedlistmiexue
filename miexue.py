class Node:
    def __init__(self, menu, harga):
        self.menu = menu
        self.harga = harga
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_pesanan(self, menu, harga):
        new_node = Node(menu, harga)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
def tampilkan_pesanan(self):
        current = self.head
        if not current:
            print("Keranjang masih kosong")
        else:
            index = 1
            while current:
                print(f"{index}. {current.menu} {current.harga} rupiah")
                current = current.next
                index += 1

    def total_harga(self):
        current = self.head
        total = 0
        while current:
            total += current.harga
            current = current.next
        return total
