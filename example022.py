#!usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""
题目：两个乒乓球队进行比赛，各出三人。甲队
为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，
c说他不和x,z比，请编程序找出三队赛手的名单。
程序分析：生成深度为3搜索树的搜索树，然后利用题设条件剪枝
"""
#原始程序
#还有优化空间
def main():
    for a in "xyz":
        for b in "xyz":
            #利用隐含条件a不能等于b，进行剪枝
            if a != b:
                for c in "xyz":
                    if c != a and c != b:
                        if a != "x" and c != "x" and c != "z":
                            print("a vs %s, b vs %s, c vs %s" %(a, b, c))

if __name__ == "__main__":
    main()
