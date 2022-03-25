

def outerFun(fnc):

    def innerFun(amt):
        print("Logged into the server.......")
        fnc(amt)
        print("Logged out of the server........")
        print("-" * 40)

    return innerFun


@outerFun
def deposit(amt):
    print(f"Amount {amt} successfully credited into the accout.....")

@outerFun
def withdraw(amt):
    print(f"Amount {amt} successfully debited from the account......")

@outerFun
def transfer(amt):
    print(f"Amount {amt} trasnfered successfully.....")


deposit(50000)
withdraw(15000)
transfer(5000)


