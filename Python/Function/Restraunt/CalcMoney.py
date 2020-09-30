""""
this program calculates the billes of my restraunt

"""
# Global variables
BIG_MAC_COST = 45
SMALL_MAC_COST = 35

def Total_Income_Sale(Big_mac,Small_mac,spend):
    print(Big_mac)
    print(Small_mac)
    print(spend)
    total = (Big_mac*BIG_MAC_COST+Small_mac*SMALL_MAC_COST+spend)
    return total


def Total_Bill(water,electricity,gas,rent=1000):
    total = (rent*0.9+water+electricity+gas)
    return total

def main():
    return  print("shalom")

print(__name__)

if __name__ == "__main__":
    print(Total_Income_Sale(40 ,10,10))
    revenue = Total_Income_Sale(100,50)-Total_Bill(200,400,150)
    print(revenue)
    main()
    print(BIG_MAC_COST)
