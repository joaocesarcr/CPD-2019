import struct
matchesToSearch = []
matchesToSearch.append(1773189583)
matchesToSearch.append(1798597502)
matchesToSearch.append(1798351256)
matchesToSearch.append(1799190427)
matchesToSearch.append(1799151530)
matchesToSearch.append(1798307715)
matchesToSearch.append(1798291968)
matchesToSearch.append(1795061493)
matchesToSearch.append(1794404902)


var = 0
strx = struct.pack('L',var)
with open('matchestosearch.bin', 'wb') as nOfMatchesFile:
    for match in matchesToSearch:
        bytesObj = struct.pack('L',match)
        nOfMatchesFile.write(bytesObj)

with open('matches.bin', 'wb') as fileb:
    fileb.write(strx)
    fileb.close()

with open('matchesnumber.bin', 'wb') as fileb:
    fileb.write(strx)
    fileb.close()

