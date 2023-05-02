def play(nums):
    player_one_scores = 0
    player_two_scores = 0

    i = 0
    while i < len(nums) - 3:
        player_one_card = nums[i]
        player_two_card = nums[i + 1]
        scores_to_add = nums[i + 2]

        if player_one_card < player_two_card:
            player_one_scores += scores_to_add
        else:
            player_two_scores += scores_to_add
        i += 3

    return 'player_one' if player_one_scores > player_two_scores else 'player_two'


print(play([1, 2, 3, 9, 8, 5, 7, 4, 6, 12, 89, 45, 21, 34, 25, 24, 56, 34, 27, 67, 56, 48]))
