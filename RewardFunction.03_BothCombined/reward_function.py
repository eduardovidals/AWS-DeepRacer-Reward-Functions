def reward_function(params):
    """
    Example of combining the previous two reward functions with speed.
    """

    # read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    progress = params['progress']
    steering_angle = params['steering_angle']
    is_offtrack = params['is_offtrack']
    reward = 0.001

    # encourage for all wheels to be on track
    if all_wheels_on_track:
        # center encouragement and speed
        if steps < 10:
            reward = (1 - (distance_from_center / (track_width / 2)) ** 4) * speed ** 2
        # reward for progress and speed
        if steps >= 10:
            reward = ((progress * speed ** 2) / steps) * 2
    else:
        reward = 0.001

    # encourage to speed up in straightaways
    if all_wheels_on_track and abs(steering_angle) < 10 and speed == 3:
        reward += (speed ** 2 / 4) + (progress / steps) ** 2
    else:
        reward += 0.001

    return float(reward)
