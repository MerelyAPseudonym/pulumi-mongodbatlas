// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas.Outputs
{

    [OutputType]
    public sealed class ClusterReplicationSpec
    {
        /// <summary>
        /// Unique identifer of the replication document for a zone in a Global Cluster.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// Number of shards to deploy in the specified zone.
        /// </summary>
        public readonly int NumShards;
        /// <summary>
        /// Physical location of the region. Each regionsConfig document describes the region’s priority in elections and the number and type of MongoDB nodes Atlas deploys to the region. You must order each regionsConfigs document by regionsConfig.priority, descending. See Region Config below for more details.
        /// </summary>
        public readonly ImmutableArray<Outputs.ClusterReplicationSpecRegionsConfig> RegionsConfigs;
        /// <summary>
        /// Name for the zone in a Global Cluster.
        /// </summary>
        public readonly string? ZoneName;

        [OutputConstructor]
        private ClusterReplicationSpec(
            string? id,

            int numShards,

            ImmutableArray<Outputs.ClusterReplicationSpecRegionsConfig> regionsConfigs,

            string? zoneName)
        {
            Id = id;
            NumShards = numShards;
            RegionsConfigs = regionsConfigs;
            ZoneName = zoneName;
        }
    }
}
