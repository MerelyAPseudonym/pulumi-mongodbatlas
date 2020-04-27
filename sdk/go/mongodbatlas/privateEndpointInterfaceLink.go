// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `.PrivateEndpointInterfaceLink` provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.
//
// > **IMPORTANT:**You must have one of the following roles to successfully handle the resource:
//   * Organization Owner
//   * Project Owner
//
// > **NOTE:** Groups and projects are synonymous terms. You may find groupId in the official documentation.
type PrivateEndpointInterfaceLink struct {
	pulumi.CustomResourceState

	// Status of the interface endpoint.
	// Returns one of the following values:
	ConnectionStatus pulumi.StringOutput `pulumi:"connectionStatus"`
	// Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.
	DeleteRequested pulumi.BoolOutput `pulumi:"deleteRequested"`
	// Error message pertaining to the interface endpoint. Returns null if there are no errors.
	ErrorMessage pulumi.StringOutput `pulumi:"errorMessage"`
	// Unique identifier of the interface endpoint you created in your VPC with the AWS resource.
	InterfaceEndpointId pulumi.StringOutput `pulumi:"interfaceEndpointId"`
	// Unique identifier of the AWS PrivateLink connection which is created by `.PrivateEndpoint` resource.
	PrivateLinkId pulumi.StringOutput `pulumi:"privateLinkId"`
	// Unique identifier for the project.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewPrivateEndpointInterfaceLink registers a new resource with the given unique name, arguments, and options.
func NewPrivateEndpointInterfaceLink(ctx *pulumi.Context,
	name string, args *PrivateEndpointInterfaceLinkArgs, opts ...pulumi.ResourceOption) (*PrivateEndpointInterfaceLink, error) {
	if args == nil || args.InterfaceEndpointId == nil {
		return nil, errors.New("missing required argument 'InterfaceEndpointId'")
	}
	if args == nil || args.PrivateLinkId == nil {
		return nil, errors.New("missing required argument 'PrivateLinkId'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &PrivateEndpointInterfaceLinkArgs{}
	}
	var resource PrivateEndpointInterfaceLink
	err := ctx.RegisterResource("mongodbatlas:index/privateEndpointInterfaceLink:PrivateEndpointInterfaceLink", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPrivateEndpointInterfaceLink gets an existing PrivateEndpointInterfaceLink resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPrivateEndpointInterfaceLink(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PrivateEndpointInterfaceLinkState, opts ...pulumi.ResourceOption) (*PrivateEndpointInterfaceLink, error) {
	var resource PrivateEndpointInterfaceLink
	err := ctx.ReadResource("mongodbatlas:index/privateEndpointInterfaceLink:PrivateEndpointInterfaceLink", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PrivateEndpointInterfaceLink resources.
type privateEndpointInterfaceLinkState struct {
	// Status of the interface endpoint.
	// Returns one of the following values:
	ConnectionStatus *string `pulumi:"connectionStatus"`
	// Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.
	DeleteRequested *bool `pulumi:"deleteRequested"`
	// Error message pertaining to the interface endpoint. Returns null if there are no errors.
	ErrorMessage *string `pulumi:"errorMessage"`
	// Unique identifier of the interface endpoint you created in your VPC with the AWS resource.
	InterfaceEndpointId *string `pulumi:"interfaceEndpointId"`
	// Unique identifier of the AWS PrivateLink connection which is created by `.PrivateEndpoint` resource.
	PrivateLinkId *string `pulumi:"privateLinkId"`
	// Unique identifier for the project.
	ProjectId *string `pulumi:"projectId"`
}

type PrivateEndpointInterfaceLinkState struct {
	// Status of the interface endpoint.
	// Returns one of the following values:
	ConnectionStatus pulumi.StringPtrInput
	// Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.
	DeleteRequested pulumi.BoolPtrInput
	// Error message pertaining to the interface endpoint. Returns null if there are no errors.
	ErrorMessage pulumi.StringPtrInput
	// Unique identifier of the interface endpoint you created in your VPC with the AWS resource.
	InterfaceEndpointId pulumi.StringPtrInput
	// Unique identifier of the AWS PrivateLink connection which is created by `.PrivateEndpoint` resource.
	PrivateLinkId pulumi.StringPtrInput
	// Unique identifier for the project.
	ProjectId pulumi.StringPtrInput
}

func (PrivateEndpointInterfaceLinkState) ElementType() reflect.Type {
	return reflect.TypeOf((*privateEndpointInterfaceLinkState)(nil)).Elem()
}

type privateEndpointInterfaceLinkArgs struct {
	// Unique identifier of the interface endpoint you created in your VPC with the AWS resource.
	InterfaceEndpointId string `pulumi:"interfaceEndpointId"`
	// Unique identifier of the AWS PrivateLink connection which is created by `.PrivateEndpoint` resource.
	PrivateLinkId string `pulumi:"privateLinkId"`
	// Unique identifier for the project.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a PrivateEndpointInterfaceLink resource.
type PrivateEndpointInterfaceLinkArgs struct {
	// Unique identifier of the interface endpoint you created in your VPC with the AWS resource.
	InterfaceEndpointId pulumi.StringInput
	// Unique identifier of the AWS PrivateLink connection which is created by `.PrivateEndpoint` resource.
	PrivateLinkId pulumi.StringInput
	// Unique identifier for the project.
	ProjectId pulumi.StringInput
}

func (PrivateEndpointInterfaceLinkArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*privateEndpointInterfaceLinkArgs)(nil)).Elem()
}
