class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        result = []

        for i, a in enumerate(transactions):
            name1,time1,amount1,city1 = a.split(",")
            if int(amount1) > 1000:
                result.append(a)
                continue
                
            for j,b in enumerate(transactions):
                if i != j: 
                    name2, time2, amount2, city2 = b.split(",")
                    if (name1 == name2 and city1 != city2) and (abs(int(time1) - int(time2)) <= 60):
                        result.append(a)
                        break
                
        return result
    