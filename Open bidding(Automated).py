#Open Bidding

print("Welcome to the Open bidding")
ch='y'
dic={}
while ch=='y':
    name=input("Enter your name ")
    amt=int(input("Enter your bid amount "))
    dic.update({name:amt})
    ch=input("Any more bidders? (y/n) ").lower()
    if ch!='y':
        print("\nTHE BID HAS ENDED")
keys=[]
for i in dic:
    keys.append(i)
high=keys[0]
for i in dic:
    if dic[i]>=dic[high]:
        high=i
print(f"\nTHE HIGHEST BIDDER IS {high} with a bid of ${dic[high]}")
    

