

class Solution(object):
    def addBoldTag(self, s, d):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        intervals = []

        for subs in d:
            sub_len = len(subs)
            for i, _ in enumerate(s):
                if s.startswith(subs, i):
                    intervals.append([i, i+sub_len-1])

        intervals = sorted(intervals, key = lambda x: (x[0], x[1]))

        stack = [intervals[0]] if intervals else []

        for start, end in intervals[1:]:
            prev_start, prev_end = stack[-1]
            if (start == prev_end + 1) or (start <= prev_end):
                stack.pop()
                stack.append([prev_start, max(prev_end, end)])
            else:
                stack.append([start, end])

        output, prev_idx = '', 0

        while stack:
            start_idx, end_idx = stack.pop(0)
            output += s[prev_idx: start_idx]
            output += '<b>' + s[start_idx:end_idx+1] + '</b>'
            prev_idx = end_idx+1
        else:
            output += s[prev_idx:]

        return output

print Solution().addBoldTag("qrzjsorbkmyzzzvoqxefvxkcwtpkhzbakuufbpgdkykmojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmweyyzzmgcoiupjnidphvzlnxtcogufozlenjfvokztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm",
    ["qr","zj","so","rb","km","yz","zz","vo","qx","ef","vx","kc","wt","pk"])
    # ['zz'])

<b>qrzjsorbkmyzzzvoqxefvxkcwtpk</b>hzbakuufbpgdky<b>km</b>ojwuennrjeciqvvacpzrrczfhxnsmginzwinzihpomxtmwey<b>yzz</b>mgcoiupjnidphvzlnxtcogufozlenjf<b>vo</b>kztghwckzyvmktduqkizixzxpanjwrdeudjyftxksjgdklwxrhmudhrtemuvelykqaafzlqmennttkighcdxfozdcoqkyshhajipnsdrljrnlwmyjuwxsebpqm
