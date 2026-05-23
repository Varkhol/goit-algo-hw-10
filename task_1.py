import time

COINS = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(amount, coins=COINS):
    sorted_coins = sorted(coins, reverse=True)
    result = {}

    for coin in sorted_coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount %= coin
        if amount == 0:
            break
    return result


def find_min_coins(amount, coins=COINS):
    if amount == 0:
        return {}
    min_coins = [float("inf")] * (amount + 1)
    min_coins[0] = 0
    used_coin = [0] * (amount + 1)
    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                prev_coins = min_coins[current_amount - coin] + 1
                if prev_coins < min_coins[current_amount]:
                    min_coins[current_amount] = prev_coins
                    used_coin[current_amount] = coin
    result = {}
    while amount > 0:
        coin = used_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result

def main():
    test_amount = 113

    print(f"Сума для видачі: {test_amount}\n")
    print(f"Жадібний алгоритм: {find_coins_greedy(test_amount)}")
    print(f"Динамічне програмування:{find_min_coins(test_amount)}\n")

    print("Порівняння часу виконання:\n")
    print(f"{'Сума':>10} | {'Жадібний алгоритм, сек':>15} | {'Динамічне програмування, сек':>15}")
    print("-" * 66)

    for amount in [113, 1000, 10000, 100000]:
        start = time.perf_counter()
        find_coins_greedy(amount)
        greedy_time = time.perf_counter() - start

        start = time.perf_counter()
        find_min_coins(amount)
        dp_time = time.perf_counter() - start

        print(f"{amount:>10} | {greedy_time:>22.6f} | {dp_time:>22.6f}")


if __name__ == "__main__":
    main()