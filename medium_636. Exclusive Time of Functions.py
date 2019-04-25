"""
For each log entry:

a) Calculate the time elapsed - Check elapsed time between the prev log entry and current log entry
b) Update the execution time of the current running function (use a stack to track the the current running function)
c) If currently running function has ended, pop the stack.
"""


class Solution(object):
    def parseData(self, log):
        fn, an, tm = log.split(':')
        return int(fn), an, int(tm)+1 if an == 'end' else int(tm)

    def exclusiveTime(self, n, logs):
        output, stack, prev_tm = [0 for i in range(n)], [0], 0

        for log in logs[1:]:
            curr_fn, curr_an, curr_tm = self.parseData(log)
            exec_tm, prev_tm = curr_tm - prev_tm, curr_tm
            if stack:
                exec_fn = stack[-1]
                stack.pop() if curr_an == 'end' else stack.append(curr_fn)
                output[exec_fn] += exec_tm
            else:
                stack.append(curr_fn)
        return output

print Solution().exclusiveTime(4, ["0:start:0","1:start:5","2:start:6","3:start:9","3:end:45","2:end:70","1:end:102","0:end:114"])
