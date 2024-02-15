'''
Name: FIXME
Date: FIXME
Program Description: Kattis problem bijele:
https://open.kattis.com/problems/bijele
Algorithm Steps:
    Input 6 numbers separated by a space
    Set varibles for # pieces there are supposed to be
    Write 6 line, one for each set of pieces, 
        taking the difference between actual pieces and pieces required
'''

king, queen, rooks, bishops, knights, pawns = input().split()

req_king = 1
req_queen = 1
req_rooks = 2
req_bishops = 2
# FIXMEs 3,4 make varibles for remaining pieces (2 knights, 8 pawns)

dif1 = req_king- king
dif2 = req_queen-queen
dif3 = req_bishops-bishops
dif4 = req_rooks-rooks

#FIXMEs 5,6: make dif5 and dif6 

#FIXME 7: make a function that prints the solution
