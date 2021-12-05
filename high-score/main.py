characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def switch_character(from_character, to_character):
    character_dist = abs(characters.index(from_character) - characters.index(to_character))
    return character_dist if character_dist <= 13 else 26 - character_dist


def find_closest_diff_position(current, target, current_position, prioritize_right):
    if current[current_position] != target[current_position]:
        return current_position, 0

    nr_steps = 0
    left_pos = current_position
    right_pos = current_position
    for i in range(len(target)):
        nr_steps += 1
        left_pos = left_pos - 1 if left_pos > 0 else len(target) - 1
        right_pos = right_pos + 1 if right_pos < len(target) - 1 else 0

        if prioritize_right and current[right_pos] != target[right_pos]:
            return right_pos, nr_steps
        if current[left_pos] != target[left_pos]:
            return left_pos, nr_steps
        if current[right_pos] != target[right_pos]:
            return right_pos, nr_steps
    return current_position, 0


def calc_solution(current, target, prioritize_right):
    nr_actions = 0
    position = 0
    while current != target:
        position, nr_steps = find_closest_diff_position(current, target, position, prioritize_right)
        nr_actions += nr_steps
        nr_actions += switch_character(current[position], target[position])
        current[position] = target[position]
    return nr_actions


if __name__ == '__main__':
    nr_tests = int(input())
    for i in range(nr_tests):
        target = [char for char in input()]
        current = [char for char in 'A'*len(target)]

        left_first_count = calc_solution(current.copy(), target.copy(), False)
        right_first_count = calc_solution(current.copy(), target.copy(), True)

        print(left_first_count if left_first_count < right_first_count else right_first_count)

