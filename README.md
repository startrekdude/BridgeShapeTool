# BridgeShapeTool
The shape of a bridge hand is the set of lengths of the suits in the hand, i.e., an unordered 4-tuple (w,x,y,z) where w+x+y+z=13, and each w, x, y, z describes the length of a suit in the hand. For this project, we wrote a program that calculates the probability distribution of the shape of a random hand. The program is for Python 3.8 or above and uses the matplotlib and tkinter libraries. The program calculates all the probabilities of all hand shapes, plots the distribution, and includes a function to calculate probability of incomplete bridge shapes (e.g., (6,4,X,X)). To run the program, simply open BridgeShapeTool.exe. The start-up/runtime is about 10 seconds.

 
Bridge Hand Probability Calculations:
To calculate the probability of a given shape the program does the following:
1. 	Calculates the number of “floating suits”, i.e., the number of suit lengths that are equal in the shape of a hand. For example, (4,3,3,3) has 3 floating suits and (5,4,3,1) has 0 floating suits. 
2.  Calculates the number of hands in a shape (w,x,y,z). Let a be the number of floating suits. Then
#h= (4 choose 1) * ((4-1) choose 1) * … * ((a+1) choose 1) * (13 choose w) * (13 choose x) * (13 choose y) * (13 choose z)
3.  Calculates the probability of a given hand shape:
P(w,x,y,z) = #h/(52 choose 13)

We also programmed a function that finds all the shapes associated with a given hand shape. If x1, … , xn (n=1,…,4) are the known numbers in the hand shape, then the code searches through all the hand shapes that have x1, … , xn in them, and outputs them. For example (6,4,X,X) outputs (6,4,2,1) and (6,4,3,0)


Icon image taken from https://www.hiclipart.com/free-transparent-background-png-clipart-icdim. We do not own the rights to the image, all credits go to the original creator who uploaded to hiclipart.com
