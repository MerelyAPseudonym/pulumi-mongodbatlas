// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `GlobalClusterConfig` provides a Global Cluster Configuration resource.
//
// > **NOTE:** Groups and projects are synonymous terms. You may find groupId in the official documentation.
//
// ## Examples Usage
//
// ### Example Global cluster
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		test, err := mongodbatlas.NewCluster(ctx, "test", &mongodbatlas.ClusterArgs{
// 			ProjectId:                pulumi.String("<YOUR-PROJECT-ID>"),
// 			DiskSizeGb:               pulumi.Float64(80),
// 			BackupEnabled:            pulumi.Bool(false),
// 			ProviderBackupEnabled:    pulumi.Bool(true),
// 			ClusterType:              pulumi.String("GEOSHARDED"),
// 			ProviderName:             pulumi.String("AWS"),
// 			ProviderDiskIops:         pulumi.Int(240),
// 			ProviderInstanceSizeName: pulumi.String("M30"),
// 			ReplicationSpecs: mongodbatlas.ClusterReplicationSpecArray{
// 				&mongodbatlas.ClusterReplicationSpecArgs{
// 					ZoneName:  pulumi.String("Zone 1"),
// 					NumShards: pulumi.Int(1),
// 					RegionsConfigs: mongodbatlas.ClusterReplicationSpecRegionsConfigArray{
// 						&mongodbatlas.ClusterReplicationSpecRegionsConfigArgs{
// 							RegionName:     pulumi.String("EU_CENTRAL_1"),
// 							ElectableNodes: pulumi.Int(3),
// 							Priority:       pulumi.Int(7),
// 							ReadOnlyNodes:  pulumi.Int(0),
// 						},
// 					},
// 				},
// 				&mongodbatlas.ClusterReplicationSpecArgs{
// 					ZoneName:  pulumi.String("Zone 2"),
// 					NumShards: pulumi.Int(1),
// 					RegionsConfigs: mongodbatlas.ClusterReplicationSpecRegionsConfigArray{
// 						&mongodbatlas.ClusterReplicationSpecRegionsConfigArgs{
// 							RegionName:     pulumi.String("US_EAST_2"),
// 							ElectableNodes: pulumi.Int(3),
// 							Priority:       pulumi.Int(7),
// 							ReadOnlyNodes:  pulumi.Int(0),
// 						},
// 					},
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mongodbatlas.NewGlobalClusterConfig(ctx, "config", &mongodbatlas.GlobalClusterConfigArgs{
// 			ProjectId:   test.ProjectId,
// 			ClusterName: test.Name,
// 			ManagedNamespaces: mongodbatlas.GlobalClusterConfigManagedNamespaceArray{
// 				&mongodbatlas.GlobalClusterConfigManagedNamespaceArgs{
// 					Db:             pulumi.String("mydata"),
// 					Collection:     pulumi.String("publishers"),
// 					CustomShardKey: pulumi.String("city"),
// 				},
// 			},
// 			CustomZoneMappings: mongodbatlas.GlobalClusterConfigCustomZoneMappingArray{
// 				&mongodbatlas.GlobalClusterConfigCustomZoneMappingArgs{
// 					Location: pulumi.String("CA"),
// 					Zone:     pulumi.String("Zone 1"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ### Example Global cluster config
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := mongodbatlas.NewCluster(ctx, "cluster_test", &mongodbatlas.ClusterArgs{
// 			ProjectId:                pulumi.String("<YOUR-PROJECT-ID>"),
// 			NumShards:                pulumi.Int(1),
// 			ReplicationFactor:        pulumi.Int(3),
// 			BackupEnabled:            pulumi.Bool(true),
// 			AutoScalingDiskGbEnabled: pulumi.Bool(true),
// 			MongoDbMajorVersion:      pulumi.String("4.0"),
// 			ProviderName:             pulumi.String("AWS"),
// 			DiskSizeGb:               pulumi.Float64(100),
// 			ProviderDiskIops:         pulumi.Int(300),
// 			ProviderEncryptEbsVolume: pulumi.Bool(false),
// 			ProviderInstanceSizeName: pulumi.String("M40"),
// 			ProviderRegionName:       pulumi.String("US_EAST_1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mongodbatlas.NewGlobalClusterConfig(ctx, "config", &mongodbatlas.GlobalClusterConfigArgs{
// 			ProjectId:   pulumi.Any(mongodbatlas_cluster.Test.Project_id),
// 			ClusterName: pulumi.Any(mongodbatlas_cluster.Test.Name),
// 			ManagedNamespaces: mongodbatlas.GlobalClusterConfigManagedNamespaceArray{
// 				&mongodbatlas.GlobalClusterConfigManagedNamespaceArgs{
// 					Db:             pulumi.String("mydata"),
// 					Collection:     pulumi.String("publishers"),
// 					CustomShardKey: pulumi.String("city"),
// 				},
// 			},
// 			CustomZoneMappings: mongodbatlas.GlobalClusterConfigCustomZoneMappingArray{
// 				&mongodbatlas.GlobalClusterConfigCustomZoneMappingArgs{
// 					Location: pulumi.String("CA"),
// 					Zone:     pulumi.String("Zone 1"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type GlobalClusterConfig struct {
	pulumi.CustomResourceState

	ClusterName pulumi.StringOutput `pulumi:"clusterName"`
	// A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
	CustomZoneMapping pulumi.MapOutput `pulumi:"customZoneMapping"`
	// Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
	CustomZoneMappings GlobalClusterConfigCustomZoneMappingArrayOutput `pulumi:"customZoneMappings"`
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces GlobalClusterConfigManagedNamespaceArrayOutput `pulumi:"managedNamespaces"`
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewGlobalClusterConfig registers a new resource with the given unique name, arguments, and options.
func NewGlobalClusterConfig(ctx *pulumi.Context,
	name string, args *GlobalClusterConfigArgs, opts ...pulumi.ResourceOption) (*GlobalClusterConfig, error) {
	if args == nil || args.ClusterName == nil {
		return nil, errors.New("missing required argument 'ClusterName'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &GlobalClusterConfigArgs{}
	}
	var resource GlobalClusterConfig
	err := ctx.RegisterResource("mongodbatlas:index/globalClusterConfig:GlobalClusterConfig", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetGlobalClusterConfig gets an existing GlobalClusterConfig resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGlobalClusterConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *GlobalClusterConfigState, opts ...pulumi.ResourceOption) (*GlobalClusterConfig, error) {
	var resource GlobalClusterConfig
	err := ctx.ReadResource("mongodbatlas:index/globalClusterConfig:GlobalClusterConfig", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering GlobalClusterConfig resources.
type globalClusterConfigState struct {
	ClusterName *string `pulumi:"clusterName"`
	// A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
	CustomZoneMapping map[string]interface{} `pulumi:"customZoneMapping"`
	// Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
	CustomZoneMappings []GlobalClusterConfigCustomZoneMapping `pulumi:"customZoneMappings"`
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces []GlobalClusterConfigManagedNamespace `pulumi:"managedNamespaces"`
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId *string `pulumi:"projectId"`
}

type GlobalClusterConfigState struct {
	ClusterName pulumi.StringPtrInput
	// A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
	CustomZoneMapping pulumi.MapInput
	// Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
	CustomZoneMappings GlobalClusterConfigCustomZoneMappingArrayInput
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces GlobalClusterConfigManagedNamespaceArrayInput
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId pulumi.StringPtrInput
}

func (GlobalClusterConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*globalClusterConfigState)(nil)).Elem()
}

type globalClusterConfigArgs struct {
	ClusterName string `pulumi:"clusterName"`
	// Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
	CustomZoneMappings []GlobalClusterConfigCustomZoneMapping `pulumi:"customZoneMappings"`
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces []GlobalClusterConfigManagedNamespace `pulumi:"managedNamespaces"`
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a GlobalClusterConfig resource.
type GlobalClusterConfigArgs struct {
	ClusterName pulumi.StringInput
	// Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.
	CustomZoneMappings GlobalClusterConfigCustomZoneMappingArrayInput
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces GlobalClusterConfigManagedNamespaceArrayInput
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId pulumi.StringInput
}

func (GlobalClusterConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*globalClusterConfigArgs)(nil)).Elem()
}
