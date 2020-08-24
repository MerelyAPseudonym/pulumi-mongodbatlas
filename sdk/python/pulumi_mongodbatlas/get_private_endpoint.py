# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetPrivateEndpointResult',
    'AwaitableGetPrivateEndpointResult',
    'get_private_endpoint',
]

@pulumi.output_type
class GetPrivateEndpointResult:
    """
    A collection of values returned by getPrivateEndpoint.
    """
    def __init__(__self__, endpoint_service_name=None, error_message=None, id=None, interface_endpoints=None, private_link_id=None, project_id=None, status=None):
        if endpoint_service_name and not isinstance(endpoint_service_name, str):
            raise TypeError("Expected argument 'endpoint_service_name' to be a str")
        pulumi.set(__self__, "endpoint_service_name", endpoint_service_name)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_endpoints and not isinstance(interface_endpoints, list):
            raise TypeError("Expected argument 'interface_endpoints' to be a list")
        pulumi.set(__self__, "interface_endpoints", interface_endpoints)
        if private_link_id and not isinstance(private_link_id, str):
            raise TypeError("Expected argument 'private_link_id' to be a str")
        pulumi.set(__self__, "private_link_id", private_link_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="endpointServiceName")
    def endpoint_service_name(self) -> str:
        """
        Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        """
        return pulumi.get(self, "endpoint_service_name")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="interfaceEndpoints")
    def interface_endpoints(self) -> List[str]:
        """
        Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        """
        return pulumi.get(self, "interface_endpoints")

    @property
    @pulumi.getter(name="privateLinkId")
    def private_link_id(self) -> str:
        return pulumi.get(self, "private_link_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the AWS PrivateLink connection.
        Returns one of the following values:
        """
        return pulumi.get(self, "status")


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


def get_private_endpoint(private_link_id: Optional[str] = None,
                         project_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointResult:
    """
    `PrivateEndpoint` describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project

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
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getPrivateEndpoint:getPrivateEndpoint', __args__, opts=opts, typ=GetPrivateEndpointResult).value

    return AwaitableGetPrivateEndpointResult(
        endpoint_service_name=__ret__.endpoint_service_name,
        error_message=__ret__.error_message,
        id=__ret__.id,
        interface_endpoints=__ret__.interface_endpoints,
        private_link_id=__ret__.private_link_id,
        project_id=__ret__.project_id,
        status=__ret__.status)
