# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetPrivateEndpointResult:
    """
    A collection of values returned by getPrivateEndpoint.
    """
    def __init__(__self__, endpoint_service_name=None, error_message=None, id=None, interface_endpoints=None, private_link_id=None, project_id=None, status=None):
        if endpoint_service_name and not isinstance(endpoint_service_name, str):
            raise TypeError("Expected argument 'endpoint_service_name' to be a str")
        __self__.endpoint_service_name = endpoint_service_name
        """
        Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        """
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        __self__.error_message = error_message
        """
        Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if interface_endpoints and not isinstance(interface_endpoints, list):
            raise TypeError("Expected argument 'interface_endpoints' to be a list")
        __self__.interface_endpoints = interface_endpoints
        """
        Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        """
        if private_link_id and not isinstance(private_link_id, str):
            raise TypeError("Expected argument 'private_link_id' to be a str")
        __self__.private_link_id = private_link_id
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        __self__.status = status
        """
        Status of the AWS PrivateLink connection.
        Returns one of the following values:
        """
class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointResult(
            endpoint_service_name=self.endpoint_service_name,
            error_message=self.error_message,
            id=self.id,
            interface_endpoints=self.interface_endpoints,
            private_link_id=self.private_link_id,
            project_id=self.project_id,
            status=self.status)

def get_private_endpoint(private_link_id=None,project_id=None,opts=None):
    """
    `.PrivateEndpoint` describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.




    :param str private_link_id: Unique identifier of the AWS PrivateLink connection.
    :param str project_id: Unique identifier for the project.
    """
    __args__ = dict()


    __args__['privateLinkId'] = private_link_id
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getPrivateEndpoint:getPrivateEndpoint', __args__, opts=opts).value

    return AwaitableGetPrivateEndpointResult(
        endpoint_service_name=__ret__.get('endpointServiceName'),
        error_message=__ret__.get('errorMessage'),
        id=__ret__.get('id'),
        interface_endpoints=__ret__.get('interfaceEndpoints'),
        private_link_id=__ret__.get('privateLinkId'),
        project_id=__ret__.get('projectId'),
        status=__ret__.get('status'))
