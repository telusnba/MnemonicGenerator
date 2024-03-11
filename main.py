from eth_account import Account
from mnemonic import Mnemonic


Account.enable_unaudited_hdwallet_features()

mnemo = Mnemonic("english")
seed_phrase = mnemo.generate(128)

print("Сид-фраза:", seed_phrase)


account = Account.from_mnemonic(mnemonic=seed_phrase, account_path=f"m/44'/60'/0'/0/0")


address = account.address
print("Адрес кошелька:", address, "\n\n\n")

print("Адреса кошельков:")
i = 0
for i in range(20):
    account = Account.from_mnemonic(mnemonic=seed_phrase, account_path=f"m/44'/60'/0'/0/{i}")
    address = account.address
    print(f"Кошелёк {i + 1}: {address}")
