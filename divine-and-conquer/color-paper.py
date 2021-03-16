"""
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1

"""
import sys

sys.setrecursionlimit(10**8)
n = int(input())

papers = []
paper_dict = dict()
paper_dict[-1] = 0
paper_dict[0] = 0
paper_dict[1] = 0

for _ in range(n):
    papers.append(list(map(int, input().split())))

def all_same(papers):
    
    paper_length = len(papers)

    first_paper = papers[0][0]

    for row in range(paper_length):
        for col in range(paper_length):
            if first_paper != papers[row][col]:
                return False
    return True

def paper_check(papers):

    paper_length = len(papers)

    if paper_length == 1:
        paper_dict[papers[0][0]] += 1
        return
    
    first_paper = papers[0][0]

    if all_same(papers):

        paper_dict[first_paper] += 1

    else:

        new_paper_length = int(paper_length/3)

        for row in range(3):
            new_paper_draft = papers[row*new_paper_length:(row+1) * new_paper_length]
            for col in range(3):
                new_paper = []
                for i in new_paper_draft:
                    new_paper.append(i[col*new_paper_length:(col+1) * new_paper_length])
                print(new_paper)
                paper_check(new_paper)


paper_check(papers)
for i in paper_dict.keys():
    print(paper_dict[i])