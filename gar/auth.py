import github3


def verify_user(username, password):
    try:
        g = github3.login(username, password)
        if g:
            g.user()
        else:
            return False
        return True
    except github3.GitHubError as ghe:
        if "401" not in ghe.message:
            print(ghe.message)
    return False


def _str_to_key(keystr):
    key_sections = keystr.split(' ')
    for section in key_sections:
        if section.startswith('AAAA'):
            return section


def verify_key(username, user_keystr):
    anon_user = github3.user(username)
    user_key = _str_to_key(user_keystr)
    for key in anon_user.iter_keys():
        key = _str_to_key(key.key)
        if key and key == user_key:
            return True
    return False


def verify_repo(username, password, reponame):
    try:
        g = github3.login(username, password)
        if g:
            owner, repo = reponame.split('/')
            repo = g.repository(owner, repo)
            if repo.permissions['push']:
                return True
        return False
    except github3.GitHubError as ghe:
        if "401" in ghe.message:
            return False
        else:
            print(ghe.message)
            return False
