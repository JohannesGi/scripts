#!/usr/bin/env python
import re

InFileName = 'Marrus_claudanielis.txt'

InFile = open( InFileName, 'r')

Linenumber = 0

for Line in InFile:
	Line = Line.strip()

	if Linenumber > 0:
		#print ( Linenumber )
		#print ( Line )
		ElementList = Line.split( '\t' )
		#print( ElementList )
		print( 'Depth:{} Lat:{} Lon:{}'.format( ElementList[4], ElementList[2], ElementList[3] ) )

		SearchString = '(\d+) ([\d.])+ (\w)'
		Result = re.search(SearchString, ElementList[2] )
		print( Result )



	Linenumber = Linenumber + 1

InFile.close()