import sys
# number = int(sys.stdin.readline().strip())
# for line in sys.stdin:
#     line = line.strip()
#     if "Did Li Hua go to university" in line:
#         sys.stdout('Yes')
#     else:
#         sys.stdout('No')

line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
x1, y1, len1 = line1.split(' ')
x2, y2, len2 = line2.split(' ')
x1, y1, len1, x2, y2, len2 = int(x1), int(y1), int(len1), int(x2), int(y2), int(len2)

dot1 = []
dot2 = []

for i in range(len1):
    for j in range(len1):
        dot1.append((x1-len1 + 1 + i, x1-len1 + 1 + j))

for i in range(len2):
    for j in range(len2):
        dot2.append((x2-len2 + 1 + i, x2-len2 + 1 + j))

print("%.2f" % float(len(set(dot1) & set(dot2))))