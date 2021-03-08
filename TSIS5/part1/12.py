colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('abc.txt', "w") as newfile:
        for color in colors:
                newfile.write("%s\n" % color)

content = open('abc.txt')
print(content.read())