from brownie import Lottery
from scripts.helpful_scripts import get_account, get_contract


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy(get_contract())


def main():
    deploy_lottery()
