class MyInt:
    def __init__(self,value) -> None:
        self.value = value
    def toRoman(self):
        value = self.value
        s=""
        romanvalue = {
            "M" : 1000,
            "CM": 900 ,
            "D" : 500 ,
            "CD": 400 ,
            "C" : 100 ,
            "XC": 90  ,
            "L" : 50  ,
            "XL": 40  ,
            "X" : 10  ,
            "IX": 9   ,
            "VII":7   ,
            "VI": 6   ,
            "V" : 5   ,
            "IV": 4   ,
            "I" : 1   ,
        }

        for i in romanvalue: 
            while value >= romanvalue[i]:
                value -= romanvalue[i]
                s += i
    
        return s

    def __add__(self,adder):
        add = self.value + adder.value
        add += add/2
        return int(add)
a,b = [MyInt(int(e)) for e in input(" *** class MyInt ***\nEnter 2 number : ").split()]
print("{} convert to Roman : {}".format(a.value,a.toRoman()))
print("{} convert to Roman : {}".format(b.value,b.toRoman()))
print(a.value,"+",b.value,"=",a+b)

