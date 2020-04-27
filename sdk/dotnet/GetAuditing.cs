// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Mongodbatlas
{
    public static class GetAuditing
    {
        /// <summary>
        /// `mongodbatlas..Auditing` describes a Auditing.
        /// 
        /// &gt; **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
        /// 
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetAuditingResult> InvokeAsync(GetAuditingArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAuditingResult>("mongodbatlas:index/getAuditing:getAuditing", args ?? new GetAuditingArgs(), options.WithVersion());
    }


    public sealed class GetAuditingArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The unique ID for the project to create the database user.
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetAuditingArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetAuditingResult
    {
        /// <summary>
        /// JSON-formatted audit filter used by the project
        /// </summary>
        public readonly bool AuditAuthorizationSuccess;
        /// <summary>
        /// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
        /// </summary>
        public readonly string AuditFilter;
        /// <summary>
        /// Denotes the configuration method for the audit filter. Possible values are: NONE - auditing not configured for the project.m FILTER_BUILDER - auditing configured via Atlas UI filter builderm FILTER_JSON - auditing configured via Atlas custom filter or API.
        /// </summary>
        public readonly string ConfigurationType;
        /// <summary>
        /// Denotes whether or not the project associated with the {GROUP-ID} has database auditing enabled.
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        public readonly string ProjectId;

        [OutputConstructor]
        private GetAuditingResult(
            bool auditAuthorizationSuccess,

            string auditFilter,

            string configurationType,

            bool enabled,

            string id,

            string projectId)
        {
            AuditAuthorizationSuccess = auditAuthorizationSuccess;
            AuditFilter = auditFilter;
            ConfigurationType = configurationType;
            Enabled = enabled;
            Id = id;
            ProjectId = projectId;
        }
    }
}
