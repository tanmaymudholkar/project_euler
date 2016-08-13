from __future__ import print_function, division

asciiValueOfAlphabet = {chr(asciiValue):asciiValue for asciiValue in range(ord('a'), 1+ord('z'))}
alphabetAtAscii = {asciiValue:chr(asciiValue) for asciiValue in range(ord('a'), 1+ord('z'))}

indexOfAlphabet = {alphabetAtAscii[asciiValue]:1+asciiValue-asciiValueOfAlphabet['a'] for asciiValue in range(ord('a'), 1+ord('z'))}
