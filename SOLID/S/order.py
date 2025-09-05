class Order:
    def __init__(self, order_id: int, total: float):
        self._order_id = order_id
        self._total = total

    def getId(self) -> int:
        return self._order_id
    
    def getTotal(self) -> float:
        return self._total