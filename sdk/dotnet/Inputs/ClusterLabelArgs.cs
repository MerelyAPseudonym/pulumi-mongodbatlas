// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas.Inputs
{

    public sealed class ClusterLabelArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The key that you want to write.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The value that you want to write.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ClusterLabelArgs()
        {
        }
    }
}
