# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "storage-actions task update",
    is_preview=True,
)
class Update(AAZCommand):
    """Update a storage task resource with the specified parameters. If a storage task is already created and a subsequent update request is issued with different properties, the storage task properties will be updated. If a storage task is already created and a subsequent update request is issued with the exact same set of properties, the request will succeed.

    :example: storage-actions task update
        az storage-actions task update -g rgteststorageactions -n testtask1 --identity "{type:SystemAssigned}" --tags "{key2:value2}" --action "{if:{condition:'[[equals(BlobType,'/BlockBlob'/)]]',operations:[{name:'SetBlobTags',parameters:{Archive-Status:'Archived'},onSuccess:'continue',onFailure:'break'}]},else:{operations:[{name:'UndeleteBlob',onSuccess:'continue',onFailure:'break'}]}}" --description StorageTask1Update --enabled true
    """

    _aaz_info = {
        "version": "2023-01-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storageactions/storagetasks/{}", "2023-01-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    AZ_SUPPORT_GENERIC_UPDATE = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, self._output)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.storage_task_name = AAZStrArg(
            options=["-n", "--name", "--storage-task-name"],
            help="The name of the storage task within the specified resource group. Storage task names must be between 3 and 18 characters in length and use numbers and lower-case letters only.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-z0-9]{3,18}$",
                max_length=18,
                min_length=3,
            ),
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.identity = AAZObjectArg(
            options=["--identity"],
            arg_group="Parameters",
            help="The managed service identity of the resource.",
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Parameters",
            help="Resource tags.",
            nullable=True,
        )

        identity = cls._args_schema.identity
        identity.type = AAZStrArg(
            options=["type"],
            help="Type of managed service identity (where both SystemAssigned and UserAssigned types are allowed).",
            enum={"None": "None", "SystemAssigned": "SystemAssigned", "SystemAssigned,UserAssigned": "SystemAssigned,UserAssigned", "UserAssigned": "UserAssigned"},
        )
        identity.user_assigned_identities = AAZDictArg(
            options=["user-assigned-identities"],
            help="The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.",
            nullable=True,
        )

        user_assigned_identities = cls._args_schema.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectArg(
            nullable=True,
            blank={},
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg(
            nullable=True,
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.action = AAZObjectArg(
            options=["--action"],
            arg_group="Properties",
            help="The storage task action that is executed",
        )
        _args_schema.description = AAZStrArg(
            options=["--description"],
            arg_group="Properties",
            help="Text that describes the purpose of the storage task",
        )
        _args_schema.enabled = AAZBoolArg(
            options=["--enabled"],
            arg_group="Properties",
            help="Storage Task is enabled when set to true and disabled when set to false",
        )

        action = cls._args_schema.action
        action.else_ = AAZObjectArg(
            options=["else"],
            help="The else block of storage task operation",
            nullable=True,
        )
        action.if_ = AAZObjectArg(
            options=["if"],
            help="The if block of storage task operation",
        )

        else_ = cls._args_schema.action.else_
        else_.operations = AAZListArg(
            options=["operations"],
            help="List of operations to execute in the else block",
        )

        operations = cls._args_schema.action.else_.operations
        operations.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_storage_task_operation_update(operations.Element)

        if_ = cls._args_schema.action.if_
        if_.condition = AAZStrArg(
            options=["condition"],
            help="Condition predicate to evaluate each object. See https://aka.ms/storagetaskconditions for valid properties and operators.",
        )
        if_.operations = AAZListArg(
            options=["operations"],
            help="List of operations to execute when the condition predicate satisfies.",
        )

        operations = cls._args_schema.action.if_.operations
        operations.Element = AAZObjectArg(
            nullable=True,
        )
        cls._build_args_storage_task_operation_update(operations.Element)
        return cls._args_schema

    _args_storage_task_operation_update = None

    @classmethod
    def _build_args_storage_task_operation_update(cls, _schema):
        if cls._args_storage_task_operation_update is not None:
            _schema.name = cls._args_storage_task_operation_update.name
            _schema.on_failure = cls._args_storage_task_operation_update.on_failure
            _schema.on_success = cls._args_storage_task_operation_update.on_success
            _schema.parameters = cls._args_storage_task_operation_update.parameters
            return

        cls._args_storage_task_operation_update = AAZObjectArg(
            nullable=True,
        )

        storage_task_operation_update = cls._args_storage_task_operation_update
        storage_task_operation_update.name = AAZStrArg(
            options=["name"],
            help="The operation to be performed on the object.",
            enum={"DeleteBlob": "DeleteBlob", "SetBlobExpiry": "SetBlobExpiry", "SetBlobImmutabilityPolicy": "SetBlobImmutabilityPolicy", "SetBlobLegalHold": "SetBlobLegalHold", "SetBlobTags": "SetBlobTags", "SetBlobTier": "SetBlobTier", "UndeleteBlob": "UndeleteBlob"},
        )
        storage_task_operation_update.on_failure = AAZStrArg(
            options=["on-failure"],
            help="Action to be taken when the operation fails for a object.",
            nullable=True,
            enum={"break": "break"},
        )
        storage_task_operation_update.on_success = AAZStrArg(
            options=["on-success"],
            help="Action to be taken when the operation is successful for a object.",
            nullable=True,
            enum={"continue": "continue"},
        )
        storage_task_operation_update.parameters = AAZDictArg(
            options=["parameters"],
            help="Key-value parameters for the operation.",
            nullable=True,
        )

        parameters = cls._args_storage_task_operation_update.parameters
        parameters.Element = AAZStrArg(
            nullable=True,
        )

        _schema.name = cls._args_storage_task_operation_update.name
        _schema.on_failure = cls._args_storage_task_operation_update.on_failure
        _schema.on_success = cls._args_storage_task_operation_update.on_success
        _schema.parameters = cls._args_storage_task_operation_update.parameters

    def _execute_operations(self):
        self.pre_operations()
        self.StorageTasksGet(ctx=self.ctx)()
        self.pre_instance_update(self.ctx.vars.instance)
        self.InstanceUpdateByJson(ctx=self.ctx)()
        self.InstanceUpdateByGeneric(ctx=self.ctx)()
        self.post_instance_update(self.ctx.vars.instance)
        yield self.StorageTasksCreate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    @register_callback
    def pre_instance_update(self, instance):
        pass

    @register_callback
    def post_instance_update(self, instance):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class StorageTasksGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageActions/storageTasks/{storageTaskName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageTaskName", self.ctx.args.storage_task_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()
            _UpdateHelper._build_schema_storage_task_read(cls._schema_on_200)

            return cls._schema_on_200

    class StorageTasksCreate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 201]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200_201,
                    self.on_error,
                    lro_options={"final-state-via": "location"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageActions/storageTasks/{storageTaskName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageTaskName", self.ctx.args.storage_task_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2023-01-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=self.ctx.vars.instance,
            )

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()
            _UpdateHelper._build_schema_storage_task_read(cls._schema_on_200_201)

            return cls._schema_on_200_201

    class InstanceUpdateByJson(AAZJsonInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance(self.ctx.vars.instance)

        def _update_instance(self, instance):
            _instance_value, _builder = self.new_content_builder(
                self.ctx.args,
                value=instance,
                typ=AAZObjectType
            )
            _builder.set_prop("identity", AAZObjectType, ".identity", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True, "client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            identity = _builder.get(".identity")
            if identity is not None:
                identity.set_prop("type", AAZStrType, ".type", typ_kwargs={"flags": {"required": True}})
                identity.set_prop("userAssignedIdentities", AAZDictType, ".user_assigned_identities")

            user_assigned_identities = _builder.get(".identity.userAssignedIdentities")
            if user_assigned_identities is not None:
                user_assigned_identities.set_elements(AAZObjectType, ".", typ_kwargs={"nullable": True})

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("action", AAZObjectType, ".action", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("description", AAZStrType, ".description", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("enabled", AAZBoolType, ".enabled", typ_kwargs={"flags": {"required": True}})

            action = _builder.get(".properties.action")
            if action is not None:
                action.set_prop("else", AAZObjectType, ".else_")
                action.set_prop("if", AAZObjectType, ".if_", typ_kwargs={"flags": {"required": True}})

            else_ = _builder.get(".properties.action.else")
            if else_ is not None:
                else_.set_prop("operations", AAZListType, ".operations", typ_kwargs={"flags": {"required": True}})

            operations = _builder.get(".properties.action.else.operations")
            if operations is not None:
                _UpdateHelper._build_schema_storage_task_operation_update(operations.set_elements(AAZObjectType, "."))

            if_ = _builder.get(".properties.action.if")
            if if_ is not None:
                if_.set_prop("condition", AAZStrType, ".condition", typ_kwargs={"flags": {"required": True}})
                if_.set_prop("operations", AAZListType, ".operations", typ_kwargs={"flags": {"required": True}})

            operations = _builder.get(".properties.action.if.operations")
            if operations is not None:
                _UpdateHelper._build_schema_storage_task_operation_update(operations.set_elements(AAZObjectType, "."))

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return _instance_value

    class InstanceUpdateByGeneric(AAZGenericInstanceUpdateOperation):

        def __call__(self, *args, **kwargs):
            self._update_instance_by_generic(
                self.ctx.vars.instance,
                self.ctx.generic_update_args
            )


class _UpdateHelper:
    """Helper class for Update"""

    @classmethod
    def _build_schema_storage_task_operation_update(cls, _builder):
        if _builder is None:
            return
        _builder.set_prop("name", AAZStrType, ".name", typ_kwargs={"flags": {"required": True}})
        _builder.set_prop("onFailure", AAZStrType, ".on_failure")
        _builder.set_prop("onSuccess", AAZStrType, ".on_success")
        _builder.set_prop("parameters", AAZDictType, ".parameters")

        parameters = _builder.get(".parameters")
        if parameters is not None:
            parameters.set_elements(AAZStrType, ".")

    _schema_storage_task_operation_read = None

    @classmethod
    def _build_schema_storage_task_operation_read(cls, _schema):
        if cls._schema_storage_task_operation_read is not None:
            _schema.name = cls._schema_storage_task_operation_read.name
            _schema.on_failure = cls._schema_storage_task_operation_read.on_failure
            _schema.on_success = cls._schema_storage_task_operation_read.on_success
            _schema.parameters = cls._schema_storage_task_operation_read.parameters
            return

        cls._schema_storage_task_operation_read = _schema_storage_task_operation_read = AAZObjectType()

        storage_task_operation_read = _schema_storage_task_operation_read
        storage_task_operation_read.name = AAZStrType(
            flags={"required": True},
        )
        storage_task_operation_read.on_failure = AAZStrType(
            serialized_name="onFailure",
        )
        storage_task_operation_read.on_success = AAZStrType(
            serialized_name="onSuccess",
        )
        storage_task_operation_read.parameters = AAZDictType()

        parameters = _schema_storage_task_operation_read.parameters
        parameters.Element = AAZStrType()

        _schema.name = cls._schema_storage_task_operation_read.name
        _schema.on_failure = cls._schema_storage_task_operation_read.on_failure
        _schema.on_success = cls._schema_storage_task_operation_read.on_success
        _schema.parameters = cls._schema_storage_task_operation_read.parameters

    _schema_storage_task_read = None

    @classmethod
    def _build_schema_storage_task_read(cls, _schema):
        if cls._schema_storage_task_read is not None:
            _schema.id = cls._schema_storage_task_read.id
            _schema.identity = cls._schema_storage_task_read.identity
            _schema.location = cls._schema_storage_task_read.location
            _schema.name = cls._schema_storage_task_read.name
            _schema.properties = cls._schema_storage_task_read.properties
            _schema.system_data = cls._schema_storage_task_read.system_data
            _schema.tags = cls._schema_storage_task_read.tags
            _schema.type = cls._schema_storage_task_read.type
            return

        cls._schema_storage_task_read = _schema_storage_task_read = AAZObjectType()

        storage_task_read = _schema_storage_task_read
        storage_task_read.id = AAZStrType(
            flags={"read_only": True},
        )
        storage_task_read.identity = AAZObjectType(
            flags={"required": True},
        )
        storage_task_read.location = AAZStrType(
            flags={"required": True},
        )
        storage_task_read.name = AAZStrType(
            flags={"read_only": True},
        )
        storage_task_read.properties = AAZObjectType(
            flags={"required": True, "client_flatten": True},
        )
        storage_task_read.system_data = AAZObjectType(
            serialized_name="systemData",
            flags={"read_only": True},
        )
        storage_task_read.tags = AAZDictType()
        storage_task_read.type = AAZStrType(
            flags={"read_only": True},
        )

        identity = _schema_storage_task_read.identity
        identity.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )
        identity.tenant_id = AAZStrType(
            serialized_name="tenantId",
            flags={"read_only": True},
        )
        identity.type = AAZStrType(
            flags={"required": True},
        )
        identity.user_assigned_identities = AAZDictType(
            serialized_name="userAssignedIdentities",
        )

        user_assigned_identities = _schema_storage_task_read.identity.user_assigned_identities
        user_assigned_identities.Element = AAZObjectType(
            nullable=True,
        )

        _element = _schema_storage_task_read.identity.user_assigned_identities.Element
        _element.client_id = AAZStrType(
            serialized_name="clientId",
            flags={"read_only": True},
        )
        _element.principal_id = AAZStrType(
            serialized_name="principalId",
            flags={"read_only": True},
        )

        properties = _schema_storage_task_read.properties
        properties.action = AAZObjectType(
            flags={"required": True},
        )
        properties.creation_time_in_utc = AAZStrType(
            serialized_name="creationTimeInUtc",
            flags={"read_only": True},
        )
        properties.description = AAZStrType(
            flags={"required": True},
        )
        properties.enabled = AAZBoolType(
            flags={"required": True},
        )
        properties.provisioning_state = AAZStrType(
            serialized_name="provisioningState",
            flags={"read_only": True},
        )
        properties.task_version = AAZIntType(
            serialized_name="taskVersion",
            flags={"read_only": True},
        )

        action = _schema_storage_task_read.properties.action
        action["else"] = AAZObjectType()
        action["if"] = AAZObjectType(
            flags={"required": True},
        )

        else_ = _schema_storage_task_read.properties.action["else"]
        else_.operations = AAZListType(
            flags={"required": True},
        )

        operations = _schema_storage_task_read.properties.action["else"].operations
        operations.Element = AAZObjectType()
        cls._build_schema_storage_task_operation_read(operations.Element)

        if_ = _schema_storage_task_read.properties.action["if"]
        if_.condition = AAZStrType(
            flags={"required": True},
        )
        if_.operations = AAZListType(
            flags={"required": True},
        )

        operations = _schema_storage_task_read.properties.action["if"].operations
        operations.Element = AAZObjectType()
        cls._build_schema_storage_task_operation_read(operations.Element)

        system_data = _schema_storage_task_read.system_data
        system_data.created_at = AAZStrType(
            serialized_name="createdAt",
        )
        system_data.created_by = AAZStrType(
            serialized_name="createdBy",
        )
        system_data.created_by_type = AAZStrType(
            serialized_name="createdByType",
        )
        system_data.last_modified_at = AAZStrType(
            serialized_name="lastModifiedAt",
        )
        system_data.last_modified_by = AAZStrType(
            serialized_name="lastModifiedBy",
        )
        system_data.last_modified_by_type = AAZStrType(
            serialized_name="lastModifiedByType",
        )

        tags = _schema_storage_task_read.tags
        tags.Element = AAZStrType()

        _schema.id = cls._schema_storage_task_read.id
        _schema.identity = cls._schema_storage_task_read.identity
        _schema.location = cls._schema_storage_task_read.location
        _schema.name = cls._schema_storage_task_read.name
        _schema.properties = cls._schema_storage_task_read.properties
        _schema.system_data = cls._schema_storage_task_read.system_data
        _schema.tags = cls._schema_storage_task_read.tags
        _schema.type = cls._schema_storage_task_read.type


__all__ = ["Update"]
