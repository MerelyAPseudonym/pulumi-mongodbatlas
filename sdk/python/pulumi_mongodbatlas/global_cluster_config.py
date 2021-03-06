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

__all__ = ['GlobalClusterConfig']


class GlobalClusterConfig(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 custom_zone_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigCustomZoneMappingArgs']]]]] = None,
                 managed_namespaces: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigManagedNamespaceArgs']]]]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        `GlobalClusterConfig` provides a Global Cluster Configuration resource.

        > **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.

        ## Examples Usage

        ### Example Global cluster

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        test = mongodbatlas.Cluster("test",
            project_id="<YOUR-PROJECT-ID>",
            disk_size_gb=80,
            backup_enabled=False,
            provider_backup_enabled=True,
            cluster_type="GEOSHARDED",
            provider_name="AWS",
            provider_disk_iops=240,
            provider_instance_size_name="M30",
            replication_specs=[
                mongodbatlas.ClusterReplicationSpecArgs(
                    zone_name="Zone 1",
                    num_shards=1,
                    regions_configs=[mongodbatlas.ClusterReplicationSpecRegionsConfigArgs(
                        region_name="EU_CENTRAL_1",
                        electable_nodes=3,
                        priority=7,
                        read_only_nodes=0,
                    )],
                ),
                mongodbatlas.ClusterReplicationSpecArgs(
                    zone_name="Zone 2",
                    num_shards=1,
                    regions_configs=[mongodbatlas.ClusterReplicationSpecRegionsConfigArgs(
                        region_name="US_EAST_2",
                        electable_nodes=3,
                        priority=7,
                        read_only_nodes=0,
                    )],
                ),
            ])
        config = mongodbatlas.GlobalClusterConfig("config",
            project_id=test.project_id,
            cluster_name=test.name,
            managed_namespaces=[mongodbatlas.GlobalClusterConfigManagedNamespaceArgs(
                db="mydata",
                collection="publishers",
                custom_shard_key="city",
            )],
            custom_zone_mappings=[mongodbatlas.GlobalClusterConfigCustomZoneMappingArgs(
                location="CA",
                zone="Zone 1",
            )])
        ```

        ### Example Global cluster config

        ```python
        import pulumi
        import pulumi_mongodbatlas as mongodbatlas

        cluster_test = mongodbatlas.Cluster("cluster-test",
            project_id="<YOUR-PROJECT-ID>",
            num_shards=1,
            replication_factor=3,
            backup_enabled=True,
            auto_scaling_disk_gb_enabled=True,
            mongo_db_major_version="4.0",
            provider_name="AWS",
            disk_size_gb=100,
            provider_disk_iops=300,
            provider_encrypt_ebs_volume=False,
            provider_instance_size_name="M40",
            provider_region_name="US_EAST_1")
        config = mongodbatlas.GlobalClusterConfig("config",
            project_id=mongodbatlas_cluster["test"]["project_id"],
            cluster_name=mongodbatlas_cluster["test"]["name"],
            managed_namespaces=[mongodbatlas.GlobalClusterConfigManagedNamespaceArgs(
                db="mydata",
                collection="publishers",
                custom_shard_key="city",
            )],
            custom_zone_mappings=[mongodbatlas.GlobalClusterConfigCustomZoneMappingArgs(
                location="CA",
                zone="Zone 1",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigCustomZoneMappingArgs']]]] custom_zone_mappings: Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigManagedNamespaceArgs']]]] managed_namespaces: Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
               * `cluster_name - (Required) The name of the Global Cluster.
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

            if cluster_name is None:
                raise TypeError("Missing required property 'cluster_name'")
            __props__['cluster_name'] = cluster_name
            __props__['custom_zone_mappings'] = custom_zone_mappings
            __props__['managed_namespaces'] = managed_namespaces
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['custom_zone_mapping'] = None
        super(GlobalClusterConfig, __self__).__init__(
            'mongodbatlas:index/globalClusterConfig:GlobalClusterConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_name: Optional[pulumi.Input[str]] = None,
            custom_zone_mapping: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            custom_zone_mappings: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigCustomZoneMappingArgs']]]]] = None,
            managed_namespaces: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigManagedNamespaceArgs']]]]] = None,
            project_id: Optional[pulumi.Input[str]] = None) -> 'GlobalClusterConfig':
        """
        Get an existing GlobalClusterConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] custom_zone_mapping: A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigCustomZoneMappingArgs']]]] custom_zone_mappings: Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['GlobalClusterConfigManagedNamespaceArgs']]]] managed_namespaces: Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
        :param pulumi.Input[str] project_id: The unique ID for the project to create the database user.
               * `cluster_name - (Required) The name of the Global Cluster.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cluster_name"] = cluster_name
        __props__["custom_zone_mapping"] = custom_zone_mapping
        __props__["custom_zone_mappings"] = custom_zone_mappings
        __props__["managed_namespaces"] = managed_namespaces
        __props__["project_id"] = project_id
        return GlobalClusterConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cluster_name")

    @property
    @pulumi.getter(name="customZoneMapping")
    def custom_zone_mapping(self) -> pulumi.Output[Mapping[str, Any]]:
        """
        A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
        """
        return pulumi.get(self, "custom_zone_mapping")

    @property
    @pulumi.getter(name="customZoneMappings")
    def custom_zone_mappings(self) -> pulumi.Output[Optional[List['outputs.GlobalClusterConfigCustomZoneMapping']]]:
        """
        Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
        """
        return pulumi.get(self, "custom_zone_mappings")

    @property
    @pulumi.getter(name="managedNamespaces")
    def managed_namespaces(self) -> pulumi.Output[List['outputs.GlobalClusterConfigManagedNamespace']]:
        """
        Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
        """
        return pulumi.get(self, "managed_namespaces")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The unique ID for the project to create the database user.
        * `cluster_name - (Required) The name of the Global Cluster.
        """
        return pulumi.get(self, "project_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

