from order import Order
from order_inventory_checker import OrderInventoryChecker 
from order_calculate_total import OrderCalculateTotal
from order_process_payment import OrderProcessPayment

class OrderProcessorService:

    def __init__(self, inventory_checker, calculate_total, process_payment):
        self._order_inventory_checker = inventory_checker
        self._order_calculate_total = calculate_total
        self._order_process_payment = process_payment

    def process_order(self, order) -> None:
        self._order_inventory_checker.check(order)
        self._order_calculate_total.calculate(order)
        self._order_process_payment.process(order)