def recur(stack):
    def getandremove(stack):
        result = stack.pop()
        if len(stack) == 0:
            return result
        else:
            i = getandremove(stack)
            stack.append(result)
            return i

    if len(stack) == 0:
        return
    i = getandremove(stack)
    recur(stack)
    stack.append(i)
    return stack

print(recur([1,2,3,4]))






