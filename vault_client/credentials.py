import os
import hvac

class VaultCredentials:
    VAULT_URL = "https://vault.metcarob.com"
    SECRET_PATH = "memset/socialchat/dendrite/socialchat/bots/jordan"

    def __init__(self):
        vault_token = os.environ.get("VAULT_TOKEN")
        if not vault_token:
            raise RuntimeError("VAULT_TOKEN environment variable is not set")

        # Strip whitespace just in case
        vault_token = vault_token.strip()

        print("DEBUG: Vault token starts with:", vault_token[:10], "...")  # shows first 10 chars
        print("DEBUG: Reading Vault path:", self.SECRET_PATH)
        print("DEBUG: Using mount_point: kv")

        client = hvac.Client(
            url=self.VAULT_URL,
            token=vault_token,
            verify=False,  # needed if Vault uses self-signed cert
        )

        # Try reading the secret (like your working test)
        try:
            response = client.secrets.kv.v2.read_secret_version(
                path=self.SECRET_PATH,
                mount_point="kv",
                raise_on_deleted_version=True,
            )
        except hvac.exceptions.Forbidden as e:
            print("DEBUG: Forbidden error reading secret:", e)
            raise

        data = response["data"]["data"]
        self._username = data["matrixusername"]
        self._password = data["password"]

    def get_username(self) -> str:
        return self._username

    def get_password(self) -> str:
        return self._password


