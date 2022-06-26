# -*- coding:utf-8 -*-
# @Time : 2022/6/23 21:19
# Auther : shenyuming
# @File : test_mode.py
# @Software : PyCharm
class Solution(object):
    def string_samle(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        rstr = " "
        if strs == []:
            return rstr

        old = strs[0]
        new = []
        for i in range(len(old)): #i为第一个元素的遍历单个字符
            for j in range(len(strs)):
                try:
                    if old[i] == strs[j][i]:
                        # print(strs[j][i])
                        new.append(strs[j][i])
                        new = list(set(new))
                    else:
                        return rstr
                except:
                    print('输入有误')
                    raise strs
            else:
              print(new)
        return rstr


    def max_same_strinf(self,str):
        if len(str) ==0:
            return " "
        max_str = max(str)
        min_str = min(str)
        for k,v in enumerate(min_str):
            if v != max_str[k]:
                return max_str[:k]
        return min_str

if __name__ == '__main__':
    a = ["flower","flow","flight"]
    b = ["dog","racecar","car"]
    print(Solution().max_same_strinf(a))
    print(Solution().max_same_strinf(b))