import unittest

from contract import Contract
from contract_info import ContractInfo
from contract_status import ContractStatus

class TestContract(unittest.TestCase):

    def test_contract_正常作成を確認する(self):
        contract_info = ContractInfo(1, '秘密保持契約', '契約書内容'*100)
        contract = Contract("123", "名前", contract_info, ContractStatus.checking.value)

        self.assertEqual(contract.contract_id, "123")
        self.assertEqual(contract.contract_name, "名前")
        self.assertEqual(contract.contract_info.language, 1)
        self.assertEqual(contract.contract_info.title, "秘密保持契約")
        self.assertEqual(contract.contract_status, ContractStatus.checking.value)

    def test_contract_契約書名バリデーションエラーを確認する(self):
        with self.assertRaises(ValueError) as e:
            Contract("123", "名前"*1000, ContractInfo(1, '秘密保持契約', '契約書内容'*100), ContractStatus.not_checked.value)

        self.assertEqual(e.exception.args[0], "契約書名は256文字以内に設定してください")

    def test_contract_契約書ステータスバリデーションエラーを確認する(self):
        with self.assertRaises(ValueError) as e:
            Contract("123", "名前", ContractInfo(1, '秘密保持契約', '契約書内容'*100), 999)

        self.assertEqual(e.exception.args[0], "正しい契約ステータスを設定してください")

    def test_contract_契約書ステータス変更を確認する(self):
        contract = Contract("123", "名前", ContractInfo(1, '秘密保持契約', '契約書内容'*100), ContractStatus.not_checked.value)
        contract.contract_status = ContractStatus.check_done.value

        self.assertEqual(contract.contract_status, ContractStatus.check_done.value)

if __name__ == "__main__":
    unittest.main()
