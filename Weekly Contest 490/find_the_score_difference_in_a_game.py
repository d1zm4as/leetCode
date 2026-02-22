# You are given an integer array nums, where nums[i] represents the points scored in the ith game.

# There are exactly two players. Initially, the first player is active and the second player is inactive.

# The following rules apply sequentially for each game i:

#     If nums[i] is odd, the active and inactive players swap roles.
#     In every 6th game (that is, game indices 5, 11, 17, ...), the active and inactive players swap roles.
#     The active player plays the ith game and gains nums[i] points.

# Return the score difference, defined as the first player's total score minus the second player's total score.©leetcode
def scoreDifference(nums):
    player1_score = 0
    player2_score = 0
    active_player = 1  # 1 for player1, 2 for player2

    for i in range(len(nums)):
        if nums[i] % 2 == 1:  # If the score is odd, swap players
            active_player = 3 - active_player
        
        if (i + 1) % 6 == 0:  # Every 6th game, swap players
            active_player = 3 - active_player
        
        if active_player == 1:
            player1_score += nums[i]
        else:
            player2_score += nums[i]

    return player1_score - player2_score