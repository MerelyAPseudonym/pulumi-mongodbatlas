// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package mongodbatlas

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// `X509AuthenticationDatabaseUser` describe a X509 Authentication Database User. This represents a X509 Authentication Database User.
//
// > **NOTE:** Groups and projects are synonymous terms. You may find groupId in the official documentation.
//
// ## Example Usage
//
// ### S
// ### Example Usage: Generate an Atlas-managed X.509 certificate for a MongoDB user
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		user, err := mongodbatlas.NewDatabaseUser(ctx, "user", &mongodbatlas.DatabaseUserArgs{
// 			DatabaseName: pulumi.String(fmt.Sprintf("%v%v", "$", "external")),
// 			Labels: mongodbatlas.DatabaseUserLabelArray{
// 				&mongodbatlas.DatabaseUserLabelArgs{
// 					Key:   pulumi.String("My Key"),
// 					Value: pulumi.String("My Value"),
// 				},
// 			},
// 			ProjectId: pulumi.String("<PROJECT-ID>"),
// 			Roles: mongodbatlas.DatabaseUserRoleArray{
// 				&mongodbatlas.DatabaseUserRoleArgs{
// 					DatabaseName: pulumi.String("admin"),
// 					RoleName:     pulumi.String("atlasAdmin"),
// 				},
// 			},
// 			Username: pulumi.String("myUsername"),
// 			X509Type: pulumi.String("MANAGED"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		testX509AuthenticationDatabaseUser, err := mongodbatlas.NewX509AuthenticationDatabaseUser(ctx, "testX509AuthenticationDatabaseUser", &mongodbatlas.X509AuthenticationDatabaseUserArgs{
// 			MonthsUntilExpiration: pulumi.Int(2),
// 			ProjectId:             user.ProjectId,
// 			Username:              user.Username,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Example Usage: Save a customer-managed X.509 configuration for an Atlas project
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-mongodbatlas/sdk/go/mongodbatlas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		testX509AuthenticationDatabaseUser, err := mongodbatlas.NewX509AuthenticationDatabaseUser(ctx, "testX509AuthenticationDatabaseUser", &mongodbatlas.X509AuthenticationDatabaseUserArgs{
// 			CustomerX509Cas: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v%v", "  -----BEGIN CERTIFICATE-----\n", "  MIICmTCCAgICCQDZnHzklxsT9TANBgkqhkiG9w0BAQsFADCBkDELMAkGA1UEBhMC\n", "  VVMxDjAMBgNVBAgMBVRleGFzMQ8wDQYDVQQHDAZBdXN0aW4xETAPBgNVBAoMCHRl\n", "  c3QuY29tMQ0wCwYDVQQLDARUZXN0MREwDwYDVQQDDAh0ZXN0LmNvbTErMCkGCSqG\n", "  SIb3DQEJARYcbWVsaXNzYS5wbHVua2V0dEBtb25nb2RiLmNvbTAeFw0yMDAyMDQy\n", "  MDQ2MDFaFw0yMTAyMDMyMDQ2MDFaMIGQMQswCQYDVQQGEwJVUzEOMAwGA1UECAwF\n", "  VGV4YXMxDzANBgNVBAcMBkF1c3RpbjERMA8GA1UECgwIdGVzdC5jb20xDTALBgNV\n", "  BAsMBFRlc3QxETAPBgNVBAMMCHRlc3QuY29tMSswKQYJKoZIhvcNAQkBFhxtZWxp\n", "  c3NhLnBsdW5rZXR0QG1vbmdvZGIuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB\n", "  iQKBgQCf1LRqr1zftzdYx2Aj9G76tb0noMPtj6faGLlPji1+m6Rn7RWD9L0ntWAr\n", "  cURxvypa9jZ9MXFzDtLevvd3tHEmfrUT3ukNDX6+Jtc4kWm+Dh2A70Pd+deKZ2/O\n", "  Fh8audEKAESGXnTbeJCeQa1XKlIkjqQHBNwES5h1b9vJtFoLJwIDAQABMA0GCSqG\n", "  SIb3DQEBCwUAA4GBADMUncjEPV/MiZUcVNGmktP6BPmEqMXQWUDpdGW2+Tg2JtUA\n", "  7MMILtepBkFzLO+GlpZxeAlXO0wxiNgEmCRONgh4+t2w3e7a8GFijYQ99FHrAC5A\n", "  iul59bdl18gVqXia1Yeq/iK7Ohfy/Jwd7Hsm530elwkM/ZEkYDjBlZSXYdyz\n", "  -----END CERTIFICATE-----\"\n", "\n")),
// 			ProjectId:       pulumi.String("<PROJECT-ID>"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func Get509AuthenticationDatabaseUser(ctx *pulumi.Context, args *Get509AuthenticationDatabaseUserArgs, opts ...pulumi.InvokeOption) (*Get509AuthenticationDatabaseUserResult, error) {
	var rv Get509AuthenticationDatabaseUserResult
	err := ctx.Invoke("mongodbatlas:index/get509AuthenticationDatabaseUser:get509AuthenticationDatabaseUser", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking get509AuthenticationDatabaseUser.
type Get509AuthenticationDatabaseUserArgs struct {
	// Identifier for the Atlas project associated with the X.509 configuration.
	ProjectId string `pulumi:"projectId"`
	// Username of the database user to create a certificate for.
	Username *string `pulumi:"username"`
}

// A collection of values returned by get509AuthenticationDatabaseUser.
type Get509AuthenticationDatabaseUserResult struct {
	// Array of objects where each details one unexpired database user certificate.
	Certificates    []Get509AuthenticationDatabaseUserCertificate `pulumi:"certificates"`
	CustomerX509Cas string                                        `pulumi:"customerX509Cas"`
	// The provider-assigned unique ID for this managed resource.
	Id        string  `pulumi:"id"`
	ProjectId string  `pulumi:"projectId"`
	Username  *string `pulumi:"username"`
}
