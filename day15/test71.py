#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student:
    name = ""
    age = 0
    score = [None] * 4

    def input(self):
        self.name = raw_input("Input name, please: ")
        self.age = int(raw_input("Input age, please: "))
        for i in range(len(self.score)):
            self.score[i] = int(raw_input("Input %d score, please: " % (i + 1)))

    def output(self):
        print 'Output name: %s' % self.name
        print 'Output age: %d' % self.age
        for i in range(len(self.score)):
            print 'Output %d score: %d' % ((i + 1), self.score[i])


if __name__ == "__main__":
    N = 5
    studentArray = [Student()] * N
    for i in range(len(studentArray)):
        studentArray[i].input()

    for i in range(len(studentArray)):
        studentArray[i].output()