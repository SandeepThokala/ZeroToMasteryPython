import re

regex = r"[a-zA-Z@#$!0-9]{8,}"

test_str = "GIBbaadam12ZAMpa@1998"

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print (f"Match {matchNum} was found at {match.start()-match.end()}: {match.group()}")
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print (f"Group {groupNum} found at {match.start(groupNum) - match.end(groupNum)}: {match.group(groupNum)}")