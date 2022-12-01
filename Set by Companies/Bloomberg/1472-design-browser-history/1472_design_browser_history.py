class BrowserHistory:

    def __init__(self, homepage: str):
        """
        leetcode->google->fb->linkedin->you
                               ^
        I have an idea about using two stacks, one for 
        history that I will back into, another one for 
        history I will forward into. 
        Wait I think one array can do the job, its just the
        image of stack feels like a closer fit but
        actually only one array is sufficient
        The idea is to use what I drew above, a pointer and 
        an array to store the history.
        when we visit, the pointer will +1 waiting for the new
        url to be added. If the pointer is less than length of array
        Meaning we have some forward history that is not cleaned yet
        So pop them out then append the url.
        Whil back and forward, use min to find out the who will lead 
        either end of the array.
        """
        self.history = [homepage]
        self.curr = 0
        
    def visit(self, url: str) -> None:
        self.curr += 1
        while self.curr < len(self.history):
            self.history.pop()

        self.history.append(url)
        
    def back(self, steps: int) -> str:
        self.curr = max(0, self.curr - steps)
        return self.history[self.curr]
      
    def forward(self, steps: int) -> str:
        self.curr = min(len(self.history) - 1, self.curr + steps)
        return self.history[self.curr]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)