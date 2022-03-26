class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        output = [[1]]
        cur_row = 1
        while cur_row < numRows:
            prevRow,newRow = output[-1],[1]
            i = 1
            while i < len(prevRow):
                newRow.append(prevRow[i-1]+prevRow[i])
                i+=1
            newRow.append(1)
            output.append(newRow)
            cur_row+=1

        return(output)
        