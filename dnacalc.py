#!/usr/bin/env python

# This is a comment

#DNASeq = raw_input( "Enter a DNA sequence " )
DNASeq = 'ATTTGGTTTACCTGTTTTTTTATTGCCC'
#DNASeq = 'ATTTGGTTCC'
# strings cannot be edited. instead give it the same name as the old name to edit it.
DNASeq = DNASeq.upper()

print( 'Sequence ' + DNASeq )

# this counts elements of the string DNASeq.
#We float it so we will have later on no problems if we're doing divisions etc.
SeqLength = float( len( DNASeq ) )

# to combine a string eg 'length is' with non-string things will break the code. Therefore I used str()

print ( 'Length is ' + str( SeqLength ) )

# .count means it will just count. in our case A

# creating variables based on properties of DNAseq. counts is a special type of fuction...
#blocking code that is already written. calc is a special kind of fuction.  a method, in this...
#case a string. Grap the count fuction. count also comes with an argument. in this case the charakter...
#we're looking for. count get 2 infos. 1) actual string 2) what we want count

TotalStrong = 0
TotalWeak = 0

Bases = "CGTA"

for Base in Bases:
	Count = DNASeq.count( Base)
	Frequency = Count / SeqLength
	print( '{}: {:.2f}'.format( Base, Frequency) )
	if Base in 'GC':
		TotalStrong = TotalStrong + Count
	else:
		TotalWeak = TotalWeak + Count
		
print( TotalStrong, TotalWeak)


# old school maths for melting temperature
if SeqLength <= 14:
	MeltTemp = ( 4 * TotalStrong ) + ( 2* TotalWeak )
	#print ( 'Melting Temp: {}'.format(MeltTemp) )
else:
	MeltTemp = 64.9 + 41 * (TotalStrong - 16.4) / SeqLength
	#print ( 'Long Melting Temp: {}'.format(MeltTemp) )
print ( 'Melting Temp: {}'.format(MeltTemp) )

print('Done')

