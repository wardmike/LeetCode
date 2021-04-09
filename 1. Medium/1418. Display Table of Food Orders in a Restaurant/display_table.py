# Prompt: https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/
# Runtime: 388 ms, faster than 79.25% of Python online submissions for Display Table of Food Orders in a Restaurant.
# Memory Usage: 22.9 MB, less than 33.96% of Python online submissions for Display Table of Food Orders in a Restaurant.


class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        
        tables = {} # maps table number to a map of orders to count of that order
        
        uniqueOrders = set()
        
        for order in orders:
            tableNum = int(order[1])
            item = order[2]
            
            if item not in uniqueOrders:
                uniqueOrders.add(item)
            
            if tableNum in tables:
                table = tables[tableNum]
                if item in table:
                    table[item] += 1
                else:
                    table[item] = 1
            else:
                tables[tableNum] = {}
                table = tables[tableNum]
                table[item] = 1
            
        # sort orders alphabetically
        sortedOrders = sorted(list(uniqueOrders))
        
        displayTable = [["Table"] + sortedOrders]
        
        for tableNum in sorted(tables):
            row = [str(tableNum)]
            tableOrders = tables[tableNum]
            for order in sortedOrders:
                if order in tableOrders:
                    row.append(str(tableOrders[order]))
                else:
                    row.append("0")
                    
            displayTable.append(row)
            
        return displayTable
