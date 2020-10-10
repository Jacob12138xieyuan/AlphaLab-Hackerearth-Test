class Node:
    def __init__(self, action):
        self.string = action[5]+'@'+action[4]+'#'+action[1]
        self.action = action[0]
        self.orderID = action[1]
        self.side = action[2]
        self.symbol = action[3]
        self.price = int(action[4])
        self.quantity = int(action[5])
        self.next = None
        self.prev = None

    def update_string(self):
        self.string = str(self.quantity) + '@' + \
            str(self.price) + '#' + self.orderID


class LinkedList:
    def __init__(self, side):
        self.head = None
        self.tail = self.head
        self.side = side
        self.orders = {}

    def print_(self):
        p = self.head
        print(self.side + ': [', end="")
        while p:
            if not p.next:
                print('\''+p.string+'\'', end="")
                break
            print('\''+p.string+'\'', end=", ")
            p = p.next
        print(']')

    def insert(self, node):
        if not self.head:  # head not exist
            self.head = node  # set node as head
            self.tail = self.head  # set node as tail

        else:  # head exists
            if self.side == 'B':
                if node.price > self.head.price:  # append at left
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                elif node.price <= self.tail.price:  # append at right
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:  # head>node>tail, in between, move node to left
                    p = self.tail
                    while node.price > p.price:
                        p = p.prev
                    # insert node after p
                    node.next = p.next
                    p.next = node
                    node.prev = p
                    node.next.prev = node
            elif self.side == 'S':
                if node.price < self.head.price:  # append at left
                    self.head.prev = node
                    node.next = self.head
                    self.head = node
                elif node.price >= self.tail.price:  # append at right
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:  # head<node<tail, in between, move node to left
                    p = self.tail
                    while node.price < p.price:
                        p = p.prev
                    # insert node after p
                    node.next = p.next
                    p.next = node
                    node.prev = p
                    node.next.prev = node
        orderID = node.string.split('#')[1]
        self.orders[orderID] = node  # add order to orders, key is orderID

    def remove_head(self):
        if not self.head.next:  # only one node
            self.head = None
            self.tail = self.head
            return
        self.head = self.head.next

    def remove_tail(self):
        if not self.tail.prev:  # only one node
            self.head = None
            self.tail = self.head
            return
        self.tail = self.tail.prev

    def remove_node(self, orderID):
        if not self.head:
            return
        if self.head.orderID == orderID:  # need to remove head
            del self.orders[orderID]  # delete order from orders
            self.remove_head()
            return
        if self.tail.orderID == orderID:  # need to remove head
            del self.orders[orderID]  # delete order from orders
            self.remove_tail()
            return
        # node in between, find node using self.orders
        node = self.orders[orderID]
        node.next.prev = node.prev
        node.prev.next = node.next
        del self.orders[orderID]  # delete order from orders


B = LinkedList('B')  # higher price on left
S = LinkedList('S')  # lower price on left

while True:
    action = input()
    if action == 'END':
        break
    action = action.split(' ')
    if action[0] == 'SUB':  # submit order

        if action[2] == 'B':  # submit buy order
            buy_p, buy_q = int(action[4]), int(action[5])
            if S.head and S.head.price <= buy_p:  # has match
                if S.head.quantity == buy_q:  # all just matched
                    S.remove_head()
                elif S.head.quantity < buy_q:  # no enough sell order
                    while buy_q != 0 and S.head and S.head.price <= buy_p:  # find all matchs
                        if S.head.quantity == buy_q:  # all just matched
                            S.remove_head()
                        elif S.head.quantity < buy_q:  # no enough sell order, remove head untill all buy matched
                            buy_q -= S.head.quantity
                            S.remove_head()
                        else:  # sell_q > buy_q, don't remove head, just deduct
                            S.head.quantity -= buy_q
                            S.head.update_string()
                            buy_q = 0
                    if buy_q != 0:  # remain buy quantity cannot match, add buy order
                        buy_node = Node(action)
                        buy_node.quantity = buy_q
                        buy_node.update_string()
                        B.insert(buy_node)
                else:  # sell_q > buy_q, deduct buy_q
                    S.head.quantity -= buy_q
                    S.head.update_string()
            else:  # no match, add sell order
                buy_node = Node(action)
                B.insert(buy_node)

        else:  # sell order
            sell_p, sell_q = int(action[4]), int(action[5])
            if B.head and B.head.price >= sell_p:  # has match
                # print(B.head.quantity, sell_q)
                if B.head.quantity == sell_q:  # all just matched
                    B.remove_head()
                elif B.head.quantity < sell_q:  # no enough buy order
                    while sell_q != 0 and B.head and B.head.price >= sell_p:  # find all match
                        if B.head.quantity == sell_q:  # all just matched
                            B.remove_head()
                        elif B.head.quantity < sell_q:  # no enough buy order, remove head untill all sell matched
                            sell_q -= B.head.quantity
                            B.remove_head()
                        else:  # buy_q > sell_q, don't remove head, just deduct
                            B.head.quantity -= sell_q
                            B.head.update_string()
                            sell_q = 0
                    if sell_q != 0:  # remain sell quantity cannot, add sell order
                        sell_node = Node(action)
                        sell_node.quantity = sell_q
                        sell_node.update_string()
                        S.insert(sell_node)
                else:  # buy_q > sell_q, deduct sell_q
                    B.head.quantity -= sell_q
                    B.head.update_string()
            else:  # no match, add sell order
                sell_node = Node(action)
                S.insert(sell_node)

    else:  # cancel order
        orderID = action[1]
        if orderID in B.orders:
            B.remove_node(orderID)  # no this orderID in B
        else:
            S.remove_node(orderID)  # it is in S

    B.print_()
    S.print_()
