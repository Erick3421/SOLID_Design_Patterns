from order import Order
from order_inventory_checker import OrderInventoryChecker 
from order_calculate_total import OrderCalculateTotal
from order_process_payment import OrderProcessPayment
from order_processor_service import OrderProcessorService

order_client = Order(1, 100.0)

inventory_checker = OrderInventoryChecker()
calculate_total = OrderCalculateTotal()
process_payment = OrderProcessPayment()

order_processor_service = OrderProcessorService(
    inventory_checker,
    calculate_total,
    process_payment
)
order_processor_service.process_order(order_client)
