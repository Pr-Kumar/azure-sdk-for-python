# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.dataprotection import DataProtectionMgmtClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-dataprotection
# USAGE
    python get_job.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = DataProtectionMgmtClient(
        credential=DefaultAzureCredential(),
        subscription_id="62b829ee-7936-40c9-a1c9-47a93f9f3965",
    )

    response = client.jobs.get(
        resource_group_name="BugBash1",
        vault_name="BugBashVaultForCCYv11",
        job_id="3c60cb49-63e8-4b21-b9bd-26277b3fdfae",
    )
    print(response)


# x-ms-original-file: specification/dataprotection/resource-manager/Microsoft.DataProtection/stable/2023-01-01/examples/JobCRUD/GetJob.json
if __name__ == "__main__":
    main()
