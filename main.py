class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)
        self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and isinstance(g, int) and isinstance(b, int)
                and 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Некорректные значения цвета. Цвет не изменен.")

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides):
            return True
        else:
            return False

    def get_sides(self):
        if self.sides_count == 12:
            return [self.__sides[0]] * self.sides_count
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print(f"Количество сторон должно быть равно {self.sides_count}. Стороны не изменены.")


class Circle(Figure):
    sides_count = 1

    def get_radius(self):
        return self.__sides[0]

    def set_radius(self, value):
        self.__sides[0] = value

    def get_square(self):
        return 3.14 * self.__sides[0] ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, s1, s2, s3):
        super().__init__(color, s1, s2, s3)
        self.__s1, self.__s2, self.__s3 = s1, s2, s3

    def get_square(self):
        p = len(self) / 2
        return (p * (p - self.__s1) * (p - self.__s2) * (p - self.__s3)) ** 0.5

    def get_height(self):
        __height = (self.__s1 + self.__s2 + self.__s3) / 2
        return 2 * self.get_square() / self.__s1


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())

circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Проверка Треугольника:
triangle1 = Triangle((66, 55, 13), 3, 4, 5)
print(triangle1.get_square())
print(triangle1.get_height())
