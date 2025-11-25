print("Sinh viên: Nguyễn Bá Nhàn")
print("MSV: 245752021610141")
print("Bài 8 - Máy ATM đơn giản")
print("=" * 50)

class Bank:
    Account_type = "Savings"
    location = "Guntur"

    def __init__(self, name, acc_num, balance):
        self.name = name
        self.acc_num = acc_num
        self.balance = balance

    def __repr__(self):
        print("Welcome to the SBI ATM Machine")
        print("-" * 35)
        pin = int(input("Please enter your pin number: "))
        if pin != 123:
            return "Pin Incorrect. Please try again"

        while True:
            print(f"\nCard: XXXX XXXX XXXX {str(self.acc_num)[-4:]}")
            print("1. Balance   2. Withdraw   3. Deposit   4. Quit")
            ch = int(input("Chọn (1-4): "))
            if ch == 1:
                print(f"Số dư: {self.balance:,} VND")
            elif ch == 2:
                amt = float(input("Số tiền rút: "))
                if amt > self.balance:
                    print("Không đủ tiền!")
                else:
                    self.balance -= amt
                    print("Rút thành công! Số dư mới:", self.balance)
            elif ch == 3:
                amt = float(input("Số tiền gửi: "))
                self.balance += amt
                print("Gửi thành công! Số dư mới:", self.balance)
            elif ch == 4:
                print("Cảm ơn quý khách!")
                break
        return ""

name = input("Nhập tên chủ tài khoản: ")
acc = int(input("Nhập số tài khoản: "))
bal = float(input("Nhập số dư ban đầu: "))
print(Bank(name, acc, bal))
