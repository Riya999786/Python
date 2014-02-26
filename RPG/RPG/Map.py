__author__ = 'Joel Santiago'

from random import randint


class Map(object):

    def __init__(self, diff):
        self.difficulty = diff
        self.list = []
        self.blankList = []
        for i in xrange(10):
            self.list.append([])
            self.blankList.append([])
            for j in xrange(10):
                self.list[i].append(randint(1, self.difficulty))
                self.blankList[i].append("*")

    def displayMap(self, x):
        print "    ",
        for i in range(len(x)):
            print "C",
        print
        print "    ",
        for i in range(len(x)):
            print i,
        print
        print "    ",
        for i in range(len(x)):
            print "-",
        print
        for i in range(len(x)):
            print "R %d|" % i,
            for j in range(len(x[i])):
                print "%s" % x[i][j],
            print
        print
