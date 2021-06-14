def reward_function(params):
    # read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']
    progress = params['progress']
    steering_angle = params['steering_angle']
    reward = 0.001

    # encourage for all wheels to be on track
    if all_wheels_on_track:
        # initially encourage to stay in the center
        if steps < 40:
            reward = (1 - (distance_from_center / (track_width / 2)) ** 4) * speed ** 2
        # after 15 steps reward the car based on track completion and speed
        if steps >= 40:
            reward = ((progress * speed ** 2) / steps) * 2
    else:
        reward = 0.01

    # encourage to speed up in straightaways
    if all_wheels_on_track and abs(steering_angle) < 3 and speed == 2.5:
        reward += speed ** 2 / 4
    else:
        reward += 0.01

    return float(reward)