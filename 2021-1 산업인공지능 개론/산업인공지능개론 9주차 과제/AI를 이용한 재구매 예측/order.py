from datetime import date

def get_recent_order_date(orderA, orderB):
    return orderA.order_date if orderA.more_recent_than(orderB) else orderB.order_date

class Order:
    def __init__(self,
                 member_no,
                 member_connection_count,
                 product_no,
                 order_product_price,
                 order_product_quantity,
                 order_date):
        tokens = order_date.split('-')
        
        self.member_no = member_no # 고객 번호
        self.member_connection_count = member_connection_count # 고객 접속수
        self.product_no = product_no # 상품 번호
        self.order_product_price = order_product_price # 상품 판매가
        self.order_product_quantity = order_product_quantity # 상품 구입수량
        self.order_date = date(int(tokens[0]), int(tokens[1]), int(tokens[2])) # 주문 일자
    
    def more_recent_than(self, order):
        return self.order_date > order.order_date

class OrderList:
    def __init__(self, sorted_by_date=False):
        self.orders = []
        self.members_no = set()
        self.products_no = set()
        self.sorted_by_date = sorted_by_date
    
    def add(self, order):
        self.orders.append(order)
        self.members_no.add(order.member_no)
        self.products_no.add(order.product_no)
    
    def count_orders(self):
        return len(self.orders)
    
    def count_products_variety(self):
        return len(self.products_no)
    
    def filter_member(self, member_no):
        order_list = OrderList()
        for order in self.orders:
            if (order.member_no == member_no):
                order_list.add(order)
        return order_list
    
    def filter_product(self, product_no):
        order_list = OrderList()
        for order in self.orders:
            if (order.product_no == product_no):
                order_list.add(order)
        return order_list
    
    def sort_by_date(self):
        if self.sorted_by_date:
            return self.orders
        else:
            orders = sorted(self.orders, key=lambda x: x.order_date)
        return orders
    
    def limit_to_date(self, last_date):
        limited_order_list = OrderList()
        orders = self.orders if self.sorted_by_date else self.sort_by_date()
        for order in orders:
            if order.order_date <= last_date:
                limited_order_list.add(order)
            else:
                return limited_order_list
            
        return limited_order_list