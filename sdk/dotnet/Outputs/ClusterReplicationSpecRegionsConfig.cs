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
    public sealed class ClusterReplicationSpecRegionsConfig
    {
        /// <summary>
        /// The number of analytics nodes for Atlas to deploy to the region. Analytics nodes are useful for handling analytic data such as reporting queries from BI Connector for Atlas. Analytics nodes are read-only, and can never become the primary.
        /// </summary>
        public readonly int? AnalyticsNodes;
        /// <summary>
        /// Number of electable nodes for Atlas to deploy to the region. Electable nodes can become the primary and can facilitate local reads.
        /// </summary>
        public readonly int? ElectableNodes;
        /// <summary>
        /// Election priority of the region. For regions with only read-only nodes, set this value to 0.
        /// </summary>
        public readonly int? Priority;
        /// <summary>
        /// Number of read-only nodes for Atlas to deploy to the region. Read-only nodes can never become the primary, but can facilitate local-reads. Specify 0 if you do not want any read-only nodes in the region.
        /// </summary>
        public readonly int? ReadOnlyNodes;
        /// <summary>
        /// Name for the region specified.
        /// </summary>
        public readonly string? RegionName;

        [OutputConstructor]
        private ClusterReplicationSpecRegionsConfig(
            int? analyticsNodes,

            int? electableNodes,

            int? priority,

            int? readOnlyNodes,

            string? regionName)
        {
            AnalyticsNodes = analyticsNodes;
            ElectableNodes = electableNodes;
            Priority = priority;
            ReadOnlyNodes = readOnlyNodes;
            RegionName = regionName;
        }
    }
}
