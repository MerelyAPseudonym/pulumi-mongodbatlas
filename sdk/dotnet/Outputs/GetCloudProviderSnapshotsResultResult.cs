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
    public sealed class GetCloudProviderSnapshotsResultResult
    {
        /// <summary>
        /// UTC ISO 8601 formatted point in time when Atlas took the snapshot.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// UDescription of the snapshot. Only present for on-demand snapshots.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.
        /// </summary>
        public readonly string ExpiresAt;
        /// <summary>
        /// Unique identifier of the snapshot.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.
        /// </summary>
        public readonly string MasterKeyUuid;
        /// <summary>
        /// Version of the MongoDB server.
        /// </summary>
        public readonly string MongodVersion;
        /// <summary>
        /// Specified the type of snapshot. Valid values are onDemand and scheduled.
        /// </summary>
        public readonly string SnapshotType;
        /// <summary>
        /// Current status of the snapshot. One of the following values: queued, inProgress, completed, failed.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// Specifies the size of the snapshot in bytes.
        /// </summary>
        public readonly int StorageSizeBytes;
        /// <summary>
        /// Specifies the type of cluster: replicaSet or shardedCluster.
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private GetCloudProviderSnapshotsResultResult(
            string createdAt,

            string description,

            string expiresAt,

            string id,

            string masterKeyUuid,

            string mongodVersion,

            string snapshotType,

            string status,

            int storageSizeBytes,

            string type)
        {
            CreatedAt = createdAt;
            Description = description;
            ExpiresAt = expiresAt;
            Id = id;
            MasterKeyUuid = masterKeyUuid;
            MongodVersion = mongodVersion;
            SnapshotType = snapshotType;
            Status = status;
            StorageSizeBytes = storageSizeBytes;
            Type = type;
        }
    }
}
