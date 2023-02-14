class ContractCategory:
    def __init__(self, contract_category_id: str, contract_category_name: str) -> None:
        self._contract_category_id: str = contract_category_id
        self._contract_category_name: str = contract_category_name

    @property
    def contract_category_id(self) -> str:
        return self._contract_category_id
    
    @property
    def contract_category_name(self) -> str:
        return self._contract_category_name
    
if __name__ == "__main__":
    category = ContractCategory('1', 'NDA')
    