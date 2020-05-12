# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetCustomDbRolesResult:
    """
    A collection of values returned by getCustomDbRoles.
    """
    def __init__(__self__, id=None, project_id=None, results=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if results and not isinstance(results, list):
            raise TypeError("Expected argument 'results' to be a list")
        __self__.results = results
        """
        A list where each represents a custom db roles.
        """
class AwaitableGetCustomDbRolesResult(GetCustomDbRolesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomDbRolesResult(
            id=self.id,
            project_id=self.project_id,
            results=self.results)

def get_custom_db_roles(project_id=None,opts=None):
    """
    `.getCustomDbRoles` describe all Custom DB Roles. This represents a custom db roles.

    > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_mongodbatlas as mongodbatlas

    test_database_user = mongodbatlas.DatabaseUser("testDatabaseUser",
        database_name="admin",
        password="test-acc-password",
        project_id="<PROJECT-ID>",
        roles=[
            {
                "databaseName": "admin",
                "roleName": "readWrite",
            },
            {
                "databaseName": "admin",
                "roleName": "atlasAdmin",
            },
        ],
        username="test-acc-username")
    test_custom_db_roles = mongodbatlas.get_custom_db_roles(project_id=mongodbatlas_custom_db_role["test"]["project_id"])
    ```



    :param str project_id: The unique ID for the project to get all custom db roles.
    """
    __args__ = dict()


    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getCustomDbRoles:getCustomDbRoles', __args__, opts=opts).value

    return AwaitableGetCustomDbRolesResult(
        id=__ret__.get('id'),
        project_id=__ret__.get('projectId'),
        results=__ret__.get('results'))
