class MyInt:
    def __init__(self, num):
        self.num = num
        self.romannum = {
            "M" : 1000,
            "CM" : 900,
            "D" : 500,
            "CD" : 400,
            "C" : 100,
            "XC" : 90,
            "L" : 50,
            "XL" : 40,
            "X" : 10,
            "IX" : 9,
            "V" : 5,
            "IV" : 4,
            "I" : 1
        }
    def __add__(self, object2):
        return MyInt(int((self.num + object2.num)*1.5))
    
    def toRoman(self):
        num_temp = self.num
        romanshow= ""
        while num_temp > 0 :
            for key , num in self.romannum.items() :
                if num <= num_temp :
                    romanshow = romanshow + key
                    num_temp  -= num 
                    break
        return romanshow
print(" *** class MyInt ***")
num1, num2, = [int(x) for x in input('Enter 2 number : ').split()]
a = MyInt(num1)
b = MyInt(num2)
print(f'{a.num} convert to Roman : {a.toRoman()}')
print(f'{b.num} convert to Roman : {b.toRoman()}')
print(f'{a.num} + {b.num} = {(a+b).num}')

    
