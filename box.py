import random

class temprange:
    def __init__(self, high, low, boxname):
        self.high = high
        self.low=low
        self.boxname = boxname
        self.nextval = None

class randomtemp:
    def __init__(self):
        self.randomval = random.randrange(1,10)


class LinkedList:
    def __init__(self):
        self.headval = None

    def insertcontainer(self, hightemp, lowtemp, box_name):
        NewBox = temprange(hightemp, lowtemp, box_name)
        if self.headval is None:
            self.headval = NewBox
            return
        BoxLoc = self.headval
        while BoxLoc.nextval:
            BoxLoc = BoxLoc.nextval
        BoxLoc.nextval = NewBox


    def checkbox(self):
        checkval = self.headval
        newrandomval = randomtemp()

        while checkval:
            print("Current temp:" ,newrandomval.randomval,  "Temperature Range:"  ,checkval.low,  "-"  ,checkval.high)
            if newrandomval.randomval < checkval.low:
                print("Message alert:", checkval.boxname,"Low Temperature")
            elif newrandomval.randomval > checkval.high:
                print("Message alert :", checkval.boxname, "High Temperature ")
            else:
                print("All ok")
            newrandomval = randomtemp()
            checkval = checkval.nextval

Box = LinkedList()
Box.insertcontainer(5,3, "Box1")
Box.insertcontainer(6,4,"Box2")
Box.insertcontainer(7,3, "Box3")
Box.insertcontainer(8,2, "Box4")
Box.insertcontainer(7,5, "Box5")


Box.checkbox()
