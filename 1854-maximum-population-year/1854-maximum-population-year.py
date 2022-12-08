class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        """
        1. For each log, update an array which stores 
        the population changes in each year. 
        2. The first index corresponds to the year 1950, 
        and the last to the year 2050.
        3. Then, iterate through the years while 
        updating the running sum, max population and 
        year of that max population.
        Return that year.
        """
        delta = [0] * 101

		# to make explicit the conversion from the year (1950 + i) to the ith index
        conversionDiff = 1950 
		
        for l in logs:
			# the log's first entry, birth, increases the population by 1
            delta[l[0] - conversionDiff] += 1 
			
			# the log's second entry, death, decreases the population by 1
            delta[l[1] - conversionDiff] -= 1
        
        runningSum = 0
        maxPop = 0
        year = 1950
		
		# find the year with the greatest population
        for i, d in enumerate(delta):
            runningSum += d
			
			# since we want the first year this population was reached, only update if strictly greater than the previous maximum population
            if runningSum > maxPop:
                maxPop = runningSum
                year = conversionDiff + i
				
        return year
        