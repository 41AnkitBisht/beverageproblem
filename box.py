import random

class temprange:
    def __init__(self, high, low):
        self.high = high
        self.low=low
        self.nextval = None

class randomtemp:
    def __init__(self):
        self.randomval = random.randrange(1,10)


class LinkedList:
    def __init__(self):
        self.headval = None

    def insertcontainer(self, hightemp, lowtemp):
        NewBox = temprange(hightemp, lowtemp)
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
                print("Message alert: warninglow")
            elif newrandomval.randomval > checkval.high:
                print("Message alert :warninghigh")
            else:
                print("All ok")
            newrandomval = randomtemp()
            checkval = checkval.nextval

Box = LinkedList()
Box.insertcontainer(5,3)
Box.insertcontainer(6,4)
Box.insertcontainer(7,3)
Box.insertcontainer(8,2)


Box.checkbox()
