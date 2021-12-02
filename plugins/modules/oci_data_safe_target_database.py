#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_data_safe_target_database
short_description: Manage a TargetDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TargetDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), registers the specified database with Data Safe and creates a Data Safe target database in the Data Safe Console.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_target_database_actions) module: activate, change_compartment,
      deactivate, download_privilege_script."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which to create the Data Safe target database.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The display name of the target database in Data Safe. The name is modifiable and does not need to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - The description of the target database in Data Safe.
            - This parameter is updatable.
        type: str
    database_details:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            database_type:
                description:
                    - The database type.
                type: str
                choices:
                    - "INSTALLED_DATABASE"
                    - "AUTONOMOUS_DATABASE"
                    - "DATABASE_CLOUD_SERVICE"
                required: true
            infrastructure_type:
                description:
                    - The infrastructure type the database is running on.
                type: str
                choices:
                    - "ORACLE_CLOUD"
                    - "CLOUD_AT_CUSTOMER"
                    - "ON_PREMISES"
                    - "NON_ORACLE_CLOUD"
                required: true
            instance_id:
                description:
                    - The OCID of the compute instance on which the database is running.
                    - Applicable when database_type is 'INSTALLED_DATABASE'
                type: str
            ip_addresses:
                description:
                    - The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.
                    - Applicable when database_type is 'INSTALLED_DATABASE'
                type: list
                elements: str
            listener_port:
                description:
                    - The port number of the database listener.
                    - Applicable when database_type is 'INSTALLED_DATABASE'
                type: int
            service_name:
                description:
                    - The service name of the database registered as target database.
                    - Applicable when database_type is one of ['INSTALLED_DATABASE', 'DATABASE_CLOUD_SERVICE']
                type: str
            autonomous_database_id:
                description:
                    - The OCID of the autonomous database registered as a target database in Data Safe.
                    - Applicable when database_type is 'AUTONOMOUS_DATABASE'
                type: str
            vm_cluster_id:
                description:
                    - The OCID of the VM cluster in which the database is running.
                    - Applicable when database_type is 'DATABASE_CLOUD_SERVICE'
                type: str
            db_system_id:
                description:
                    - The OCID of the cloud database system registered as a target database in Data Safe.
                    - Applicable when database_type is 'DATABASE_CLOUD_SERVICE'
                type: str
    credentials:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            user_name:
                description:
                    - The database user name.
                type: str
                required: true
            password:
                description:
                    - The password of the database user.
                type: str
                required: true
    tls_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            status:
                description:
                    - Status to represent whether the database connection is TLS enabled or not.
                type: str
                choices:
                    - "ENABLED"
                    - "DISABLED"
                required: true
            certificate_store_type:
                description:
                    - The format of the certificate store.
                type: str
                choices:
                    - "JKS"
            store_password:
                description:
                    - The password to read the trust store and key store files, if they are password protected.
                type: str
            trust_store_content:
                description:
                    - Base64 encoded string of trust store file content.
                type: str
            key_store_content:
                description:
                    - Base64 encoded string of key store file content.
                type: str
    connection_option:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            connection_type:
                description:
                    - "The connection type used to connect to the database. Allowed values:
                      - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
                      - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe."
                type: str
                choices:
                    - "PRIVATE_ENDPOINT"
                    - "ONPREM_CONNECTOR"
                required: true
            datasafe_private_endpoint_id:
                description:
                    - The OCID of the Data Safe private endpoint.
                    - Applicable when connection_type is 'PRIVATE_ENDPOINT'
                type: str
            on_prem_connector_id:
                description:
                    - The OCID of the on-premises connector.
                    - Applicable when connection_type is 'ONPREM_CONNECTOR'
                type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    target_database_id:
        description:
            - The OCID of the Data Safe target database.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the TargetDatabase.
            - Use I(state=present) to create or update a TargetDatabase.
            - Use I(state=absent) to delete a TargetDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create target_database
  oci_data_safe_target_database:
    # required
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    database_details:
      # required
      database_type: CLOUD_DB_SYSTEM
      infrastructure_type: ORACLE_CLOUD

      # optional
      instance_id: ocid1.instance.oc1.iad.anuwcljsgn3s2facu6dvc6uzhykv3uj56l5zevbob7dli4pqntjbq5343f2bq
      ip_addresses: [ "null" ]
      listener_port: 56
      service_name: database.host.com

    # optional
    display_name: null
    description: null
    credentials:
      # required
      user_name: databaseAdminUser
      password: example-password
    tls_config:
      # required
      status: ENABLED

      # optional
      certificate_store_type: JKS
      store_password: example-password
      trust_store_content: trust_store_content_example
      key_store_content: key_store_content_example
    connection_option:
      # required
      connection_type: PRIVATE_ENDPOINT

      # optional
      datasafe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target_database
  oci_data_safe_target_database:
    # required
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: null
    description: null
    database_details:
      # required
      database_type: CLOUD_DB_SYSTEM
      infrastructure_type: ORACLE_CLOUD

      # optional
      instance_id: ocid1.instance.oc1.iad.anuwcljsgn3s2facu6dvc6uzhykv3uj56l5zevbob7dli4pqntjbq5343f2bq
      ip_addresses: [ "null" ]
      listener_port: 56
      service_name: database.host.com
    credentials:
      # required
      user_name: databaseAdminUser
      password: example-password
    tls_config:
      # required
      status: ENABLED

      # optional
      certificate_store_type: JKS
      store_password: example-password
      trust_store_content: trust_store_content_example
      key_store_content: key_store_content_example
    connection_option:
      # required
      connection_type: PRIVATE_ENDPOINT

      # optional
      datasafe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_target_database:
    # required
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: null

    # optional
    description: null
    database_details:
      # required
      database_type: CLOUD_DB_SYSTEM
      infrastructure_type: ORACLE_CLOUD

      # optional
      instance_id: ocid1.instance.oc1.iad.anuwcljsgn3s2facu6dvc6uzhykv3uj56l5zevbob7dli4pqntjbq5343f2bq
      ip_addresses: [ "null" ]
      listener_port: 56
      service_name: database.host.com
    credentials:
      # required
      user_name: databaseAdminUser
      password: example-password
    tls_config:
      # required
      status: ENABLED

      # optional
      certificate_store_type: JKS
      store_password: example-password
      trust_store_content: trust_store_content_example
      key_store_content: key_store_content_example
    connection_option:
      # required
      connection_type: PRIVATE_ENDPOINT

      # optional
      datasafe_private_endpoint_id: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete target_database
  oci_data_safe_target_database:
    # required
    target_database_id: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete target_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_target_database:
    # required
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: null
    state: absent

"""

RETURN = """
target_database:
    description:
        - Details of the TargetDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment which contains the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..aaaaaaaaqkb3jtub4lnlha7vfvp4f2mj6zxraqfnxernheayom3pljsfppca"
        id:
            description:
                - The OCID of the Data Safe target database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the target database in Data Safe.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The description of the target database in Data Safe.
            returned: on success
            type: str
            sample: description_example
        database_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_type:
                    description:
                        - The database type.
                    returned: on success
                    type: str
                    sample: DATABASE_CLOUD_SERVICE
                infrastructure_type:
                    description:
                        - The infrastructure type the database is running on.
                    returned: on success
                    type: str
                    sample: ORACLE_CLOUD
                autonomous_database_id:
                    description:
                        - The OCID of the autonomous database registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: ocid1.autonomousdatabase.oc1.iad.abuwcljs4hz5fnsyazyoblbm3o24ykw5iiwa44it2jzvhby73r6324522c2q
                vm_cluster_id:
                    description:
                        - The OCID of the VM cluster in which the database is running.
                    returned: on success
                    type: str
                    sample: ocid1.vmcluster.oc1.iad.abuwc33era5gex4puvmuphzxrfukxaxwqit7ze6egqquxe75ojb3lytlvtkq
                db_system_id:
                    description:
                        - The OCID of the cloud database system registered as a target database in Data Safe.
                    returned: on success
                    type: str
                    sample: ocid1.dbsystem.oc1.iad.abuwcljsgz57qgikkkpzenfya3uznj356vwjcgqrcy6x2dzcgierhbsonz7q
                service_name:
                    description:
                        - The database service name.
                    returned: on success
                    type: str
                    sample: service_name_example
                instance_id:
                    description:
                        - The OCID of the compute instance on which the database is running.
                    returned: on success
                    type: str
                    sample: ocid1.instance.oc1.iad.anuwcljsgn3s2facu6dvc6uzhykv3uj56l5zevbob7dli4pqntjbq5343f2bq
                ip_addresses:
                    description:
                        - The list of database host IP Addresses. Fully qualified domain names can be used if connectionType is 'ONPREM_CONNECTOR'.
                    returned: on success
                    type: list
                    sample: []
                listener_port:
                    description:
                        - The port number of the database listener.
                    returned: on success
                    type: int
                    sample: 56
        credentials:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                user_name:
                    description:
                        - The database user name.
                    returned: on success
                    type: str
                    sample: user_name_example
                password:
                    description:
                        - The password of the database user.
                    returned: on success
                    type: str
                    sample: example-password
        tls_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                status:
                    description:
                        - Status to represent whether the database connection is TLS enabled or not.
                    returned: on success
                    type: str
                    sample: ENABLED
                certificate_store_type:
                    description:
                        - The format of the certificate store.
                    returned: on success
                    type: str
                    sample: JKS
                store_password:
                    description:
                        - The password to read the trust store and key store files, if they are password protected.
                    returned: on success
                    type: str
                    sample: example-password
                trust_store_content:
                    description:
                        - Base64 encoded string of trust store file content.
                    returned: on success
                    type: str
                    sample: trust_store_content_example
                key_store_content:
                    description:
                        - Base64 encoded string of key store file content.
                    returned: on success
                    type: str
                    sample: key_store_content_example
        connection_option:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                connection_type:
                    description:
                        - "The connection type used to connect to the database. Allowed values:
                          - PRIVATE_ENDPOINT - Represents connection through private endpoint in Data Safe.
                          - ONPREM_CONNECTOR - Represents connection through on-premises connector in Data Safe."
                    returned: on success
                    type: str
                    sample: PRIVATE_ENDPOINT
                on_prem_connector_id:
                    description:
                        - The OCID of the on-premises connector.
                    returned: on success
                    type: str
                    sample: "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx"
                datasafe_private_endpoint_id:
                    description:
                        - The OCID of the Data Safe private endpoint.
                    returned: on success
                    type: str
                    sample: "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the target database in Data Safe.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time of target database registration and creation in Data Safe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time of the target database update in Data Safe.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaaqkb3jtub4lnlha7vfvp4f2mj6zxraqfnxernheayom3pljsfppca",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "database_details": {
            "database_type": "DATABASE_CLOUD_SERVICE",
            "infrastructure_type": "ORACLE_CLOUD",
            "autonomous_database_id": "ocid1.autonomousdatabase.oc1.iad.abuwcljs4hz5fnsyazyoblbm3o24ykw5iiwa44it2jzvhby73r6324522c2q",
            "vm_cluster_id": "ocid1.vmcluster.oc1.iad.abuwc33era5gex4puvmuphzxrfukxaxwqit7ze6egqquxe75ojb3lytlvtkq",
            "db_system_id": "ocid1.dbsystem.oc1.iad.abuwcljsgz57qgikkkpzenfya3uznj356vwjcgqrcy6x2dzcgierhbsonz7q",
            "service_name": "service_name_example",
            "instance_id": "ocid1.instance.oc1.iad.anuwcljsgn3s2facu6dvc6uzhykv3uj56l5zevbob7dli4pqntjbq5343f2bq",
            "ip_addresses": [],
            "listener_port": 56
        },
        "credentials": {
            "user_name": "user_name_example",
            "password": "example-password"
        },
        "tls_config": {
            "status": "ENABLED",
            "certificate_store_type": "JKS",
            "store_password": "example-password",
            "trust_store_content": "trust_store_content_example",
            "key_store_content": "key_store_content_example"
        },
        "connection_option": {
            "connection_type": "PRIVATE_ENDPOINT",
            "on_prem_connector_id": "ocid1.onpremconnector.oc1..xxxxxxEXAMPLExxxxxx",
            "datasafe_private_endpoint_id": "ocid1.datasafeprivateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import CreateTargetDatabaseDetails
    from oci.data_safe.models import UpdateTargetDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeTargetDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "target_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_database_id")

    def get_get_fn(self):
        return self.client.get_target_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_database,
            target_database_id=self.module.params.get("target_database_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["target_database_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_target_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateTargetDatabaseDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_target_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTargetDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_database_id=self.module.params.get("target_database_id"),
                update_target_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_target_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_database_id=self.module.params.get("target_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafeTargetDatabaseHelperCustom = get_custom_class(
    "DataSafeTargetDatabaseHelperCustom"
)


class ResourceHelper(
    DataSafeTargetDatabaseHelperCustom, DataSafeTargetDatabaseHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            database_details=dict(
                type="dict",
                options=dict(
                    database_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "INSTALLED_DATABASE",
                            "AUTONOMOUS_DATABASE",
                            "DATABASE_CLOUD_SERVICE",
                        ],
                    ),
                    infrastructure_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ORACLE_CLOUD",
                            "CLOUD_AT_CUSTOMER",
                            "ON_PREMISES",
                            "NON_ORACLE_CLOUD",
                        ],
                    ),
                    instance_id=dict(type="str"),
                    ip_addresses=dict(type="list", elements="str"),
                    listener_port=dict(type="int"),
                    service_name=dict(type="str"),
                    autonomous_database_id=dict(type="str"),
                    vm_cluster_id=dict(type="str"),
                    db_system_id=dict(type="str"),
                ),
            ),
            credentials=dict(
                type="dict",
                options=dict(
                    user_name=dict(type="str", required=True),
                    password=dict(type="str", required=True, no_log=True),
                ),
            ),
            tls_config=dict(
                type="dict",
                options=dict(
                    status=dict(
                        type="str", required=True, choices=["ENABLED", "DISABLED"]
                    ),
                    certificate_store_type=dict(type="str", choices=["JKS"]),
                    store_password=dict(type="str", no_log=True),
                    trust_store_content=dict(type="str"),
                    key_store_content=dict(type="str", no_log=True),
                ),
            ),
            connection_option=dict(
                type="dict",
                options=dict(
                    connection_type=dict(
                        type="str",
                        required=True,
                        choices=["PRIVATE_ENDPOINT", "ONPREM_CONNECTOR"],
                    ),
                    datasafe_private_endpoint_id=dict(type="str"),
                    on_prem_connector_id=dict(type="str"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            target_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_database",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
