// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas.Inputs
{

    public sealed class ClusterReplicationSpecArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Unique identifer of the replication document for a zone in a Global Cluster.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Number of shards to deploy in the specified zone.
        /// </summary>
        [Input("numShards", required: true)]
        public Input<int> NumShards { get; set; } = null!;

        [Input("regionsConfigs")]
        private InputList<Inputs.ClusterReplicationSpecRegionsConfigArgs>? _regionsConfigs;

        /// <summary>
        /// Physical location of the region. Each regionsConfig document describes the region’s priority in elections and the number and type of MongoDB nodes Atlas deploys to the region. You must order each regionsConfigs document by regionsConfig.priority, descending. See Region Config below for more details.
        /// </summary>
        public InputList<Inputs.ClusterReplicationSpecRegionsConfigArgs> RegionsConfigs
        {
            get => _regionsConfigs ?? (_regionsConfigs = new InputList<Inputs.ClusterReplicationSpecRegionsConfigArgs>());
            set => _regionsConfigs = value;
        }

        /// <summary>
        /// Name for the zone in a Global Cluster.
        /// </summary>
        [Input("zoneName")]
        public Input<string>? ZoneName { get; set; }

        public ClusterReplicationSpecArgs()
        {
        }
    }
}
