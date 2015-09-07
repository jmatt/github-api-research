import github3


def verify_user(username, password):
    try:
        g = github3.login(username, password)
        g.user()
        return True
    except GitHubError as ghe:
        if "401" in ghe.message:
            return False
        else:
            print(ghe.message)

        
def _str_to_key(keystr):
    key_sections = keystr.split(' ')
    for section in key_section:
        if section.startswith('AAAA'):
            return section


def verify_key(username, user_keystr):
    anon_user = github3.user(username)
    user_key = _str_to_key(user_keystr)
    for keystr in anon_user.iter_keys():
        key = _str_to_key(keystr)
        if key and key == user_key:
            return True
    return False
