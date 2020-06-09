# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class DatabaseUser(pulumi.CustomResource):
    auth_database_name: pulumi.Output[str]
    """
    The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
    """
    database_name: pulumi.Output[str]
    """
    Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
    """
    labels: pulumi.Output[list]
    password: pulumi.Output[str]
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    """
    roles: pulumi.Output[list]
    """
    List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.

      * `collectionName` (`str`) - Collection for which the role applies. You can specify a collection for the `read` and `readWrite` roles. If you do not specify a collection for `read` and `readWrite`, the role applies to all collections in the database (excluding some collections in the `system`. database).
      * `database_name` (`str`) - Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
      * `role_name` (`str`) - Name of the role to grant. See [Create a Database User](https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/) `roles.roleName` for valid values and restrictions.
    """
    username: pulumi.Output[str]
    """
    Username for authenticating to MongoDB.
    """
    x509_type: pulumi.Output[str]
    """
    X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:
    """
    def __init__(__self__, resource_name, opts=None, auth_database_name=None, database_name=None, labels=None, password=None, project_id=None, roles=None, username=None, x509_type=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a DatabaseUser resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_database_name: The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param pulumi.Input[str] database_name: Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[list] roles: List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.
        :param pulumi.Input[str] username: Username for authenticating to MongoDB.
        :param pulumi.Input[str] x509_type: X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:

        The **labels** object supports the following:

          * `key` (`pulumi.Input[str]`) - The key that you want to write.
          * `value` (`pulumi.Input[str]`) - The value that you want to write.

        The **roles** object supports the following:

          * `collectionName` (`pulumi.Input[str]`) - Collection for which the role applies. You can specify a collection for the `read` and `readWrite` roles. If you do not specify a collection for `read` and `readWrite`, the role applies to all collections in the database (excluding some collections in the `system`. database).
          * `database_name` (`pulumi.Input[str]`) - Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
          * `role_name` (`pulumi.Input[str]`) - Name of the role to grant. See [Create a Database User](https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/) `roles.roleName` for valid values and restrictions.
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

            __props__['auth_database_name'] = auth_database_name
            if database_name is not None:
                warnings.warn("use auth_database_name instead", DeprecationWarning)
                pulumi.log.warn("database_name is deprecated: use auth_database_name instead")
            __props__['database_name'] = database_name
            __props__['labels'] = labels
            __props__['password'] = password
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['roles'] = roles
            if username is None:
                raise TypeError("Missing required property 'username'")
            __props__['username'] = username
            __props__['x509_type'] = x509_type
        super(DatabaseUser, __self__).__init__(
            'mongodbatlas:index/databaseUser:DatabaseUser',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, auth_database_name=None, database_name=None, labels=None, password=None, project_id=None, roles=None, username=None, x509_type=None):
        """
        Get an existing DatabaseUser resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_database_name: The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is always the admin database.
        :param pulumi.Input[str] database_name: Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[list] roles: List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.
        :param pulumi.Input[str] username: Username for authenticating to MongoDB.
        :param pulumi.Input[str] x509_type: X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:

        The **labels** object supports the following:

          * `key` (`pulumi.Input[str]`) - The key that you want to write.
          * `value` (`pulumi.Input[str]`) - The value that you want to write.

        The **roles** object supports the following:

          * `collectionName` (`pulumi.Input[str]`) - Collection for which the role applies. You can specify a collection for the `read` and `readWrite` roles. If you do not specify a collection for `read` and `readWrite`, the role applies to all collections in the database (excluding some collections in the `system`. database).
          * `database_name` (`pulumi.Input[str]`) - Database on which the user has the specified role. A role on the `admin` database can include privileges that apply to the other databases.
          * `role_name` (`pulumi.Input[str]`) - Name of the role to grant. See [Create a Database User](https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/) `roles.roleName` for valid values and restrictions.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["auth_database_name"] = auth_database_name
        __props__["database_name"] = database_name
        __props__["labels"] = labels
        __props__["password"] = password
        __props__["project_id"] = project_id
        __props__["roles"] = roles
        __props__["username"] = username
        __props__["x509_type"] = x509_type
        return DatabaseUser(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

