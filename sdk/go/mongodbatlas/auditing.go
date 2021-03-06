// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `Auditing` provides an Auditing resource. This allows auditing to be created.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := mongodbatlas.NewAuditing(ctx, "test", &mongodbatlas.AuditingArgs{
// 			AuditAuthorizationSuccess: pulumi.Bool(false),
// 			AuditFilter:               pulumi.String("{ 'atype': 'authenticate', 'param': {   'user': 'auditAdmin',   'db': 'admin',   'mechanism': 'SCRAM-SHA-1' }}"),
// 			Enabled:                   pulumi.Bool(true),
// 			ProjectId:                 pulumi.String("<project-id>"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Auditing struct {
	pulumi.CustomResourceState

	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess pulumi.BoolOutput `pulumi:"auditAuthorizationSuccess"`
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter pulumi.StringOutput `pulumi:"auditFilter"`
	// Denotes the configuration method for the audit filter. Possible values are:
	// * NONE - auditing not configured for the project.
	// * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
	// * FILTER_JSON - auditing configured via Atlas custom filter or API.
	ConfigurationType pulumi.StringOutput `pulumi:"configurationType"`
	// Denotes whether or not the project associated with the {project_id} has database auditing enabled.
	Enabled pulumi.BoolOutput `pulumi:"enabled"`
	// The unique ID for the project to configure auditing.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewAuditing registers a new resource with the given unique name, arguments, and options.
func NewAuditing(ctx *pulumi.Context,
	name string, args *AuditingArgs, opts ...pulumi.ResourceOption) (*Auditing, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &AuditingArgs{}
	}
	var resource Auditing
	err := ctx.RegisterResource("mongodbatlas:index/auditing:Auditing", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAuditing gets an existing Auditing resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAuditing(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AuditingState, opts ...pulumi.ResourceOption) (*Auditing, error) {
	var resource Auditing
	err := ctx.ReadResource("mongodbatlas:index/auditing:Auditing", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Auditing resources.
type auditingState struct {
	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess *bool `pulumi:"auditAuthorizationSuccess"`
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter *string `pulumi:"auditFilter"`
	// Denotes the configuration method for the audit filter. Possible values are:
	// * NONE - auditing not configured for the project.
	// * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
	// * FILTER_JSON - auditing configured via Atlas custom filter or API.
	ConfigurationType *string `pulumi:"configurationType"`
	// Denotes whether or not the project associated with the {project_id} has database auditing enabled.
	Enabled *bool `pulumi:"enabled"`
	// The unique ID for the project to configure auditing.
	ProjectId *string `pulumi:"projectId"`
}

type AuditingState struct {
	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess pulumi.BoolPtrInput
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter pulumi.StringPtrInput
	// Denotes the configuration method for the audit filter. Possible values are:
	// * NONE - auditing not configured for the project.
	// * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
	// * FILTER_JSON - auditing configured via Atlas custom filter or API.
	ConfigurationType pulumi.StringPtrInput
	// Denotes whether or not the project associated with the {project_id} has database auditing enabled.
	Enabled pulumi.BoolPtrInput
	// The unique ID for the project to configure auditing.
	ProjectId pulumi.StringPtrInput
}

func (AuditingState) ElementType() reflect.Type {
	return reflect.TypeOf((*auditingState)(nil)).Elem()
}

type auditingArgs struct {
	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess *bool `pulumi:"auditAuthorizationSuccess"`
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter *string `pulumi:"auditFilter"`
	// Denotes whether or not the project associated with the {project_id} has database auditing enabled.
	Enabled *bool `pulumi:"enabled"`
	// The unique ID for the project to configure auditing.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a Auditing resource.
type AuditingArgs struct {
	// JSON-formatted audit filter used by the project
	AuditAuthorizationSuccess pulumi.BoolPtrInput
	// Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
	AuditFilter pulumi.StringPtrInput
	// Denotes whether or not the project associated with the {project_id} has database auditing enabled.
	Enabled pulumi.BoolPtrInput
	// The unique ID for the project to configure auditing.
	ProjectId pulumi.StringInput
}

func (AuditingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*auditingArgs)(nil)).Elem()
}
