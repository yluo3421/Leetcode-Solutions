 def getUnalottedUsers(bids, totalShares): 
    #Function getUnalottedUsers    
    #Sorts price(decending) and timestamp(ascending)    
    sorted_bids = sorted(sorted(bids, key = lambda x:x[3] , reverse=False), key = lambda x:x[2] , reverse=True)
    shares_received = dict() #Dictionary to store all ids that were allocated atleast 1 share    
    for i in range(len(sorted_bids)): #loop through sorted list       
        if totalShares>0: #Check if shares are still remaining          
            if sorted_bids[i][2]> sorted_bids[i+1][2]: #Checking if there is no tie in bidding amount             
                if totalShares< sorted_bids[i][1]: #If shares are less than requested                
                    shares_received[sorted_bids[i][0]] = "1"                
                    return [x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())]             
                totalShares-=sorted_bids[i][1] #if shares are more than requested             
                shares_received[sorted_bids[i][0]] = "1"           
            else: #If there is a tie in amount             
                sum_req = sorted_bids[i][1]             
                end = i             
                for j in range(i,len(sorted_bids)): #Check how many users have bid the same amount                
                    end=j                
                    if sorted_bids[j][2]== sorted_bids[j+1][2]:                   
                        sum_req+= sorted_bids[j+1][1]                   
                        continue                
                    else:                   
                        break             
                if totalShares < (end-i): #If total shares < number of users that bid same amount                
                    for x in range(i,len(sorted_bids)): #allocate according to timestamp                   
                        if totalShares>0:                      
                            shares_received[sorted_bids[x][0]] = "1"                      
                            totalShares-=1                   
                        else:                      
                            return [x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())]             
                elif totalShares>sum_req: #If totalshares> requested amount by all users                
                    for x in range(i, end+1):                   
                        shares_received[sorted_bids[x][0]] = "1"                
                    totalShares-=sum_req             
                else:                
                    for x in range(i, end+1): #if shares are > number of ties users but< requested amount                   
                        shares_received[sorted_bids[x][0]] = "1"                
                    return [x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())]       
        else:          
            return [x[0] for x in sorted_bids if x[0] not in list(shares_received.keys())] 

def main():    
    bids = [[1,5,5,0],[2,7,8,1],[3,7,5,1],[4,10,3,3]]    
    totalShares = 18    
    ret = getUnalottedUsers(bids, totalShares)    
    print(ret) 
main() 