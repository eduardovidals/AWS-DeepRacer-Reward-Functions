def reward_function(params):
    """
    Example of waypoints reward function using an optimized racing line calculated from the K1999 algorithm.
    This reward function is focused on Oval_track.
    """

    # use arrays calculated from the optimized race line notebook
    centerleft = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 49, 50, 51, 52, 53, 54, 55, 56,
                  57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 100, 101, 102]

    centerright = [21, 22, 23, 24, 32, 33, 34, 35, 36, 47, 48, 72, 73, 74, 75, 76, 83, 84, 85, 86, 87, 97, 98, 99]

    right = [25, 26, 27, 28, 29, 30, 31, 77, 78, 79, 80, 81, 82]

    fast = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 48, 49, 50, 51, 52, 53, 54, 55, 56,
            57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 99, 100, 101]

    medium = [20, 21, 22, 23, 30, 31, 32, 33, 34, 35, 36, 43, 44, 45, 46, 47, 72, 73, 74, 81, 82, 83, 84, 85, 86, 87,
              94, 95, 96, 97, 98]

    slow = [24, 25, 26, 27, 28, 29, 37, 38, 39, 40, 41, 42, 75, 76, 77, 78, 79, 80, 88, 89, 90, 91, 92, 93]

    # initialize variables
    closest = params['closest_waypoints']
    nextwaypoint = max(closest[0], closest[1])
    all_wheels_on_track = params['all_wheels_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    reward = 0.001

    if all_wheels_on_track:
        if nextwaypoint in centerleft:
            if (distance_from_center / params['track_width']) <= 0.25 and (is_left_of_center):
                reward = 14
        elif (params['distance_from_center'] / params['track_width']) <= 0.25 and (not is_left_of_center):
            reward = 0
        else:
            reward = -7

    elif nextwaypoint in centerright:
        if (distance_from_center / track_width) <= 0.25 and (not is_left_of_center):
            reward = 14
        elif (distance_from_center / track_width) <= 0.25 and is_left_of_center:
            reward = 0
        else:
            reward = -7

    elif nextwaypoint in right:
        if (not is_left_of_center) and (distance_from_center / track_width) > 0.25 and (
                distance_from_center / track_width) < 0.48:
            reward = 14
        else:
            reward = -7

    if nextwaypoint in fast:
        if speed == 3:
            reward += 14
        else:
            reward -= (5 - speed) ** 2

    elif nextwaypoint in medium:
        if speed == 2:
            reward += 14
        else:
            reward -= 7

    elif nextwaypoint in slow:
        if speed == 1:
            reward += 14
        else:
            reward -= (2 + speed) ** 2

    else:
        reward = 0.001

    return float(reward)
