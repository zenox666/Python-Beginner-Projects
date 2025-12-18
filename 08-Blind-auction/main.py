import art
print(art.logo)

auction_continues=True
auction_record= {}
while auction_continues:
    name = input("what is your name: ")
    bid = int(input("what is your bid: $"))
    auction_record[name]=bid
    any_bids_left=input("Are there any other bidders? Type 'yes or 'no'.").lower()

    if any_bids_left=="no":

        auction_continues=False
        highest_bid=0
        highest_bidder=""
        for bidder in auction_record:
            bid_price=auction_record[bidder]
            if bid_price>highest_bid:
                highest_bid=bid_price
                highest_bidder += bidder
        print(f"The winner is {highest_bidder} with highest bid: ${highest_bid}")

    elif any_bids_left=="yes":
        auction_continues=True
        print("\n" *100)

# import art
# print(art.logo)
#
# def find_highest_bidder(bidding_record):
#     highest_bid = 0
#     winner = ""
#     for bidder in bidding_record:
#         bid_amount = bidding_record[bidder]
#         if bid_amount > highest_bid:
#             highest_bid = bid_amount
#             winner = bidder
#     print(f"The winner is {winner} with a bid of ${highest_bid}")
#
# auction_continues = True
# auction_record = {}
# while auction_continues:
#     name = input("what is your name: ")
#     bid = int(input("what is your bid: $"))
#     auction_record[name] = bid
#     any_bids_left = input("Are there any other bidders? Type 'yes or 'no'.").lower()
#
#     if any_bids_left == "no":
#         auction_continues = False
#         find_highest_bidder(auction_record)
#
#     elif any_bids_left == "yes":
#         auction_continues = True
#         print("\n" * 100)


# import art
# print(art.logo)
#
# auction_continues=True
# auction_record= {}
# while auction_continues:
#     name = input("what is your name:")
#     bid = int(input("what is your bid: $"))
#     auction_record[name]=bid
#     any_bids_left=input("Are there any other bidders? Type 'yes or 'no'.").lower()
#
#     if any_bids_left=="no":
#         auction_continues=False
#
#         highest_bid=max(auction_record.values())
#         highest_bidder=max(auction_record,key=auction_record.get)
#
#         print(f"The winner is {highest_bidder} with bid: ${highest_bid}")
#
#     elif any_bids_left=="yes":
#         auction_continues=True
#         print("\n" *100)
