// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `GlobalClusterConfig` describes all managed namespaces and custom zone mappings associated with the specified Global Cluster.
//
// > **NOTE:** Groups and projects are synonymous terms. You may find groupId in the official documentation.
func LookupGlobalClusterConfig(ctx *pulumi.Context, args *LookupGlobalClusterConfigArgs, opts ...pulumi.InvokeOption) (*LookupGlobalClusterConfigResult, error) {
	var rv LookupGlobalClusterConfigResult
	err := ctx.Invoke("mongodbatlas:index/getGlobalClusterConfig:getGlobalClusterConfig", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getGlobalClusterConfig.
type LookupGlobalClusterConfigArgs struct {
	ClusterName string `pulumi:"clusterName"`
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces []GetGlobalClusterConfigManagedNamespace `pulumi:"managedNamespaces"`
	// The unique ID for the project to create the database user.
	// * `clusterName - (Required) The name of the Global Cluster.
	ProjectId string `pulumi:"projectId"`
}

// A collection of values returned by getGlobalClusterConfig.
type LookupGlobalClusterConfigResult struct {
	ClusterName string `pulumi:"clusterName"`
	// A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.
	CustomZoneMapping map[string]interface{} `pulumi:"customZoneMapping"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see [Global Clusters](https://docs.atlas.mongodb.com/reference/api/global-clusters/). See Managed Namespace below for more details.
	ManagedNamespaces []GetGlobalClusterConfigManagedNamespace `pulumi:"managedNamespaces"`
	ProjectId         string                                   `pulumi:"projectId"`
}
