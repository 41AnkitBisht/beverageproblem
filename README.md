# beverageproblem
For this problem i have used object oriented approach.
1. Creating a temprange class which initialize with High Temperature and Low Temperature(Temp range) <br>
2. Now i have connected the object of this class like nodes in linked list. <br>
3. The insertcontainer function can be used to add new containers. <br>
4. The checkbox function can be used to check temp of box.
5. If the program need to be executed every 2 min the time library in python can be used. <br>
6. For current value of temperature i have used random function in python.

The forward approach on this problem can be 
1. Create a class on beveragename and then use the beverage name to identify the temperature range required. <br>
2. Suppose "beer 1" need  temp range 4-7 then using a dict we can store the key value pair as dict = { "beer 1": [4,5] } <br>
3. Next time the we need a container for "beer 1 " we do not need to set the temperature range.
4. Further lets say that "beer 1" : temp range(3,8) and "beer 2": temp range(4,7) so we can store "beer 1" and "beer 2" in the same container{Temp range(4,7)}.Since [3< 4 < 7 < 8]
