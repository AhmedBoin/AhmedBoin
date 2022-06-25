from brownie import Contract, accounts, config, FundMe, network


def deploy_fund_me():
    account = get_account()
    # fund_me = FundMe.deploy({"from": account}, publish_source=True)
    fund_me = Contract("0x56Df97aA550C3D93a7BE955fEc4044591749f451")
    print(f"Contract deployed to {fund_me.address}")


def get_account():
    if network.show_active == "development":
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me, type(fund_me))
    # fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print(fund_me)
    # fund_me.withdraw({"from": account})


def main():
    # deploy_fund_me()
    fund()
    withdraw()
