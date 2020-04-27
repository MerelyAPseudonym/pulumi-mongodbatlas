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
    public sealed class GlobalClusterConfigManagedNamespace
    {
        /// <summary>
        /// The name of the collection associated with the managed namespace.
        /// </summary>
        public readonly string Collection;
        /// <summary>
        /// The custom shard key for the collection. Global Clusters require a compound shard key consisting of a location field and a user-selected second key, the custom shard key.
        /// </summary>
        public readonly string CustomShardKey;
        /// <summary>
        /// The name of the database containing the collection.
        /// </summary>
        public readonly string Db;

        [OutputConstructor]
        private GlobalClusterConfigManagedNamespace(
            string collection,

            string customShardKey,

            string db)
        {
            Collection = collection;
            CustomShardKey = customShardKey;
            Db = db;
        }
    }
}
