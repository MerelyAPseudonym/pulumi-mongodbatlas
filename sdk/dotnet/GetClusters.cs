// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas
{
    public static class GetClusters
    {
        /// <summary>
        /// `mongodbatlas.Cluster` describes all Clusters by the provided project_id. The data source requires your Project ID.
        /// 
        /// &gt; **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        /// 
        /// &gt; **IMPORTANT:**
        /// &lt;br&gt; &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see [Billing](https://docs.atlas.mongodb.com/billing/).
        /// &lt;br&gt; &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Mongodbatlas = Pulumi.Mongodbatlas;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var testCluster = new Mongodbatlas.Cluster("testCluster", new Mongodbatlas.ClusterArgs
        ///         {
        ///             ProjectId = "&lt;YOUR-PROJECT-ID&gt;",
        ///             DiskSizeGb = 100,
        ///             NumShards = 1,
        ///             ReplicationFactor = 3,
        ///             ProviderBackupEnabled = true,
        ///             AutoScalingDiskGbEnabled = true,
        ///             ProviderName = "AWS",
        ///             ProviderDiskIops = 300,
        ///             ProviderVolumeType = "STANDARD",
        ///             ProviderEncryptEbsVolume = true,
        ///             ProviderInstanceSizeName = "M40",
        ///             ProviderRegionName = "US_EAST_1",
        ///         });
        ///         var testClusters = testCluster.ProjectId.Apply(projectId =&gt; Mongodbatlas.GetClusters.InvokeAsync(new Mongodbatlas.GetClustersArgs
        ///         {
        ///             ProjectId = projectId,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetClustersResult> InvokeAsync(GetClustersArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClustersResult>("mongodbatlas:index/getClusters:getClusters", args ?? new GetClustersArgs(), options.WithVersion());
    }


    public sealed class GetClustersArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID for the project to get the clusters.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetClustersArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetClustersResult
    {
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ProjectId;
        /// <summary>
        /// A list where each represents a Cluster. See Cluster below for more details.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetClustersResultResult> Results;

        [OutputConstructor]
        private GetClustersResult(
            string id,

            string projectId,

            ImmutableArray<Outputs.GetClustersResultResult> results)
        {
            Id = id;
            ProjectId = projectId;
            Results = results;
        }
    }
}
