__author__ = 'Joel Santiago'

import pickle
import os.path
from tkinter import *
import tkinter.messagebox


class Address:
    def __init__(self, firstname, lastname, number, street, city, state, zipcode):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.street = street
        self.city = city
        self.state = state
        self.zip = zipcode


class AddressBook:
    def __init__(self):
        window = Tk()
        window.title = "Address Book"

        self.firstnameVar = StringVar()
        self.lastnameVar = StringVar()
        self.numberVar = StringVar()
        self.streetVar = StringVar()
        self.cityVar = StringVar()
        self.stateVar = StringVar()
        self.zipVar = StringVar()

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="First").grid(row=1, column=1, sticky=W)
        Entry(frame1, textvariable=self.firstnameVar, width=20).grid(row=1, column=2)
        Label(frame1, text="Last").grid(row=1, column=3, sticky=W)
        Entry(frame1, textvariable=self.lastnameVar, width=20).grid(row=1, column=4)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="Number").grid(row=1, column=1, sticky=W)
        Entry(frame3, textvariable=self.numberVar, width=40).grid(row=1, column=2)

        frame4 = Frame(window)
        frame4.pack()
        Label(frame4, text="Street").grid(row=1, column=1, sticky=W)
        Entry(frame4, textvariable=self.streetVar, width=40).grid(row=1, column=2)

        frame5 = Frame(window)
        frame5.pack()
        Label(frame5, text="City", width=5).grid(row=1, column=1, sticky=W)
        Entry(frame5, textvariable=self.cityVar).grid(row=1, column=2)
        Label(frame5, text="State").grid(row=1, column=3, sticky=W)
        Entry(frame5, textvariable=self.stateVar, width=5).grid(row=1, column=4)
        Label(frame5, text="ZIP").grid(row=1, column=5, sticky=W)
        Entry(frame5, textvariable=self.zipVar, width=5).grid(row=1, column=6)

        frame6 = Frame(window)
        frame6.pack()
        Button(frame6, text="Add", command=self.processAdd).grid(row=1, column=1)
        Button(frame6, text="First", command=self.processFirst).grid(row=1, column=2)
        Button(frame6, text="Previous", command=self.processPrevious).grid(row=1, column=3)
        Button(frame6, text="Next", command=self.processNext).grid(row=1, column=4)
        Button(frame6, text="Last", command=self.processLast).grid(row=1, column=5)

        self.addressList = self.loadAddress()
        self.current = 0

        if len(self.addressList) > 0:
            self.setAddress()

        window.mainloop()

    # TODO replace save to dat file with update query to sqlite db file
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
        address = Address(self.firstnameVar.get(), self.lastnameVar.get(), self.numberVar.get(), self.streetVar.get(),
                          self.cityVar.get(), self.stateVar.get(), self.zipVar.get())
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
        self.current = len(self.addressList) - 1
        self.setAddress()

    def setAddress(self):
        self.firstnameVar.set(self.addressList[self.current].firstname)
        self.lastnameVar.set(self.addressList[self.current].lastname)
        self.numberVar.set(self.addressList[self.current].number)
        self.streetVar.set(self.addressList[self.current].street)
        self.cityVar.set(self.addressList[self.current].city)
        self.stateVar.set(self.addressList[self.current].state)
        self.zipVar.set(self.addressList[self.current].zip)

AddressBook()