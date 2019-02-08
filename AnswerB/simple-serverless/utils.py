from hashlib import md5


def create_md5_hash(s: str) -> str:
    return md5(s.encode()).hexdigest()


if __name__ == '__main__':
    assert create_md5_hash("test") == "098f6bcd4621d373cade4e832627b4f6"
