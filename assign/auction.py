import os
bid_details={}
bid=True
max=0

while(bid):
   bidder_name=input("Who is bidding?\n")
   bid_amount=int(input("What is your amount?$"))
   bid_details[bidder_name]=bid_amount
   other=input("Are there any other bidders?Type yes or no\n")
   if(other=='no'):bid=False
   else:os.system('clear') 
        

for bid in bid_details:
   if(bid_details[bid]>max):
      max=bid_details[bid]
      key=bid
print(f"The maximum bid amount is {bid_details[key]} by {key}")