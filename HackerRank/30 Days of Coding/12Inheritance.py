class Person:
    def __init__(self, first_name, last_name, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.id_number = id_number

    def printPerson(self):
        print("Name:", self.last_name + ",", self.first_name)
        print("ID:", self.id_number)


class Student(Person):
    def __init__(self, first_name, last_name, id_number, scores):
        super().__init__(first_name, last_name, id_number)
        self.scores = scores

    def calculate(self):
        result = sum(scores) / len(scores)
        if 90 <= result <= 100:
            grade = 'O'
        elif 80 <= result < 90:
            grade = 'E'
        elif 70 <= result < 80:
            grade = 'A'
        elif 55 <= result < 70:
            grade = 'P'
        elif 40 <= result < 55:
            grade = 'D'
        else:
            grade = 'T'
        return grade


if __name__ == '__main__':
    line = input().split()
    first_name = line[0]
    last_name = line[1]
    idNum = line[2]
    numScores = int(input())
    scores = list(map(int, input().split()))
    s = Student(first_name, last_name, idNum, scores)
    s.printPerson()
    print("Grade:", s.calculate())
