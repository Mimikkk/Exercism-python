class Garden:
    def __init__(self, diagram, students = None):
        self.__students = sorted(students) if students else ["Alice", "Bob", "Charlie", "David",
                                                    "Eve", "Fred", "Ginny", "Harriet",
                                                    "Ileana", "Joseph", "Kincaid", "Larry"]
        self.__plants = {'G': 'Grass', 'V': 'Violets', 'C': 'Clover', 'R': 'Radishes'}
        self.__student_plants: dict = {}

        (self.__row_1, self.__row_2) = map(lambda x: tuple(x[i:i+2] for i in range(0, len(x), 2)), diagram.split('\n'))

    def plants(self, name):
        i = self.__students.index(name)
        return list(map(lambda x: self.__plants[x], self.__row_1[i]+self.__row_2[i]))
