"""
1359. Count All Valid Pickup and Delivery Options

Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.


Example 1:
Input: n = 1
Output: 1
Explanation: Unique order (P1, D1), Delivery 1 always is after of Pickup 1.

Example 2:
Input: n = 2
Output: 6
Explanation: All possible orders:
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.

Example 3:
Input: n = 3
Output: 90
"""
MOD = 10 ** 9 + 7


def countOrders(n: int) -> int:
    result = 1
    # Only one combination available when we only have one item to pick up and deliver
    if n == 1:
        return result

    """
    If it is more than 1 item to pick up & deliver
    Pick up - Pick can be done in any order, hence its n! ways of pick up items.
    Delivery - Delivery is slightly different, can only be done once the item is picked up
    E.g. with N = 3
    (_, _, _, _, _, _) there are six order of P and D can be placed, start with item P1
    (P1, _, _, _, _, _) then only D1 can happen and can be in any places which is 2N - 1 = 5 optional cases as N = 3
    lets assume to put D2  right after P1 to make problem a lot simpler
    Now, lets have a look at the P2 item
    (P1, D1, P2, _, _, _), then P2 can be in any left places which is 2N - 3 = 3 optional cases for delivery as N = 3
    (P1, D1, P2, D2, P3, _), then with P3, can also be in any left places which is 2N - 5 = 1
    But this combination is only if the order of P1, P2 ,P3 but there are n! ways of we set for pick up
    hence multiply by n!
    """

    # So we need to check order from first item to the N's item
    for i in range(1, n + 1):
        # each time, we do n! and delivery option which is 2*i - 1
        result *= i * (2 * i - 1)
        # In case number is too big, as requested, apply modulo
        result %= MOD

    return result


# print(countOrders(1))
# print(countOrders(2))
print(countOrders(3))
