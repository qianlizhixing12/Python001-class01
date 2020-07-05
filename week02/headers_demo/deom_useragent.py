from fake_useragent import UserAgent

ua = UserAgent(verify_ssl=False)
print(f"chrome: {ua.chrome}")
print(f"ie: {ua.ie}")
print(f"random: {ua.random}")