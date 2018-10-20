# 公告数据
start_url = [['https://bbs.ppmoney.com/forum-120-%s.html' % i for i in range(1, 6)],
              ['https://bbs.ppmoney.com/forum-121-%s.html' % i for i in range(1, 15)],
              ['https://bbs.ppmoney.com/forum-117-%s.html' % i for i in range(1, 54)],
              ['https://bbs.ppmoney.com/forum-118-%s.html' % i for i in range(1, 37)],
              ['https://bbs.ppmoney.com/forum-115-%s.html' % i for i in range(1, 17)],
              ['https://bbs.ppmoney.com/forum-114-%s.html' % i for i in range(1, 39)],
              ['https://bbs.ppmoney.com/forum-105-%s.html' % i for i in range(1, 697)],
              ['https://bbs.ppmoney.com/forum-56-%s.html' % i for i in range(1, 1001)],
              ['https://bbs.ppmoney.com/forum-69-%s.html' % i for i in range(1, 1001)],
              ['https://bbs.ppmoney.com/forum-106-%s.html' % i for i in range(1, 233)],
              ['https://bbs.ppmoney.com/forum-116-%s.html' % i for i in range(1, 1001)],
              ['https://bbs.ppmoney.com/forum-107-%s.html' % i for i in range(1, 259)],
              ['https://bbs.ppmoney.com/forum-122-%s.html' % i for i in range(1, 7)],
              ['https://bbs.ppmoney.com/forum-124-%s.html' % i for i in range(1, 13)]]

start_list = []
for i in range(len(start_url)):
    for j in start_url[i]:
        start_list.append(j)
# print(len(start_list))