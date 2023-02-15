class ContractInfo:
    def __init__(self, language: int, title: str, contents: str) -> None:
        self._language: str = language
        self._title: str = title
        self._contents: str = contents

    @property
    def language(self) -> int:
        return self._language
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def contents(self) -> str:
        return self._contents
    
if __name__ == "__main__":
    info = ContractInfo(1, '秘密保持契約', '契約書内容'*100)
    