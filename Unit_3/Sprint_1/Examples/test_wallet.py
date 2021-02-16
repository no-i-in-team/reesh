import pytest
from lambdata.wallet import Wallet

@pytest.fixture
def empty_wallet():
    wallet = Wallet()
    return wallet


def test_default_initial_amount():
    wallet = Wallet()
    assert wallet.balance == 0

def test_setting_initial_amount():
    wallet = Wallet(100)
    assert wallet.balance == 100

def test_wallet_add_cash():
    wallet = Wallet(20)
    wallet.add_cash(100)
    assert wallet.balance == 120

def test_wallet_spend_cash():
    wallet = Wallet(20)
    wallet.spend_cash(10)
    assert wallet.balance == 10