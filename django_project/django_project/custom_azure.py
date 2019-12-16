from storages.backends.azure_storage import AzureStorage
import os


class AzureMediaStorage(AzureStorage):
    # Must be replaced by your <storage_account_name>
    account_name = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    location = 'media'
    file_overwrite = False
    # Must be replaced by your <storage_account_key>
    account_key = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY1")
    azure_container = 'media'
    expiration_secs = None


class AzureStaticStorage(AzureStorage):
    # Must be replaced by your storage_account_name
    account_name = os.environ.get("AZURE_STORAGE_ACCOUNT_NAME")
    # Must be replaced by your <storage_account_key>
    location = 'static'
    file_overwrite = False
    account_key = os.environ.get("AZURE_STORAGE_ACCOUNT_KEY1")
    azure_container = 'static'
    expiration_secs = None
