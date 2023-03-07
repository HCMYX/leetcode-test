'''
58. 最后一个单词的长度
https://leetcode.cn/problems/length-of-last-word/
给你一个字符串 s，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中 最后一个 单词的长度。
单词 是指仅由字母组成、不包含任何空格字符的最大子字符串。

输入：s = "Hello World"    输出：5
解释：最后一个单词是“World”，长度为5。

输入：s = "   fly me   to   the moon  "    输出：4
解释：最后一个单词是“moon”，长度为4。

输入：s = "luffy is still joyboy"  输出：6
解释：最后一个单词是长度为6的“joyboy”。

1 <= s.length <= 104
s 仅有英文字母和空格 ' ' 组成
s 中至少存在一个单词
'''
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = 0
        i = 0
        for a in s:
            if a == " ":
                if i != 0:
                    r = i
                i = 0
            else:
                i += 1
        if i != 0:
            r=i

        return r;


def main():  # 主函数的代码
    s = Solution
    s.lengthOfLastWord(s,"   fly me   to   the moon  " )

if __name__ == "__main__":
    main()