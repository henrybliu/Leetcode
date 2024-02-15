class Solution:
    '''
    Want to store the digit and letter logs and then sort the letter logs by
    its contents. Space could also be better saved by saving the index to the
    input logs rather than the log itself.

    Time: O(nlogn)
    Space: O(n)
    '''
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dLog = [] # store digit logs but maintain order that they appear in logs
        lLog = [] # store (log content, original log) to sort log content lexographically

        for log in logs:
            parsed = log.split(' ')
            # if digit log
            if parsed[1][0] in '0123456789':
                dLog.append(log)

            # if letter log
            else:
                lLog.append((parsed[1:], log))

        lLog.sort()

        res = []
        for l in lLog:
            res.append(l[1])
        for d in dLog:
            res.append(d)

        return res