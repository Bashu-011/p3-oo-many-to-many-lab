# class Author:
#     def __init__(self, name):
#         self.name = name
#         self._contracts = []

#     def contracts(self):
#         return self._contracts

#     def books(self):
#         return [contract.book for contract in self._contracts]

#     def sign_contract(self, book, date, royalties):
#         contract = Contract(self, book, date, royalties)
#         self._contracts.append(contract)
#         return contract

#     def total_royalties(self):
#         total = sum(contract.royalties for contract in self._contracts)
#         return total


# class Book:
#     def __init__(self, title):
#         self.title = title


# class Contract:
#     all = []

#     def __init__(self, author, book, date, royalties):
#         self.author = None
#         self.book = None
#         self.date = None
#         self.royalties = None
#         self.set_author(author)
#         self.set_book(book)
#         self.set_date(date)
#         self.set_royalties(royalties)
#         type(self).all.append(self)

#     @classmethod
#     def contracts_by_date(cls, date):
#         return [contract for contract in cls.all if contract.date == date]

#     def set_author(self, author):
#         if not isinstance(author, Author):
#             raise ValueError("Author must be an instance of Author")
#         self.author = author

#     def set_book(self, book):
#         if not isinstance(book, Book):
#             raise ValueError("Book must be an instance of Book")
#         self.book = book

#     def set_date(self, date):
#         if not isinstance(date, str):
#             raise ValueError("Date must be a string")
#         self.date = date

#     def set_royalties(self, royalties):
#         if not isinstance(royalties, int) and not isinstance(royalties, float):
#             raise ValueError("Royalties must be a number")
#         self.royalties = royalties


# class Author:
#     def __init__(self, name):
#         self.name = name

#     def contracts(self):
#         return [contract for contract in Contract.all if contract.author == self]

#     def books(self):
#         return [contract.book for contract in self.contracts()]

#     def sign_contract(self, book, date, royalties):
#         contract = Contract(self, book, date, royalties)
#         return contract

#     def total_royalties(self):
#         return sum(contract.royalties for contract in self.contracts())
#     pass

# class Book:
#     def __init__(self, title):
#         self.title = title

#     def contracts(self):
#         return [contract for contract in Contract.all if contract.book == self]

#     def authors(self):
#         return [contract.author for contract in self.contracts()]
#     pass  

# class Contract:
#     all = []

#     def __init__(self, author, book, date, royalties):
#         if not isinstance(author, Author):
#             raise TypeError("Author must be an instance of Author class")
#         if not isinstance(book, Book):
#             raise TypeError("Book must be an instance of Book class")
#         if not isinstance(date, str):
#             raise TypeError("Date must be a string")
#         if not isinstance(royalties, int):
#             raise TypeError("Royalties must be an integer")

#         self.author = author
#         self.book = book
#         self.date = date
#         self.royalties = royalties
#         Contract.all.append(self)

#     @classmethod
#     def contracts_by_date(cls, date):
#         return sorted(cls.all_contracts, key=lambda contract: contract.date)
#     pass

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise TypeError("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(royalties, int) and not isinstance(royalties, float):  # Adjusted to check for float as well
            raise TypeError("Royalties must be an integer or float")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
