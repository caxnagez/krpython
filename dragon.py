class Dragon:
    def __init__(self, height, danger, color):
        self.height = height
        self.danger = danger
        self.color = color
        
    def __lt__(self, other): #сравнение
        if self.height != other.height:
            return self.height < other.height
        if self.danger != other.danger:
            return self.danger < other.danger
        return self.color < other.color
    def __eq__(self, other): #чек равенства
        return (self.height == other.height and self.danger == other.danger and self.color == other.color)
    def __gt__(self, other):
        return not self < other and not self == other
    def __le__(self, other):
        return self < other or self == other
    def __add__(self, other): #сложение
        new_height = (self.height + other.height) // 2
        new_danger = max(self.danger, other.danger)
        new_color = min(self.color, other.color)
        return Dragon(new_height, new_danger, new_color)
    def __sub__(self, number): #число - дракон
        new_height = self.height - (self.height // number)
        new_danger = self.danger + (self.danger % number)
        if new_danger < 0:
            new_danger = 0
        return Dragon(new_height, new_danger, self.color)
    def __mod__(self, number):#дракона на число
        return [Dragon(self.height % number, self.danger // number, self.color) for _ in range(number)]
    def __call__(self, string):
        return string * self.danger
    def change_color(self, new_color): #чейнж цвета
        if self.danger > 0:
            self.danger -= 1
        self.color = new_color
    def __str__(self): #представление дракона
        return f"Dragon with height {self.height}, danger {self.danger} and color {self.color}."
    def __repr__(self): #официальное представление
        return f"Dragon({self.height}, {self.danger}, '{self.color}')"

dr = Dragon(69, 5, "brown")
dr1 = Dragon(69, 5, "gray")
print(dr > dr1, dr != dr1, dr <=
dr1)
print(dr, dr1, sep="\n")
print()
dr -= 23
dr1 -= 2
dr2 = dr + dr1
print(dr, dr1, dr2, sep="\n")
dr = Dragon(35, 7, "beige")
dr1 = Dragon(17, 1, "cyan")
print(dr > dr1, dr != dr1, dr <= dr1) 
print(dr, dr1, sep="\n")
print()
dr.change_color("white")
dr1.change_color("red")
dr1.change_color("gold")
print(dr, dr1, sep="\n")
print()
res = dr % 4
res[0] -= 2
print(res)
print(dr("Welcome"), sep="\n")
