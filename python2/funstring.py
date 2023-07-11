class FunString:

    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

    def size(self):
        return len(self.string)

    def change_size(self):
        ch_size = ""
        for char in self.string:
            if char.islower():
                ch_size += char.upper()
            else:
                ch_size += char.lower()
        return ch_size

    def reverse(self):
        rev = ""
        i = len(self.string) - 1
        while i >= 0:
            rev += self.string[i]
            i -= 1
        return rev

    def deleteSame(self):
        delete = ""
        text = []
        for i in self.string:
            if i not in text:
                text.append(i)
                delete += i
        return delete

str1, str2 = input("Enter String and Number of Function : ").split()
res = FunString(str1)
if str2 == "1":
    print(res.size())
elif str2 == "2":
    print(res.change_size())
elif str2 == "3":
    print(res.reverse())
elif str2 == "4":
    print(res.deleteSame())