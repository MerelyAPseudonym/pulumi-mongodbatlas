// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas
{
    public static class GetPrivateEndpoint
    {
        /// <summary>
        /// `mongodbatlas..PrivateEndpoint` describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project
        /// 
        /// &gt; **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPrivateEndpointResult> InvokeAsync(GetPrivateEndpointArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPrivateEndpointResult>("mongodbatlas:index/getPrivateEndpoint:getPrivateEndpoint", args ?? new GetPrivateEndpointArgs(), options.WithVersion());
    }


    public sealed class GetPrivateEndpointArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Unique identifier of the AWS PrivateLink connection.
        /// </summary>
        [Input("privateLinkId", required: true)]
        public string PrivateLinkId { get; set; } = null!;

        /// <summary>
        /// Unique identifier for the project.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetPrivateEndpointArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPrivateEndpointResult
    {
        /// <summary>
        /// Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.
        /// </summary>
        public readonly string EndpointServiceName;
        /// <summary>
        /// Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.
        /// </summary>
        public readonly string ErrorMessage;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.
        /// </summary>
        public readonly ImmutableArray<string> InterfaceEndpoints;
        public readonly string PrivateLinkId;
        public readonly string ProjectId;
        /// <summary>
        /// Status of the AWS PrivateLink connection.
        /// Returns one of the following values:
        /// </summary>
        public readonly string Status;

        [OutputConstructor]
        private GetPrivateEndpointResult(
            string endpointServiceName,

            string errorMessage,

            string id,

            ImmutableArray<string> interfaceEndpoints,

            string privateLinkId,

            string projectId,

            string status)
        {
            EndpointServiceName = endpointServiceName;
            ErrorMessage = errorMessage;
            Id = id;
            InterfaceEndpoints = interfaceEndpoints;
            PrivateLinkId = privateLinkId;
            ProjectId = projectId;
            Status = status;
        }
    }
}
