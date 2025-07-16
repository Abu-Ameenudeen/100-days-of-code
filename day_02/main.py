from restaurant.tip_calculator import Tip_calculator


def main():
    your_split = Tip_calculator(bill_amt=100, tip=12)
    print(f"Amount you have to pay is: {your_split.split_amount(5)}")

    
if __name__ == "__main__":
    main()
    