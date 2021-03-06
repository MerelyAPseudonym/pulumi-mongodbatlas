// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas.Inputs
{

    public sealed class EncryptionAtRestGoogleCloudKmsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies whether Encryption at Rest is enabled for an Atlas project. To disable Encryption at Rest, pass only this parameter with a value of false. When you disable Encryption at Rest, Atlas also removes the configuration details.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        /// <summary>
        /// The Key Version Resource ID from your GCP account.
        /// </summary>
        [Input("keyVersionResourceId", required: true)]
        public Input<string> KeyVersionResourceId { get; set; } = null!;

        /// <summary>
        /// String-formatted JSON object containing GCP KMS credentials from your GCP account.
        /// </summary>
        [Input("serviceAccountKey", required: true)]
        public Input<string> ServiceAccountKey { get; set; } = null!;

        public EncryptionAtRestGoogleCloudKmsArgs()
        {
        }
    }
}
