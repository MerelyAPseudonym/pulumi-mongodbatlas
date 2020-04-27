// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas
{
    public static class Get509AuthenticationDatabaseUser
    {
        /// <summary>
        /// `mongodbatlas..X509AuthenticationDatabaseUser` describe a X509 Authentication Database User. This represents a X509 Authentication Database User.
        /// 
        /// &gt; **NOTE:** Groups and projects are synonymous terms. You may find group_id in the official documentation.
        /// </summary>
        public static Task<Get509AuthenticationDatabaseUserResult> InvokeAsync(Get509AuthenticationDatabaseUserArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<Get509AuthenticationDatabaseUserResult>("mongodbatlas:index/get509AuthenticationDatabaseUser:get509AuthenticationDatabaseUser", args ?? new Get509AuthenticationDatabaseUserArgs(), options.WithVersion());
    }


    public sealed class Get509AuthenticationDatabaseUserArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Identifier for the Atlas project associated with the X.509 configuration.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        /// <summary>
        /// Username of the database user to create a certificate for.
        /// </summary>
        [Input("username")]
        public string? Username { get; set; }

        public Get509AuthenticationDatabaseUserArgs()
        {
        }
    }


    [OutputType]
    public sealed class Get509AuthenticationDatabaseUserResult
    {
        /// <summary>
        /// Array of objects where each details one unexpired database user certificate.
        /// </summary>
        public readonly ImmutableArray<Outputs.Get509AuthenticationDatabaseUserCertificateResult> Certificates;
        public readonly string CustomerX509Cas;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ProjectId;
        public readonly string? Username;

        [OutputConstructor]
        private Get509AuthenticationDatabaseUserResult(
            ImmutableArray<Outputs.Get509AuthenticationDatabaseUserCertificateResult> certificates,

            string customerX509Cas,

            string id,

            string projectId,

            string? username)
        {
            Certificates = certificates;
            CustomerX509Cas = customerX509Cas;
            Id = id;
            ProjectId = projectId;
            Username = username;
        }
    }
}
