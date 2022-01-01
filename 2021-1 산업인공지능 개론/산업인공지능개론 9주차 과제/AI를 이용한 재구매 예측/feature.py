from order import Order, OrderList
from numpy import np
from tqdm import tqdm

class Feature:
    def __init__(self,
                 average_price_product, # 특정 상품의 주문 평균가
                 product_order_count_member, # 특정 고객의 특정 상품 주문수
                 product_order_count_members, # 모든 고객의 특정 상품 주문수
                 product_variety_member, # 특정 고객이 주문한 모든 상품의 종류 수
                 connection_count_member, # 특정 고객의 접속 수
                 reorder_cycle_product_member, # 특정 고객의 특정 상품 평균 재주문 주기
                 reorder_cycle_products_member, # 특정 고객의 모든 상품 평균 재주문 주기
                 reorder_cycle_product_members): # 모든 고객의 특정 상품 평균 재주문 주기
        self.app = average_price_product
        self.pocm = product_order_count_member
        self.pocms = product_order_count_members
        self.pvm = product_variety_member
        self.ccm = connection_count_member
        self.rcpm = reorder_cycle_product_member
        self.rcpsm = reorder_cycle_products_member
        self.rcpms = reorder_cycle_product_members
    
    def as_list(self):
        return [self.app, self.pocm, self.pocms, self.pvm, self.ccm, self.rcpm, self.rcpsm, self.rcpms]

class FeatureFactory:
    def __init__(self, order_list):
        self.order_list = order_list
    
    def __create_feature_app(self, orderA, orderB): # 특정 상품의 주문 평균가 반환 A <-> B
        return (int(orderA.order_product_price) + int(orderB.order_product_price)) / 2
    
    def __create_feature_pocm(self, order_list, member_no, product_no): # 특정 고객의 특정 상품 주문수 ~B
        filtered_orders = order_list.filter_member(member_no).filter_product(product_no)
        return filtered_orders.count_orders()
    
    def __create_feature_pocms(self, order_list, product_no): # 모든 고객의 특정 상품 주문수 ~B
        filtered_orders = order_list.filter_product(product_no)
        return filtered_orders.count_orders()
    
    def __create_feature_pvm(self, order_list, member_no): # 특정 고객이 주문한 모든 상품의 종류 수 반환 ~B
        filtered_orders = order_list.filter_member(member_no)
        return filtered_orders.count_products_variety()
    
    def __create_feature_ccm(self, order): # 특정 고객의 접속 수 B
        return int(order.member_connection_count)
    
    def __create_feature_rcpm(self, order_list, member_no, product_no): # 특정 고객의 특정 상품 평균 재주문 주기 ~B
        filtered_orders = order_list.filter_member(member_no).filter_product(product_no)
        sorted_orders = filtered_orders.sort_by_date()
        
        cycles = []
        for i in range(len(sorted_orders) - 1):
            cycles.append((sorted_orders[i + 1].order_date - sorted_orders[i].order_date).days)
        
        return np.mean(cycles)
    
    def __create_feature_rcpsm(self, order_list, member_no): # 특정 고객의 모든 상품 평균 재주문 주기 ~B
        filtered_orders = order_list.filter_member(member_no)
        
        cycles = []
        for product_no in filtered_orders.products_no:
            sorted_orders = filtered_orders.filter_product(product_no).sort_by_date()
            for i in range(len(sorted_orders) - 1):
                cycles.append((sorted_orders[i + 1].order_date - sorted_orders[i].order_date).days)
            
        return np.mean(cycles)
    
    def __create_feature_rcpms(self, orders, product_no): # 모든 고객의 특정 상품 평균 재주문 주기 ~B
        filtered_orders = orders.filter_product(product_no)
        
        cycles = []
        for member_no in filtered_orders.members_no:
            sorted_orders = filtered_orders.filter_member(member_no).sort_by_date()
            for i in range(len(sorted_orders) - 1):
                cycles.append((sorted_orders[i + 1].order_date - sorted_orders[i].order_date).days)
            
        return np.mean(cycles)
    
    def __create_feature(self, orderA, orderB):
        if orderA.member_no != orderB.member_no:
            raise Exception('비교 대상들의 고객은 서로 같아야 합니다.')
        elif orderA.product_no != orderB.product_no:
            raise Exception('비교 대상들의 상품은 서로 같아야 합니다.')
            
        target_member_no = orderB.member_no
        target_product_no = orderB.product_no
        pre_order = orderA if orderB.more_recent_than(orderA) else orderB
        later_order = orderB if orderB.more_recent_than(orderA) else orderA
        limited_orders = self.order_list.limit_to_date(get_recent_order_date(orderA, orderB))
        
        app = self.__create_feature_app(orderA, orderB)
        pocm = self.__create_feature_pocm(limited_orders, target_member_no, target_product_no)
        pocms = self.__create_feature_pocms(limited_orders, target_product_no)
        pvm = self.__create_feature_pvm(limited_orders, target_member_no)
        ccm = self.__create_feature_ccm(later_order)
        rcpm = self.__create_feature_rcpm(limited_orders, target_member_no, target_product_no)
        rcpsm = self.__create_feature_rcpsm(limited_orders, target_member_no)
        rcpms = self.__create_feature_rcpms(limited_orders, target_product_no)
        feature = Feature(app, pocm, pocms, pvm, ccm, rcpm, rcpsm, rcpms)
        
        reorder_cycle = (later_order.order_date - pre_order.order_date).days
        return feature, reorder_cycle
    
    def create_features(self, limit=None):
        features = []
        cycles = []
        for member_no in (list(self.order_list.members_no)):
            member_filtered_order_list = self.order_list.filter_member(member_no)
            for product_no in member_filtered_order_list.products_no:
                filtered_order_list = member_filtered_order_list.filter_product(product_no)
                if len(filtered_order_list.orders) <= 2:
                    continue
                
                sorted_orders = filtered_order_list.sort_by_date()
                for i in range(len(sorted_orders) - 1):
                    feature, cycle = self.__create_feature(sorted_orders[i], sorted_orders[i + 1])
                    features.append(feature)
                    cycles.append(cycle)
                    if limit:
                        if len(features) >= limit:
                            return features, cycles
        return features, cycles