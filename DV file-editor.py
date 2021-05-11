import re
o = open("output.txt", "a", encoding="utf8")  # open for append
anchorNum = 1
pageLink = "    <a href=\"#\d+\">"
oldPageNum = "     [pg"
pageNum = 821
padding = "<a style=\"padding-top: 50vh\""
a = "    </a>"
span = ""
for line in open("input.txt", encoding="utf8"):
    if re.match(pageLink, line):
        line = ""
    if line.startswith(oldPageNum):
        line = ""
    if line.startswith(padding):
        line = "</td>\n<td>\n<img src = \"https://digitalcollections.lib.washington.edu/digital/api/singleitem/image/iraqdiaries/" + str(pageNum - 1) + "/default.jpg\">\n</td>\n</tr>\n<tr>\n<td><span class=\"pb\">\n<p id = \"" + str(anchorNum) + ";\" style=\"padding-top: 180px\"> </p> <p style=\"font-size: 25px; font-family: PT Serif; font-weight: bold\">Page " + str(anchorNum) + ":</p>\n"
        pageNum = pageNum + 1
        anchorNum = anchorNum + 1
    if re.match(a, line):
        line = ""
    o.write(line)
o.close()

o = open("output.txt", "a", encoding="utf8")  # open for append
x = 1
for line in open("input.txt", encoding="utf8"):
    if line.startswith("   <span class=\"pb\">"):
        line =  "<a style=\"padding-top: 50vh\" id = \"a" + str(x) + "\"></a>" + line
        x = x + 1
    o.write(line)
o.close()