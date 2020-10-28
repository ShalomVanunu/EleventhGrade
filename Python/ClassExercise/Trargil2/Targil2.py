

"""
this program exclude the URLs
"""

with open('Text.txt', 'r') as reader :
    content = reader.readlines() # content is List of lines . end nb \n

links = []

for line in content:
    if "http" in line:
        links.append(line[line.find('https'):-1])
print(links)
