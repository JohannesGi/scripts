#!/usr/bin/env python

# This is a comment

DNASeq = 'ATGAACC'

print( 'Sequence ' + DNASeq )

SeqLength = float( len( DNASeq ) )

# to combine a string eg 'length is' with non-string things will break the code. Therefore I used str()

print ( 'Length is ' + str( SeqLength ) )

# .count means it will just count. in our case A

NumberA = DNASeq.count('A')
NumberT = DNASeq.count('T')
NumberG = DNASeq.count('G')
NumberC = DNASeq.count('C')

print('A: ' + str( NumberA / SeqLength ) )
print('T: ' + str( NumberT / SeqLength ) )
print('G: ' + str( NumberG / SeqLength ) )
print('C: ' + str( NumberC / SeqLength ) )