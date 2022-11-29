class Solution:
#     def invalidTransactions(self, transactions: List[str]) -> List[str]:
#         """
#         go through transactions and find those with same name,
#         then find the one with 1000 +
#         """
#         cities = defaultdict(lambda: defaultdict(list))
#         ans = []
        
#         for item in transactions:
#             name, time, amount, city = item.split(",")
#             cities[city][name].append(time)
#         # print(cities)
#         # defaultdict(<function Solution.invalidTransactions.<locals>.<lambda> at             0x7f314a52c5e0>, {'mtv': defaultdict(<class 'list'>, {'alice': ['20']}),             'beijing': defaultdict(<class 'list'>, {'alice': ['50']})})
#         for item in transactions:
#             name, time, amount, city = item.split(",")
            
#             if int(amount) >= 1000:
#                 ans.append(item)
            
#             for key, value in cities.items():
#                 if key == city:
#                     continue
                    
                
#                 if any([abs(int(x) - int(time)) <= 60 for x in value[name]]):
#                     ans.append(item)
#                     break
                
                    
#         return ans  
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        cities = defaultdict(lambda: defaultdict(list))
        output = []
        
		#build city map. 
        for t in transactions:
            name, time, amount, city = t.split(',')
            cities[city][name].append(time)

		#Check each transaction against all transactions in a given city name from a given person
        for t in transactions:
            name, time, amount, city = t.split(',')
            
			#Case 1
            if int(amount) > 1000:
                output.append(t)
                continue
                
			#Case 2
            for k,v in cities.items():
                if k == city:
                    continue
                    
                if any([abs(int(x) - int(time)) <= 60 for x in v[name]]):
                    output.append(t)
                    break;
                
        
        return output
                        