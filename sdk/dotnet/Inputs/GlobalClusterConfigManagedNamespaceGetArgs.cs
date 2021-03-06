// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas.Inputs
{

    public sealed class GlobalClusterConfigManagedNamespaceGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the collection associated with the managed namespace.
        /// </summary>
        [Input("collection", required: true)]
        public Input<string> Collection { get; set; } = null!;

        /// <summary>
        /// The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.
        /// </summary>
        [Input("customShardKey", required: true)]
        public Input<string> CustomShardKey { get; set; } = null!;

        /// <summary>
        /// The name of the database containing the collection.
        /// </summary>
        [Input("db", required: true)]
        public Input<string> Db { get; set; } = null!;

        public GlobalClusterConfigManagedNamespaceGetArgs()
        {
        }
    }
}
