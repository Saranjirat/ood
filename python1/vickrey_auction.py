def vickrey_auction():
    bids = input("Enter All Bid : ").split()
    
    if len(bids) < 2:
        print("not enough bidder")
        return
    
    bids = list(map(int, bids))
    sorted_bids = sorted(bids, reverse=True)
    
    if sorted_bids[0] == sorted_bids[1]:
        print("error : have more than one highest bid")
        return
    
    winner_bid = sorted_bids[0]
    second_highest_bid = sorted_bids[1]
    
    print(f"winner bid is {winner_bid} need to pay {second_highest_bid}")

vickrey_auction()

