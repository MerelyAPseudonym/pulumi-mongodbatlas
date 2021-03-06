# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = [
    'GetPrivateEndpointInterfaceLinkResult',
    'AwaitableGetPrivateEndpointInterfaceLinkResult',
    'get_private_endpoint_interface_link',
]

@pulumi.output_type
class GetPrivateEndpointInterfaceLinkResult:
    """
    A collection of values returned by getPrivateEndpointInterfaceLink.
    """
    def __init__(__self__, connection_status=None, delete_requested=None, error_message=None, id=None, interface_endpoint_id=None, private_link_id=None, project_id=None):
        if connection_status and not isinstance(connection_status, str):
            raise TypeError("Expected argument 'connection_status' to be a str")
        pulumi.set(__self__, "connection_status", connection_status)
        if delete_requested and not isinstance(delete_requested, bool):
            raise TypeError("Expected argument 'delete_requested' to be a bool")
        pulumi.set(__self__, "delete_requested", delete_requested)
        if error_message and not isinstance(error_message, str):
            raise TypeError("Expected argument 'error_message' to be a str")
        pulumi.set(__self__, "error_message", error_message)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if interface_endpoint_id and not isinstance(interface_endpoint_id, str):
            raise TypeError("Expected argument 'interface_endpoint_id' to be a str")
        pulumi.set(__self__, "interface_endpoint_id", interface_endpoint_id)
        if private_link_id and not isinstance(private_link_id, str):
            raise TypeError("Expected argument 'private_link_id' to be a str")
        pulumi.set(__self__, "private_link_id", private_link_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)

    @property
    @pulumi.getter(name="connectionStatus")
    def connection_status(self) -> str:
        """
        Status of the interface endpoint.
        Returns one of the following values:
        """
        return pulumi.get(self, "connection_status")

    @property
    @pulumi.getter(name="deleteRequested")
    def delete_requested(self) -> bool:
        """
        Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.
        """
        return pulumi.get(self, "delete_requested")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Error message pertaining to the interface endpoint. Returns null if there are no errors.
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
    @pulumi.getter(name="interfaceEndpointId")
    def interface_endpoint_id(self) -> str:
        return pulumi.get(self, "interface_endpoint_id")

    @property
    @pulumi.getter(name="privateLinkId")
    def private_link_id(self) -> str:
        return pulumi.get(self, "private_link_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")


class AwaitableGetPrivateEndpointInterfaceLinkResult(GetPrivateEndpointInterfaceLinkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointInterfaceLinkResult(
            connection_status=self.connection_status,
            delete_requested=self.delete_requested,
            error_message=self.error_message,
            id=self.id,
            interface_endpoint_id=self.interface_endpoint_id,
            private_link_id=self.private_link_id,
            project_id=self.project_id)


def get_private_endpoint_interface_link(interface_endpoint_id: Optional[str] = None,
                                        private_link_id: Optional[str] = None,
                                        project_id: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointInterfaceLinkResult:
    """
    `mongodbatlas_private_endpoint_link` describe a Private Endpoint Link. This represents a Private Endpoint Link Connection that wants to retrieve details in an Atlas project.

    > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.


    :param str private_link_id: Unique identifier of the AWS PrivateLink connection.
    :param str project_id: Unique identifier for the project.
    """
    __args__ = dict()
    __args__['interfaceEndpointId'] = interface_endpoint_id
    __args__['privateLinkId'] = private_link_id
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('mongodbatlas:index/getPrivateEndpointInterfaceLink:getPrivateEndpointInterfaceLink', __args__, opts=opts, typ=GetPrivateEndpointInterfaceLinkResult).value

    return AwaitableGetPrivateEndpointInterfaceLinkResult(
        connection_status=__ret__.connection_status,
        delete_requested=__ret__.delete_requested,
        error_message=__ret__.error_message,
        id=__ret__.id,
        interface_endpoint_id=__ret__.interface_endpoint_id,
        private_link_id=__ret__.private_link_id,
        project_id=__ret__.project_id)
