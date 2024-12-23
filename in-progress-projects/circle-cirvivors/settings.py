# Constant settings
window_width = 1280
window_height = 720


##### Dynamic settings #####

# Enemy settings
enemy_speed = 5
enemy_size = 25
enemy_color = [255, 255, 255]

### Enemy spawn settings ###
# Spawn interval (milliseconds)
initial_spawn_interval = 1000
# How much faster to spawn
spawn_interval_decrement = 50
# How often decrease spawn interval
decrement_interval = 2000
# Don't change! vvv
current_spawn_interval = initial_spawn_interval
last_decrement_time = 0

# Projectile settings
projectile_speed = 2
projectile_size = 5
projectile_color = [255, 0, 0]

# Player settings
player_health = 100
player_size = 20
player_color = [140, 210, 205]
health_color = [0, 255, 0]

# Round settings
round_time = 30  # seconds
timer_color = [255, 255, 255]  # starts white

# Health bar stuff
healthbar_width = window_width
