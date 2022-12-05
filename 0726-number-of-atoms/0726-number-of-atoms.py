class Solution:
    def countOfAtoms(self, formula: str) -> str:
        """
        Ahhhh, I wasn't good at chemistry in high school
        I think stack is a good tool to use to solve this
        chemistry problem.
        We will go through each char in the formula
        if its (, we can insert another counter to store
        whatever formula inside
        then at ), we will pop out the last Counter
        and multiply by the number comes behind the )
        Add the element and multiplicity
        to the original Counter in stack
        
        If there is no (, then we should first
        find the the element, then find out its
        multiplicity. Add the element and multiplicity
        to the original Counter in stack
        
        At the end, we combine all element and multiplicity
        in the original Counter and return
        """
        n = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < n:
            if formula[i] == "(":
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ")":
                top = stack.pop()
                i += 1
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start:i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                start = i
                i += 1
                while i < n and formula[i].islower():
                    i += 1
                name = formula[start:i]
                start = i
                while i < n and formula[i].isdigit():
                    i += 1
                multiplicity = int(formula[start: i] or 1)
                stack[-1][name] += multiplicity
        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else "") for name in sorted(stack[-1]))
                 