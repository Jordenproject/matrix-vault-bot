import os
import hvac

# Load token from environment
vault_token = os.environ.get("VAULT_TOKEN")
if not vault_token:
    raise RuntimeError("VAULT_TOKEN environment variable is not set")
vault_token = vault_token.strip()
print("TEST VAULT_TOKEN:", repr(vault_token))

# Initialize Vault client
client = hvac.Client(
    url="https://vault.metcarob.com",
    token=vault_token,
    verify=False
)

# Check authentication
if not client.is_authenticated():
    print("Token invalid or cannot connect")
else:
    print("Authenticated successfully")
    # Try reading secret
    secret = client.secrets.kv.v2.read_secret_version(
        path="memset/socialchat/dendrite/socialchat/bots/jordan",
        mount_point="kv"
    )
    data = secret["data"]["data"]
    print("Secret data keys:", list(data.keys()))
    if "matrixusername" in data:
        print("Username accessible:", data["matrixusername"])
    else:
        print("Token cannot access username")




# import os

# print("TEST VAULT_TOKEN:", repr(os.environ.get("VAULT_TOKEN")))


# import os
# import hvac


# client = hvac.Client(
#     url="https://vault.metcarob.com",
#     token=os.environ.get("VAULT_TOKEN")
# )

# if not client.is_authenticated():
#     print("Token invalid")
# else:
#     secret = client.secrets.kv.v2.read_secret_version(
#         path="memset/socialchat/dendrite/socialchat/bots/jordan",
#         mount_point="kv"
#     )
#     data = secret["data"]["data"]
#     if "matrixusername" in data:
#         print("Username accessible:", data["matrixusername"])
#     else:
#         print("Token cannot access username")







# # test_vault.py
# from vault_client import VaultCredentials
# creds = VaultCredentials()
# password = creds.get_password()     # call on instance
# username = creds.get_username()
# # password = VaultCredentials.get_password()
# print("Vault password retrieved:", password)
# print("Vault username retrieved:", username)