__author__ = 'Joel Santiago'

import pickle
import os.path
from tkinter import *
import tkinter.messagebox


class Address:
    def __init__(self, name, number, street, city, state, zipcode):
        self.name = name
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode


class AddressBook:
    def __init__(self):
        window = Tk()
        window.title = "Address Book"

        self.nameVar = StringVar()
        self.numberVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Name").grid(row=1, column=1, sticky=W)
        Entry(frame1, textvariable=self.nameVar, width=40).grid(row=1, column=2)

        frame2 = Frame(window)
        frame2.pack()
        Label(frame2, text="Number").grid(row=1, column=1, sticky=W)
        Entry(frame2, textvariable=self.numberVar, width=40).grid(row=1, column=2)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="Street").grid(row=1, column=1, sticky=W)
        Entry(frame3, textvariable=self.streetVar, width=40).grid(row=1, column=2)

        frame4 = Frame(window)
        frame4.pack()
        Label(frame4, text="City", width=5).grid(row=1, column=1, sticky=W)
        Entry(frame4, textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame4, text="State").grid(row=1, column=3, sticky=W)
        Entry(frame4, textvariable=self.stateVar, width=5).grid(row=1, column=4)
        Label(frame4, text="ZIP").grid(row=1, column=5, sticky=W)
        Entry(frame4, textvariable=self.zipVar, width=5).grid(row=1, column=6)

        frame5 = Frame(window)
        frame5.pack()
        Button(frame5, text="Add", command=self.processAdd).grid(row=1, column=1)
        btFirst = Button(frame5, text="First", command=self.processFirst).grid(row=1, column=2)
        btPrevious = Button(frame5, text="Previous", command=self.processPrevious).grid(row=1, column=3)
        btNext = Button(frame5, text="Next", command=self.processNext).grid(row=1, column=4)
        btLast = Button(frame5, text="Last", command=self.processLast).grid(row=1, column=5)

        self.addressList = self.loadAddress()
        self.current = 0

        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop()

    def saveAddress(self):
        outfile = open("address.dat", "wb")
        pickle.dump(self.addressList, outfile)
        tkinter.messagebox.showinfo("Address saved", "A new address is saved")
        outfile.close()

    # TODO replace load from address.dat with create and load from sqlite db file
    def loadAddress(self):
        if not os.path.isfile("address.dat"):
            return []

        try:
            infile = open("address.dat", "rb")
            addressList = pickle.load(infile)
        except EOFError:
            addressList = []

        infile.close()
        return addressList

    # TODO replace add address process with write to sqlite db file
    def processAdd(self):
        address = Address(self.nameVar.get(), self.numberVar.get(), self.streetVar.get(), self.cityVar.get(),
                          self.stateVar.get(), self.zipVar.get())
        self.addressList.append(address)
        self.saveAddress()

    def processFirst(self):
        self.current = 0
        self.setAddress()

    def processNext(self):
        if self.current < len(self.addressList) - 1:
            self.current += 1
            self.setAddress()

    def processPrevious(self):
        if self.current > 0:
            self.current -= 1
            self.setAddress()

    def processLast(self):
        self.current = len(self.addressList) - 1;
        self.setAddress()

    def setAddress(self):
        self.nameVar.set(self.addressList[self.current].name)
        self.numberVar.set(self.addressList[self.current].number)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)

AddressBook()