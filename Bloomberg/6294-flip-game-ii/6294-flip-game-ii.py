class Solution:
    def canWin(self, currentState: str) -> bool:
        if not currentState or len(currentState) < 2:
            return False
        
        for i in range(len(currentState) - 1):
            if currentState[i] == currentState[i+1] == "+":
                nextState = currentState[:i] + "--" + currentState[i+2:]
                if not self.canWin(nextState):
                    return True
        return False
