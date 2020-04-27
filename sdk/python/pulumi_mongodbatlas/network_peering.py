# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class NetworkPeering(pulumi.CustomResource):
    accepter_region_name: pulumi.Output[str]
    """
    Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
    """
    atlas_cidr_block: pulumi.Output[str]
    """
    Unique identifier for an Azure AD directory.
    """
    atlas_gcp_project_id: pulumi.Output[str]
    """
    The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
    """
    atlas_id: pulumi.Output[str]
    atlas_vpc_name: pulumi.Output[str]
    """
    The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
    """
    aws_account_id: pulumi.Output[str]
    """
    Account ID of the owner of the peer VPC.
    """
    azure_directory_id: pulumi.Output[str]
    """
    Unique identifier for an Azure AD directory.
    """
    azure_subscription_id: pulumi.Output[str]
    """
    Unique identifer of the Azure subscription in which the VNet resides.
    """
    connection_id: pulumi.Output[str]
    """
    Unique identifier for the peering connection.
    """
    container_id: pulumi.Output[str]
    """
    Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
    """
    error_message: pulumi.Output[str]
    """
    When `"status" : "FAILED"`, Atlas provides a description of the error.
    """
    error_state: pulumi.Output[str]
    """
    Description of the Atlas error when `status` is `Failed`, Otherwise, Atlas returns `null`.
    """
    error_state_name: pulumi.Output[str]
    """
    Error state, if any. The VPC peering connection error state value can be one of the following: `REJECTED`, `EXPIRED`, `INVALID_ARGUMENT`.
    """
    gcp_project_id: pulumi.Output[str]
    """
    GCP project ID of the owner of the network peer.
    """
    network_name: pulumi.Output[str]
    """
    Name of the network peer to which Atlas connects.
    """
    peer_id: pulumi.Output[str]
    """
    The Network Peering Container ID.
    """
    project_id: pulumi.Output[str]
    """
    The unique ID for the project to create the database user.
    """
    provider_name: pulumi.Output[str]
    """
    Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
    """
    resource_group_name: pulumi.Output[str]
    """
    Name of your Azure resource group.
    """
    route_table_cidr_block: pulumi.Output[str]
    """
    Peer VPC CIDR block or subnet.
    """
    status: pulumi.Output[str]
    """
    (Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: `ADDING_PEER`, `AVAILABLE`, `FAILED`, `DELETING` GCP Only:  `WAITING_FOR_USER`.
    """
    status_name: pulumi.Output[str]
    """
    (AWS Only) The VPC peering connection status value can be one of the following: `INITIATING`, `PENDING_ACCEPTANCE`, `FAILED`, `FINALIZING`, `AVAILABLE`, `TERMINATING`.
    """
    vnet_name: pulumi.Output[str]
    """
    Name of your Azure VNet.
    """
    vpc_id: pulumi.Output[str]
    """
    Unique identifier of the peer VPC.
    """
    def __init__(__self__, resource_name, opts=None, accepter_region_name=None, atlas_cidr_block=None, atlas_gcp_project_id=None, atlas_vpc_name=None, aws_account_id=None, azure_directory_id=None, azure_subscription_id=None, container_id=None, gcp_project_id=None, network_name=None, project_id=None, provider_name=None, resource_group_name=None, route_table_cidr_block=None, vnet_name=None, vpc_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a NetworkPeering resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepter_region_name: Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
        :param pulumi.Input[str] atlas_cidr_block: Unique identifier for an Azure AD directory.
        :param pulumi.Input[str] atlas_gcp_project_id: The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
        :param pulumi.Input[str] atlas_vpc_name: The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
        :param pulumi.Input[str] aws_account_id: Account ID of the owner of the peer VPC.
        :param pulumi.Input[str] azure_directory_id: Unique identifier for an Azure AD directory.
        :param pulumi.Input[str] azure_subscription_id: Unique identifer of the Azure subscription in which the VNet resides.
        :param pulumi.Input[str] container_id: Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
        :param pulumi.Input[str] gcp_project_id: GCP project ID of the owner of the network peer.
        :param pulumi.Input[str] network_name: Name of the network peer to which Atlas connects.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] provider_name: Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
        :param pulumi.Input[str] resource_group_name: Name of your Azure resource group.
        :param pulumi.Input[str] route_table_cidr_block: Peer VPC CIDR block or subnet.
        :param pulumi.Input[str] vnet_name: Name of your Azure VNet.
        :param pulumi.Input[str] vpc_id: Unique identifier of the peer VPC.
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

            __props__['accepter_region_name'] = accepter_region_name
            __props__['atlas_cidr_block'] = atlas_cidr_block
            __props__['atlas_gcp_project_id'] = atlas_gcp_project_id
            __props__['atlas_vpc_name'] = atlas_vpc_name
            __props__['aws_account_id'] = aws_account_id
            __props__['azure_directory_id'] = azure_directory_id
            __props__['azure_subscription_id'] = azure_subscription_id
            if container_id is None:
                raise TypeError("Missing required property 'container_id'")
            __props__['container_id'] = container_id
            __props__['gcp_project_id'] = gcp_project_id
            __props__['network_name'] = network_name
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if provider_name is None:
                raise TypeError("Missing required property 'provider_name'")
            __props__['provider_name'] = provider_name
            __props__['resource_group_name'] = resource_group_name
            __props__['route_table_cidr_block'] = route_table_cidr_block
            __props__['vnet_name'] = vnet_name
            __props__['vpc_id'] = vpc_id
            __props__['atlas_id'] = None
            __props__['connection_id'] = None
            __props__['error_message'] = None
            __props__['error_state'] = None
            __props__['error_state_name'] = None
            __props__['peer_id'] = None
            __props__['status'] = None
            __props__['status_name'] = None
        super(NetworkPeering, __self__).__init__(
            'mongodbatlas:index/networkPeering:NetworkPeering',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, accepter_region_name=None, atlas_cidr_block=None, atlas_gcp_project_id=None, atlas_id=None, atlas_vpc_name=None, aws_account_id=None, azure_directory_id=None, azure_subscription_id=None, connection_id=None, container_id=None, error_message=None, error_state=None, error_state_name=None, gcp_project_id=None, network_name=None, peer_id=None, project_id=None, provider_name=None, resource_group_name=None, route_table_cidr_block=None, status=None, status_name=None, vnet_name=None, vpc_id=None):
        """
        Get an existing NetworkPeering resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accepter_region_name: Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
        :param pulumi.Input[str] atlas_cidr_block: Unique identifier for an Azure AD directory.
        :param pulumi.Input[str] atlas_gcp_project_id: The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
        :param pulumi.Input[str] atlas_vpc_name: The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
        :param pulumi.Input[str] aws_account_id: Account ID of the owner of the peer VPC.
        :param pulumi.Input[str] azure_directory_id: Unique identifier for an Azure AD directory.
        :param pulumi.Input[str] azure_subscription_id: Unique identifer of the Azure subscription in which the VNet resides.
        :param pulumi.Input[str] connection_id: Unique identifier for the peering connection.
        :param pulumi.Input[str] container_id: Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
        :param pulumi.Input[str] error_message: When `"status" : "FAILED"`, Atlas provides a description of the error.
        :param pulumi.Input[str] error_state: Description of the Atlas error when `status` is `Failed`, Otherwise, Atlas returns `null`.
        :param pulumi.Input[str] error_state_name: Error state, if any. The VPC peering connection error state value can be one of the following: `REJECTED`, `EXPIRED`, `INVALID_ARGUMENT`.
        :param pulumi.Input[str] gcp_project_id: GCP project ID of the owner of the network peer.
        :param pulumi.Input[str] network_name: Name of the network peer to which Atlas connects.
        :param pulumi.Input[str] peer_id: The Network Peering Container ID.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
        :param pulumi.Input[str] provider_name: Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
        :param pulumi.Input[str] resource_group_name: Name of your Azure resource group.
        :param pulumi.Input[str] route_table_cidr_block: Peer VPC CIDR block or subnet.
        :param pulumi.Input[str] status: (Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: `ADDING_PEER`, `AVAILABLE`, `FAILED`, `DELETING` GCP Only:  `WAITING_FOR_USER`.
        :param pulumi.Input[str] status_name: (AWS Only) The VPC peering connection status value can be one of the following: `INITIATING`, `PENDING_ACCEPTANCE`, `FAILED`, `FINALIZING`, `AVAILABLE`, `TERMINATING`.
        :param pulumi.Input[str] vnet_name: Name of your Azure VNet.
        :param pulumi.Input[str] vpc_id: Unique identifier of the peer VPC.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["accepter_region_name"] = accepter_region_name
        __props__["atlas_cidr_block"] = atlas_cidr_block
        __props__["atlas_gcp_project_id"] = atlas_gcp_project_id
        __props__["atlas_id"] = atlas_id
        __props__["atlas_vpc_name"] = atlas_vpc_name
        __props__["aws_account_id"] = aws_account_id
        __props__["azure_directory_id"] = azure_directory_id
        __props__["azure_subscription_id"] = azure_subscription_id
        __props__["connection_id"] = connection_id
        __props__["container_id"] = container_id
        __props__["error_message"] = error_message
        __props__["error_state"] = error_state
        __props__["error_state_name"] = error_state_name
        __props__["gcp_project_id"] = gcp_project_id
        __props__["network_name"] = network_name
        __props__["peer_id"] = peer_id
        __props__["project_id"] = project_id
        __props__["provider_name"] = provider_name
        __props__["resource_group_name"] = resource_group_name
        __props__["route_table_cidr_block"] = route_table_cidr_block
        __props__["status"] = status
        __props__["status_name"] = status_name
        __props__["vnet_name"] = vnet_name
        __props__["vpc_id"] = vpc_id
        return NetworkPeering(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

