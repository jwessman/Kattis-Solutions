def flip_card(card):
    card_as_string = str(card)
    flipped_card = ''
    for digit_index in reversed(range(0, len(card_as_string))):
        digit = card_as_string[digit_index]
        if digit == '1':
            flipped_card += '1'
        elif digit == '2':
            flipped_card += '2'
        elif digit == '5':
            flipped_card += '5'
        elif digit == '6':
            flipped_card += '9'
        elif digit == '8':
            flipped_card += '8'
        elif digit == '9':
            flipped_card += '6'
        elif digit == '0':
            flipped_card += '0'
        else:
            return None
    # Removes
    return int(flipped_card)


def is_subset_sum(cards, n, desired_sum, nr_chosen_cards):
    if desired_sum == 0:
        return True

    if n == 0:
        return False
    if desired_sum < 0:
        return False
    if nr_chosen_cards == 2:
        return False

    flipped_card = flip_card(cards[n - 1])

    if flipped_card is not None and flipped_card > desired_sum and cards[n - 1] > desired_sum:
        return is_subset_sum(cards, n - 1, desired_sum, nr_chosen_cards)
    elif cards[n - 1] > desired_sum:
        return is_subset_sum(cards, n - 1, desired_sum, nr_chosen_cards)

    if flipped_card is not None:
        return is_subset_sum(cards, n - 1, desired_sum, nr_chosen_cards) or \
               is_subset_sum(cards, n - 1, desired_sum - cards[n - 1], nr_chosen_cards + 1) or \
               is_subset_sum(cards, n - 1, desired_sum - flipped_card, nr_chosen_cards + 1)
    else:
        return is_subset_sum(cards, n - 1, desired_sum, nr_chosen_cards) or \
               is_subset_sum(cards, n - 1, desired_sum - cards[n - 1], nr_chosen_cards + 1)


if __name__ == '__main__':
    nr_cards, desired_sum = input().split()
    cards = list(map(int, input().split()))

    if is_subset_sum(cards, int(nr_cards), int(desired_sum), 0):
        print("YES")
    else:
        print("NO")
