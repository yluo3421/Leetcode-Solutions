end = 0
n = len(nums)
for start in range(n):
    # 如果窗口不满足条件，就右移end扩大窗口
    while end < n and (start和end的构成的窗口不满足条件):
        end += 1
    
    # 注意这里需要再次确认if中的条件，之前while循环结束可能是因为end越界
    if start和end的构成的窗口满足条件:
        用start和end更新结果