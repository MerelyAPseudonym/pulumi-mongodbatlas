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
    public sealed class GetClusterConnectionStringsResult
    {
        public readonly ImmutableDictionary<string, object> AwsPrivateLink;
        public readonly ImmutableDictionary<string, object> AwsPrivateLinkSrv;
        public readonly string Private;
        public readonly string PrivateSrv;
        public readonly string Standard;
        public readonly string StandardSrv;

        [OutputConstructor]
        private GetClusterConnectionStringsResult(
            ImmutableDictionary<string, object> awsPrivateLink,

            ImmutableDictionary<string, object> awsPrivateLinkSrv,

            string @private,

            string privateSrv,

            string standard,

            string standardSrv)
        {
            AwsPrivateLink = awsPrivateLink;
            AwsPrivateLinkSrv = awsPrivateLinkSrv;
            Private = @private;
            PrivateSrv = privateSrv;
            Standard = standard;
            StandardSrv = standardSrv;
        }
    }
}
