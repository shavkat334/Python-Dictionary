def get_active_users(users: dict[str, dict]) -> list[str]:
    active_list = []
    for name, info in users.items():
        if info.get("active") == True:
            active_list.append(name)
    return active_list
 
data = {"Ali": {"active": True}, "Vali": {"active": False}}
print(get_active_users(data))