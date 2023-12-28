# access_levels
# -1 - Anyone can access
#

al_separation = [
    {'endpoint': 'public_web.index_', 'access_levels': [-1]},
    {'endpoint': 'public', 'access_levels': [-1]},
    {'endpoint': 'user_login.sign_in', 'access_levels': [-1]},
    {'endpoint': 'user_login.sign_out', 'access_levels': [-1]}
]
