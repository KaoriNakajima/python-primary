import uuid

from contract.contract import Contract
from contract.contract_info import ContractInfo
from contract.contract_status import ContractStatus


class CreateContract:

    @classmethod
    def create_contract(cls, name: str, language: int, title: str, contents: str) -> Contract:
        contract_info = ContractInfo(
            language=language,
            title=title,
            contents=contents
        )
        contract_id: str = str(uuid.uuid4())
        contract = Contract(
            contract_id=contract_id,
            contract_name=name,
            contract_info=contract_info,
            contract_status=ContractStatus.not_checked.value
        )
        return contract
