"""
A website domain like "discuss.leetcode.com" consists of various subdomains. At the top level,
 we have "com", at the next level, we have "leetcode.com", and at the lowest level, "discuss.
 leetcode.com". When we visit a domain like "discuss.leetcode.com", we will also visit the
 parent domains "leetcode.com" and "com" implicitly.Now, call a "count-paired domain" to be
 a count (representing the number of visits this domain received), followed by a space,
 followed by the address. An example of a count-paired domain might be "9001 discuss.leetcode.com".
 We are given a list cpdomains of count-paired domains. We would like a list of count-paired
 domains, (in the same format as the input, and in any order), that explicitly counts the
 number of visits to each subdomain.

 Example 1:
Input:
["9001 discuss.leetcode.com"]
Output:
["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]
Explanation:
We only have one website domain: "discuss.leetcode.com". As discussed above, the subdomain
"leetcode.com" and "com" will also be visited. So they will all be visited 9001 times.

Example 2:
Input:
["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output:
["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
Explanation:
We will visit "google.mail.com" 900 times, "yahoo.com" 50 times, "intel.mail.com" once and "wiki.org" 5
times. For the subdomains, we will visit "mail.com" 900 + 1 = 901 times, "com" 900 + 50 + 1 = 951 times,
and "org" 5 times.

Notes:

1.The length of cpdomains will not exceed 100.
2.The length of each domain name will not exceed 100.
3.Each address will have either 1 or 2 "." characters.
4.The input count in any count-paired domain will not exceed 10000.
5.The answer output can be returned in any order.
"""
# 本题利用了collections.Counter()的特殊作用

# 逆向思维很重要
# 整体思路
# 1.首先循环读取每一个字符串
# 2.对每一个字符串进行操作
# (1)先根据字符串特点使用split()函数将times和次数分开
# (2)在按照字典的形式,将域名作为“key”,times作为内容保存
# (3)通过识别"."对域名进行分割并按照字典形式保存
# (4)再利用字典的加法，对每一个分割后的域名的times进行统计
# 3.返回结果
import collections
class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c = collections.Counter()
        for cd in cpdomains:
            n, d = cd.split()
            c[d] += int(n)
            for i in range(len(d)):
                if d[i] == '.':
                    c[d[i + 1:]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]


A = Solution()
B = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
C = A.subdomainVisits(B)
print(C)