"""
A seller recieve a 13% for everything he has sold
This code recieve the name and the total sold for the seller an shows how much he gain
"""


seller=input("Seller's name: ")
commision=0.13
total_sold=float(input("Total sold: "))

total_gain=round(total_sold+(total_sold*commision),2)
print(f"The seller {seller} have gained {total_gain}$ in this month")