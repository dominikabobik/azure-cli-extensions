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
    "devcenter admin catalog-task get-error-detail",
)
class GetErrorDetail(AAZCommand):
    """Gets customization task error details.

    :example: Get error detail
        az devcenter admin catalog-task get-error-detail --catalog-name "CentralCatalog" --task-name "SampleTask" --dev-center-name "Contoso" --resource-group "rg1"
    """

    _aaz_info = {
        "version": "2024-05-01-preview",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.devcenter/devcenters/{}/catalogs/{}/tasks/{}/geterrordetails", "2024-05-01-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.catalog_name = AAZStrArg(
            options=["--catalog-name"],
            help="The name of the catalog.",
            required=True,
            id_part="child_name_1",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        _args_schema.dev_center_name = AAZStrArg(
            options=["-d", "--dev-center", "--dev-center-name"],
            help="The name of the dev center. Use `az configure -d dev-center=<dev_center_name>` to configure a default.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-]{2,25}$",
                max_length=26,
                min_length=3,
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.task_name = AAZStrArg(
            options=["-n", "--name", "--task-name"],
            help="The name of the task.",
            required=True,
            id_part="child_name_2",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9][a-zA-Z0-9-_.]{2,62}$",
                max_length=63,
                min_length=3,
            ),
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.CustomizationTasksGetErrorDetails(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class CustomizationTasksGetErrorDetails(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.DevCenter/devcenters/{devCenterName}/catalogs/{catalogName}/tasks/{taskName}/getErrorDetails",
                **self.url_parameters
            )

        @property
        def method(self):
            return "POST"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "catalogName", self.ctx.args.catalog_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "devCenterName", self.ctx.args.dev_center_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "taskName", self.ctx.args.task_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-05-01-preview",
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

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.errors = AAZListType(
                flags={"read_only": True},
            )

            errors = cls._schema_on_200.errors
            errors.Element = AAZObjectType()

            _element = cls._schema_on_200.errors.Element
            _element.code = AAZStrType()
            _element.message = AAZStrType()

            return cls._schema_on_200


class _GetErrorDetailHelper:
    """Helper class for GetErrorDetail"""


__all__ = ["GetErrorDetail"]
