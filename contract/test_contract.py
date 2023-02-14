import unittest

from contract import Contract
from contract_category import ContractCategory
from contract_status import ContractStatus

class TestContract(unittest.TestCase):

    def test_contract_正常作成を確認する(self):
        contract_category = ContractCategory("1", "NDA")
        contract = Contract("123", "名前", contract_category, ContractStatus.checking.value)

        self.assertEqual(contract.contract_id, "123")
        self.assertEqual(contract.contract_name, "名前")
        self.assertEqual(contract.contract_category.contract_category_id, "1")
        self.assertEqual(contract.contract_category.contract_category_name, "NDA")
        self.assertEqual(contract.contract_status, ContractStatus.checking.value)

    def test_contract_契約書名バリデーションエラーを確認する(self):
        with self.assertRaises(ValueError) as e:
            Contract("123", "名前"*1000, ContractCategory("1", "NDA"), ContractStatus.not_checked.value)

        self.assertEqual(e.exception.args[0], "契約書名は256文字以内に設定してください")

    def test_contract_契約書ステータスバリデーションエラーを確認する(self):
        with self.assertRaises(ValueError) as e:
            Contract("123", "名前", ContractCategory("1", "NDA"), 999)

        self.assertEqual(e.exception.args[0], "正しい契約ステータスを設定してください")

    def test_contract_契約書ステータス変更を確認する(self):
        contract = Contract("123", "名前", ContractCategory("1", "NDA"), ContractStatus.not_checked.value)
        contract.contract_status = ContractStatus.check_done.value

        self.assertEqual(contract.contract_status, ContractStatus.check_done.value)

if __name__ == "__main__":
    unittest.main()
