# vault_client/__init__.py
import os
import hvac
from .credentials import VaultCredentials

# Load Vault token from environment
VAULT_TOKEN = os.environ.get("VAULT_TOKEN")
if not VAULT_TOKEN:
    raise RuntimeError("VAULT_TOKEN environment variable is not set")

VAULT_TOKEN = VAULT_TOKEN.strip()  # remove any whitespace/newlines

# Vault server URL (can also be read from VaultCredentials if preferred)
VAULT_URL = "https://vault.metcarob.com"

# Initialize hvac client at package level
client = hvac.Client(
    url=VAULT_URL,
    token=VAULT_TOKEN,
    verify=False,  # skip TLS verification if needed
)







# import os
# import hvac
# from .credentials import VaultCredentials

# vault_token = os.environ.get("VAULT_TOKEN")
# if not vault_token:
#     raise RuntimeError("VAULT_TOKEN environment variable is not set")

# client = hvac.Client(
#     url=self.VAULT_URL,
#     token=vault_token,
#     verify=False
# )
