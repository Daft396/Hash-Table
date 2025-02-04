class hash_table:
    def __init__(self,size):
        self.__table = [None] * size
        self.__key = size
        self.__maxsize = size
        self.__size = 0

    def show(self):
        print(self.__table)

    def store(self,item):
        if self.__size == self.__maxsize:
            print('Table is full')
            return
        address = item%self.__key
        print(address)

        while self.__table[address] is not None:
            address = (address+1) % self.__maxsize
        self.__table[address] = item
        self.__size +=1

    def search(self,item):
        address = item % self.__key
        if self.__table[address] is None:
            print("Item is not in the list")
            return
        while self.__table[address] is not None and self.__table[address] is not item:
            address = (address+1) % self.__maxsize
            self.__table[address] = item
            self.__size +=1
            if self.__table[address] is item:
                return True
            else:
                continue

    def delete(self,item):
        
hash1 = hash_table(11)

hash1.store(28)
hash1.store(29)
hash1.store(2345)
hash1.store(223)
hash1.show()
