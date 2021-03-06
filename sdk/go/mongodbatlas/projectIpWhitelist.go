// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `ProjectIpWhitelist` provides an IP Whitelist entry resource. The whitelist grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.
//
// > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
//
// > **IMPORTANT:**
// When you remove an entry from the whitelist, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.
//
// ## Example Usage
// ### Using CIDR Block
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
// 		_, err := mongodbatlas.NewProjectIpWhitelist(ctx, "test", &mongodbatlas.ProjectIpWhitelistArgs{
// 			CidrBlock: pulumi.String("1.2.3.4/32"),
// 			Comment:   pulumi.String("cidr block for tf acc testing"),
// 			ProjectId: pulumi.String("<PROJECT-ID>"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Using IP Address
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
// 		_, err := mongodbatlas.NewProjectIpWhitelist(ctx, "test", &mongodbatlas.ProjectIpWhitelistArgs{
// 			Comment:   pulumi.String("ip address for tf acc testing"),
// 			IpAddress: pulumi.String("2.3.4.5"),
// 			ProjectId: pulumi.String("<PROJECT-ID>"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Using an AWS Security Group
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
// 		testNetworkContainer, err := mongodbatlas.NewNetworkContainer(ctx, "testNetworkContainer", &mongodbatlas.NetworkContainerArgs{
// 			ProjectId:      pulumi.String("<PROJECT-ID>"),
// 			AtlasCidrBlock: pulumi.String("192.168.208.0/21"),
// 			ProviderName:   pulumi.String("AWS"),
// 			RegionName:     pulumi.String("US_EAST_1"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mongodbatlas.NewNetworkPeering(ctx, "testNetworkPeering", &mongodbatlas.NetworkPeeringArgs{
// 			ProjectId:           pulumi.String("<PROJECT-ID>"),
// 			ContainerId:         testNetworkContainer.ContainerId,
// 			AccepterRegionName:  pulumi.String("us-east-1"),
// 			ProviderName:        pulumi.String("AWS"),
// 			RouteTableCidrBlock: pulumi.String("172.31.0.0/16"),
// 			VpcId:               pulumi.String("vpc-0d93d6f69f1578bd8"),
// 			AwsAccountId:        pulumi.String("232589400519"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = mongodbatlas.NewProjectIpWhitelist(ctx, "testProjectIpWhitelist", &mongodbatlas.ProjectIpWhitelistArgs{
// 			ProjectId:        pulumi.String("<PROJECT-ID>"),
// 			AwsSecurityGroup: pulumi.String("sg-0026348ec11780bd1"),
// 			Comment:          pulumi.String("TestAcc for awsSecurityGroup"),
// 		}, pulumi.DependsOn([]pulumi.Resource{
// 			"mongodbatlas_network_peering.test",
// 		}))
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// > **IMPORTANT:** In order to use AWS Security Group(s) VPC Peering must be enabled like above example.
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
