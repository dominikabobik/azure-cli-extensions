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
    "storagesync sync-group cloud-endpoint trigger-change-detection",
)
class TriggerChangeDetection(AAZCommand):
    """Triggers detection of changes performed on Azure File share connected to the specified Azure File Sync Cloud Endpoint.
    """

    _aaz_info = {
        "version": "2022-06-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.storagesync/storagesyncservices/{}/syncgroups/{}/cloudendpoints/{}/triggerchangedetection", "2022-06-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations, None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.cloud_endpoint_name = AAZStrArg(
            options=["-n", "--name", "--cloud-endpoint-name"],
            help="Name of Cloud Endpoint object.",
            required=True,
            id_part="child_name_2",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.storage_sync_service_name = AAZStrArg(
            options=["--storage-sync-service", "--storage-sync-service-name"],
            help="Name of Storage Sync Service resource.",
            required=True,
            id_part="name",
        )
        _args_schema.sync_group_name = AAZStrArg(
            options=["--sync-group-name"],
            help="Name of Sync Group resource.",
            required=True,
            id_part="child_name_1",
        )

        # define Arg Group "Parameters"

        _args_schema = cls._args_schema
        _args_schema.change_detection_mode = AAZStrArg(
            options=["--change-detection-mode"],
            arg_group="Parameters",
            help="Change Detection Mode. Applies to a directory specified in directoryPath parameter.",
            enum={"Default": "Default", "Recursive": "Recursive"},
        )
        _args_schema.directory_path = AAZStrArg(
            options=["--directory-path"],
            arg_group="Parameters",
            help="Relative path to a directory Azure File share for which change detection is to be performed.",
        )
        _args_schema.paths = AAZListArg(
            options=["--paths"],
            arg_group="Parameters",
            help="Array of relative paths on the Azure File share to be included in the change detection. Can be files and directories.",
        )

        paths = cls._args_schema.paths
        paths.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        yield self.CloudEndpointsTriggerChangeDetection(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    class CloudEndpointsTriggerChangeDetection(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    self.on_200,
                    self.on_error,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StorageSync/storageSyncServices/{storageSyncServiceName}/syncGroups/{syncGroupName}/cloudEndpoints/{cloudEndpointName}/triggerChangeDetection",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "cloudEndpointName", self.ctx.args.cloud_endpoint_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "storageSyncServiceName", self.ctx.args.storage_sync_service_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "syncGroupName", self.ctx.args.sync_group_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2022-06-01",
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
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("changeDetectionMode", AAZStrType, ".change_detection_mode")
            _builder.set_prop("directoryPath", AAZStrType, ".directory_path")
            _builder.set_prop("paths", AAZListType, ".paths")

            paths = _builder.get(".paths")
            if paths is not None:
                paths.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200(self, session):
            pass


class _TriggerChangeDetectionHelper:
    """Helper class for TriggerChangeDetection"""


__all__ = ["TriggerChangeDetection"]
