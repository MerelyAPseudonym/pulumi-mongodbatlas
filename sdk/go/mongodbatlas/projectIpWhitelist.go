// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `.ProjectIpWhitelist` provides an IP Whitelist entry resource. The whitelist grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.
//
// > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
//
// > **IMPORTANT:**
// When you remove an entry from the whitelist, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.
type ProjectIpWhitelist struct {
	pulumi.CustomResourceState

	// ID of the whitelisted AWS security group. Mutually exclusive with `cidrBlock` and `ipAddress`.
	AwsSecurityGroup pulumi.StringOutput `pulumi:"awsSecurityGroup"`
	// Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with `awsSecurityGroup` and `ipAddress`.
	CidrBlock pulumi.StringOutput `pulumi:"cidrBlock"`
	// Comment to add to the whitelist entry.
	Comment pulumi.StringOutput `pulumi:"comment"`
	// Whitelisted IP address. Mutually exclusive with `awsSecurityGroup` and `cidrBlock`.
	IpAddress pulumi.StringOutput `pulumi:"ipAddress"`
	// The ID of the project in which to add the whitelist entry.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
}

// NewProjectIpWhitelist registers a new resource with the given unique name, arguments, and options.
func NewProjectIpWhitelist(ctx *pulumi.Context,
	name string, args *ProjectIpWhitelistArgs, opts ...pulumi.ResourceOption) (*ProjectIpWhitelist, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &ProjectIpWhitelistArgs{}
	}
	var resource ProjectIpWhitelist
	err := ctx.RegisterResource("mongodbatlas:index/projectIpWhitelist:ProjectIpWhitelist", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetProjectIpWhitelist gets an existing ProjectIpWhitelist resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProjectIpWhitelist(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ProjectIpWhitelistState, opts ...pulumi.ResourceOption) (*ProjectIpWhitelist, error) {
	var resource ProjectIpWhitelist
	err := ctx.ReadResource("mongodbatlas:index/projectIpWhitelist:ProjectIpWhitelist", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ProjectIpWhitelist resources.
type projectIpWhitelistState struct {
	// ID of the whitelisted AWS security group. Mutually exclusive with `cidrBlock` and `ipAddress`.
	AwsSecurityGroup *string `pulumi:"awsSecurityGroup"`
	// Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with `awsSecurityGroup` and `ipAddress`.
	CidrBlock *string `pulumi:"cidrBlock"`
	// Comment to add to the whitelist entry.
	Comment *string `pulumi:"comment"`
	// Whitelisted IP address. Mutually exclusive with `awsSecurityGroup` and `cidrBlock`.
	IpAddress *string `pulumi:"ipAddress"`
	// The ID of the project in which to add the whitelist entry.
	ProjectId *string `pulumi:"projectId"`
}

type ProjectIpWhitelistState struct {
	// ID of the whitelisted AWS security group. Mutually exclusive with `cidrBlock` and `ipAddress`.
	AwsSecurityGroup pulumi.StringPtrInput
	// Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with `awsSecurityGroup` and `ipAddress`.
	CidrBlock pulumi.StringPtrInput
	// Comment to add to the whitelist entry.
	Comment pulumi.StringPtrInput
	// Whitelisted IP address. Mutually exclusive with `awsSecurityGroup` and `cidrBlock`.
	IpAddress pulumi.StringPtrInput
	// The ID of the project in which to add the whitelist entry.
	ProjectId pulumi.StringPtrInput
}

func (ProjectIpWhitelistState) ElementType() reflect.Type {
	return reflect.TypeOf((*projectIpWhitelistState)(nil)).Elem()
}

type projectIpWhitelistArgs struct {
	// ID of the whitelisted AWS security group. Mutually exclusive with `cidrBlock` and `ipAddress`.
	AwsSecurityGroup *string `pulumi:"awsSecurityGroup"`
	// Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with `awsSecurityGroup` and `ipAddress`.
	CidrBlock *string `pulumi:"cidrBlock"`
	// Comment to add to the whitelist entry.
	Comment *string `pulumi:"comment"`
	// Whitelisted IP address. Mutually exclusive with `awsSecurityGroup` and `cidrBlock`.
	IpAddress *string `pulumi:"ipAddress"`
	// The ID of the project in which to add the whitelist entry.
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a ProjectIpWhitelist resource.
type ProjectIpWhitelistArgs struct {
	// ID of the whitelisted AWS security group. Mutually exclusive with `cidrBlock` and `ipAddress`.
	AwsSecurityGroup pulumi.StringPtrInput
	// Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with `awsSecurityGroup` and `ipAddress`.
	CidrBlock pulumi.StringPtrInput
	// Comment to add to the whitelist entry.
	Comment pulumi.StringPtrInput
	// Whitelisted IP address. Mutually exclusive with `awsSecurityGroup` and `cidrBlock`.
	IpAddress pulumi.StringPtrInput
	// The ID of the project in which to add the whitelist entry.
	ProjectId pulumi.StringInput
}

func (ProjectIpWhitelistArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*projectIpWhitelistArgs)(nil)).Elem()
}
