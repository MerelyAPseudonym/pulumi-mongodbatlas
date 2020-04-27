# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Auditing(pulumi.CustomResource):
    audit_authorization_success: pulumi.Output[bool]
    """
    JSON-formatted audit filter used by the project
    """
    audit_filter: pulumi.Output[str]
    """
    Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
    """
    configuration_type: pulumi.Output[str]
    """
    Denotes the configuration method for the audit filter. Possible values are: 
    * NONE - auditing not configured for the project.
    * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
    * FILTER_JSON - auditing configured via Atlas custom filter or API.
    """
    enabled: pulumi.Output[bool]
    """
    Denotes whether or not the project associated with the {project_id} has database auditing enabled.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to configure auditing.
    """
    def __init__(__self__, resource_name, opts=None, audit_authorization_success=None, audit_filter=None, enabled=None, project_id=None, __props__=None, __name__=None, __opts__=None):
        """
        `.Auditing` provides an Auditing resource. This allows auditing to be created.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_authorization_success: JSON-formatted audit filter used by the project
        :param pulumi.Input[str] audit_filter: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['audit_authorization_success'] = audit_authorization_success
            __props__['audit_filter'] = audit_filter
            __props__['enabled'] = enabled
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['configuration_type'] = None
        super(Auditing, __self__).__init__(
            'mongodbatlas:index/auditing:Auditing',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, audit_authorization_success=None, audit_filter=None, configuration_type=None, enabled=None, project_id=None):
        """
        Get an existing Auditing resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] audit_authorization_success: JSON-formatted audit filter used by the project
        :param pulumi.Input[str] audit_filter: Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
        :param pulumi.Input[str] configuration_type: Denotes the configuration method for the audit filter. Possible values are: 
               * NONE - auditing not configured for the project.
               * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
               * FILTER_JSON - auditing configured via Atlas custom filter or API.
        :param pulumi.Input[bool] enabled: Denotes whether or not the project associated with the {project_id} has database auditing enabled.
        :param pulumi.Input[str] project_id: The unique ID for the project to configure auditing.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["audit_authorization_success"] = audit_authorization_success
        __props__["audit_filter"] = audit_filter
        __props__["configuration_type"] = configuration_type
        __props__["enabled"] = enabled
        __props__["project_id"] = project_id
        return Auditing(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

