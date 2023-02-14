from contract_status import ContractStatus
from contract_category import ContractCategory


class Contract:
    def __init__(
        self, 
        contract_id: str,
        contract_name: str,
        contract_category: ContractCategory,
        contract_status: int) -> None:

        if len(contract_name) > 256:
            raise ValueError('契約書名は256文字以内に設定してください')
        
        if contract_status not in [status.value for status in ContractStatus]:
            raise ValueError('正しい契約ステータスを設定してください')

        self._contract_id = contract_id
        self._contract_name = contract_name
        self._contract_category = contract_category
        self._contract_status = contract_status

    @property
    def contract_id(self) -> str:
        return self._contract_id

    @property
    def contract_name(self) -> str:
        return self._contract_name


    @property
    def contract_category(self) -> ContractCategory:
        return self._contract_category


    @property
    def contract_status(self) -> int:
        return self._contract_status
    
    @contract_status.setter
    def contract_status(self, value: int) -> None:
        self._contract_status = value

if __name__ == "__main__":
    category = ContractCategory('1', 'NDA')
    test_contract = Contract("123", "秘密保持契約", category, ContractStatus.not_checked.value)
    test_contract.contract_status = ContractStatus.check_done.value
    