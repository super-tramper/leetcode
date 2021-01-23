class Solution:
    def accountsMerge(self, accounts):
        ans = []
        n = len(accounts)
        email_dict = {}
        parents = list(range(n))
        # 若字典中不存在email，将email加入email_dict，否则将parent指向字典中email对应的值
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in email_dict:
                    email_dict[email] = i
                else:
                    parents[self.findParent(email_dict[email], parents)] = i
        # print(parents)
        for i in range(n):
            parent = self.findParent(i, parents)
            if parent != i:
                self.mergeAccount(parent, i, accounts)
        # print(accounts)
        for i in range(n):
            self.findParent(i, parents) == i and ans.append(accounts[i])
        for i, item in enumerate(ans):
            ans[i] = item[:1] + list(sorted(set(item[1:])))
        return ans

    def findParent(self, x, parents):
        while x != parents[x]:
            x = parents[x]
        return x

    def unionAccount(self, x, y, parents):
        parents[self.findParent(y, parents)] = self.findParent(x, parents)

    def mergeAccount(self, x, y, accounts):
        accounts[x] = accounts[x][:1] + list(accounts[x][1:] + accounts[y][1:])


if __name__ == '__main__':
    solution = Solution()
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    # accounts = [["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe1@m.co"],
    #             ["Kevin", "Kevin3@m.co", "Kevin5@m.co", "Kevin0@m.co"],
    #             ["Ethan", "Ethan5@m.co", "Ethan4@m.co", "Ethan0@m.co"],
    #             ["Hanzo", "Hanzo3@m.co", "Hanzo1@m.co", "Hanzo0@m.co"],
    #             ["Fern", "Fern5@m.co", "Fern1@m.co", "Fern0@m.co"]]
    # accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
    #             ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
    #             ["David", "David1@m.co", "David2@m.co"]]
    print(solution.accountsMerge(accounts))
    # sorted = [["Ethan", "Ethan0@m.co", "Ethan4@m.co", "Ethan5@m.co"],
    #           ["Gabe", "Gabe0@m.co", "Gabe1@m.co", "Gabe3@m.co"],
    #           ["Hanzo", "Hanzo0@m.co", "Hanzo1@m.co", "Hanzo3@m.co"],
    #           ["Kevin", "Kevin0@m.co", "Kevin3@m.co", "Kevin5@m.co"],
    #           ["Fern", "Fern0@m.co", "Fern1@m.co", "Fern5@m.co"]]
