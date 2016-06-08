#!/usr/bin/env python
import re
import sys

arguments = sys.argv
print arguments

InFileName = sys.argv[ 1 ]

#InFileName = 'Marrus_claudanielis.txt'

InFile = open( InFileName, 'r')

#Linenumber = 0

for Line in InFile:
	Line = Line.strip()
	print ( Line )

#	if Linenumber > 0:
#		print ( Line )
#		print ( Line )
#		#ElementList = Line.split( '\t' )
#		#print( ElementList )
#		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )
	
InFile.close()