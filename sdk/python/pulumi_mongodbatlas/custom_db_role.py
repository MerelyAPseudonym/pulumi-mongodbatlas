# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['CustomDbRole']


class CustomDbRole(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['CustomDbRoleActionArgs']]]]] = None,
                 inherited_roles: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['CustomDbRoleInheritedRoleArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        `CustomDbRole` provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.

        > **IMPORTANT** Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.

        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test_role = mongodbatlas.CustomDbRole("testRole",
            actions=[
                mongodbatlas.CustomDbRoleActionArgs(
                    action="UPDATE",
                    resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                        collection_name="",
                        database_name="anyDatabase",
                    )],
                ),
                mongodbatlas.CustomDbRoleActionArgs(
                    action="INSERT",
                    resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                        collection_name="",
                        database_name="anyDatabase",
                    )],
                ),
                mongodbatlas.CustomDbRoleActionArgs(
                    action="REMOVE",
                    resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                        collection_name="",
                        database_name="anyDatabase",
                    )],
                ),
            ],
            project_id="<PROJECT-ID>",
            role_name="myCustomRole")
        ```
        ### With Inherited Roles

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        inherited_role_one = mongodbatlas.CustomDbRole("inheritedRoleOne",
            actions=[mongodbatlas.CustomDbRoleActionArgs(
                action="INSERT",
                resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                    collection_name="",
                    database_name="anyDatabase",
                )],
            )],
            project_id="<PROJECT-ID>",
            role_name="insertRole")
        inherited_role_two = mongodbatlas.CustomDbRole("inheritedRoleTwo",
            actions=[mongodbatlas.CustomDbRoleActionArgs(
                action="SERVER_STATUS",
                resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                    cluster=True,
                )],
            )],
            project_id=inherited_role_one.project_id,
            role_name="statusServerRole")
        test_role = mongodbatlas.CustomDbRole("testRole",
            actions=[
                mongodbatlas.CustomDbRoleActionArgs(
                    action="UPDATE",
                    resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                        collection_name="",
                        database_name="anyDatabase",
                    )],
                ),
                mongodbatlas.CustomDbRoleActionArgs(
                    action="REMOVE",
                    resources=[mongodbatlas.CustomDbRoleActionResourceArgs(
                        collection_name="",
                        database_name="anyDatabase",
                    )],
                ),
            ],
            inherited_roles=[
                mongodbatlas.CustomDbRoleInheritedRoleArgs(
                    database_name="admin",
                    role_name=inherited_role_one.role_name,
                ),
                mongodbatlas.CustomDbRoleInheritedRoleArgs(
                    database_name="admin",
                    role_name=inherited_role_two.role_name,
                ),
            ],
            project_id=inherited_role_one.project_id,
            role_name="myCustomRole")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] role_name: Name of the inherited role. This can either be another custom role or a built-in role.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if actions is None:
                raise TypeError("Missing required property 'actions'")
            __props__['actions'] = actions
            __props__['inherited_roles'] = inherited_roles
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if role_name is None:
                raise TypeError("Missing required property 'role_name'")
            __props__['role_name'] = role_name
        super(CustomDbRole, __self__).__init__(
            'mongodbatlas:index/customDbRole:CustomDbRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['CustomDbRoleActionArgs']]]]] = None,
            inherited_roles: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['CustomDbRoleInheritedRoleArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            role_name: Optional[pulumi.Input[str]] = None) -> 'CustomDbRole':
        """
        Get an existing CustomDbRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] role_name: Name of the inherited role. This can either be another custom role or a built-in role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["actions"] = actions
        __props__["inherited_roles"] = inherited_roles
        __props__["project_id"] = project_id
        __props__["role_name"] = role_name
        return CustomDbRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> List['outputs.CustomDbRoleAction']:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="inheritedRoles")
    def inherited_roles(self) -> Optional[List['outputs.CustomDbRoleInheritedRole']]:
        return pulumi.get(self, "inherited_roles")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The unique ID for the project to create the database user.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> str:
        """
        Name of the inherited role. This can either be another custom role or a built-in role.
        """
        return pulumi.get(self, "role_name")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

