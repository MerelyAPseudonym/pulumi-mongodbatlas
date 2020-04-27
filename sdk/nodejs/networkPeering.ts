// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class NetworkPeering extends pulumi.CustomResource {
    /**
     * Get an existing NetworkPeering resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: NetworkPeeringState, opts?: pulumi.CustomResourceOptions): NetworkPeering {
        return new NetworkPeering(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mongodbatlas:index/networkPeering:NetworkPeering';

    /**
     * Returns true if the given object is an instance of NetworkPeering.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is NetworkPeering {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === NetworkPeering.__pulumiType;
    }

    /**
     * Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
     */
    public readonly accepterRegionName!: pulumi.Output<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    public readonly atlasCidrBlock!: pulumi.Output<string>;
    /**
     * The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
     */
    public readonly atlasGcpProjectId!: pulumi.Output<string>;
    public /*out*/ readonly atlasId!: pulumi.Output<string>;
    /**
     * The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
     */
    public readonly atlasVpcName!: pulumi.Output<string>;
    /**
     * Account ID of the owner of the peer VPC.
     */
    public readonly awsAccountId!: pulumi.Output<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    public readonly azureDirectoryId!: pulumi.Output<string>;
    /**
     * Unique identifer of the Azure subscription in which the VNet resides.
     */
    public readonly azureSubscriptionId!: pulumi.Output<string>;
    /**
     * Unique identifier for the peering connection.
     */
    public /*out*/ readonly connectionId!: pulumi.Output<string>;
    /**
     * Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
     */
    public readonly containerId!: pulumi.Output<string>;
    /**
     * When `"status" : "FAILED"`, Atlas provides a description of the error.
     */
    public /*out*/ readonly errorMessage!: pulumi.Output<string>;
    /**
     * Description of the Atlas error when `status` is `Failed`, Otherwise, Atlas returns `null`.
     */
    public /*out*/ readonly errorState!: pulumi.Output<string>;
    /**
     * Error state, if any. The VPC peering connection error state value can be one of the following: `REJECTED`, `EXPIRED`, `INVALID_ARGUMENT`.
     */
    public /*out*/ readonly errorStateName!: pulumi.Output<string>;
    /**
     * GCP project ID of the owner of the network peer.
     */
    public readonly gcpProjectId!: pulumi.Output<string>;
    /**
     * Name of the network peer to which Atlas connects.
     */
    public readonly networkName!: pulumi.Output<string>;
    /**
     * The Network Peering Container ID.
     */
    public /*out*/ readonly peerId!: pulumi.Output<string>;
    /**
     * The unique ID for the project to create the database user.
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
     */
    public readonly providerName!: pulumi.Output<string>;
    /**
     * Name of your Azure resource group.
     */
    public readonly resourceGroupName!: pulumi.Output<string>;
    /**
     * Peer VPC CIDR block or subnet.
     */
    public readonly routeTableCidrBlock!: pulumi.Output<string>;
    /**
     * (Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: `ADDING_PEER`, `AVAILABLE`, `FAILED`, `DELETING` GCP Only:  `WAITING_FOR_USER`.
     */
    public /*out*/ readonly status!: pulumi.Output<string>;
    /**
     * (AWS Only) The VPC peering connection status value can be one of the following: `INITIATING`, `PENDING_ACCEPTANCE`, `FAILED`, `FINALIZING`, `AVAILABLE`, `TERMINATING`.
     */
    public /*out*/ readonly statusName!: pulumi.Output<string>;
    /**
     * Name of your Azure VNet.
     */
    public readonly vnetName!: pulumi.Output<string>;
    /**
     * Unique identifier of the peer VPC.
     */
    public readonly vpcId!: pulumi.Output<string>;

    /**
     * Create a NetworkPeering resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: NetworkPeeringArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: NetworkPeeringArgs | NetworkPeeringState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as NetworkPeeringState | undefined;
            inputs["accepterRegionName"] = state ? state.accepterRegionName : undefined;
            inputs["atlasCidrBlock"] = state ? state.atlasCidrBlock : undefined;
            inputs["atlasGcpProjectId"] = state ? state.atlasGcpProjectId : undefined;
            inputs["atlasId"] = state ? state.atlasId : undefined;
            inputs["atlasVpcName"] = state ? state.atlasVpcName : undefined;
            inputs["awsAccountId"] = state ? state.awsAccountId : undefined;
            inputs["azureDirectoryId"] = state ? state.azureDirectoryId : undefined;
            inputs["azureSubscriptionId"] = state ? state.azureSubscriptionId : undefined;
            inputs["connectionId"] = state ? state.connectionId : undefined;
            inputs["containerId"] = state ? state.containerId : undefined;
            inputs["errorMessage"] = state ? state.errorMessage : undefined;
            inputs["errorState"] = state ? state.errorState : undefined;
            inputs["errorStateName"] = state ? state.errorStateName : undefined;
            inputs["gcpProjectId"] = state ? state.gcpProjectId : undefined;
            inputs["networkName"] = state ? state.networkName : undefined;
            inputs["peerId"] = state ? state.peerId : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["providerName"] = state ? state.providerName : undefined;
            inputs["resourceGroupName"] = state ? state.resourceGroupName : undefined;
            inputs["routeTableCidrBlock"] = state ? state.routeTableCidrBlock : undefined;
            inputs["status"] = state ? state.status : undefined;
            inputs["statusName"] = state ? state.statusName : undefined;
            inputs["vnetName"] = state ? state.vnetName : undefined;
            inputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as NetworkPeeringArgs | undefined;
            if (!args || args.containerId === undefined) {
                throw new Error("Missing required property 'containerId'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            if (!args || args.providerName === undefined) {
                throw new Error("Missing required property 'providerName'");
            }
            inputs["accepterRegionName"] = args ? args.accepterRegionName : undefined;
            inputs["atlasCidrBlock"] = args ? args.atlasCidrBlock : undefined;
            inputs["atlasGcpProjectId"] = args ? args.atlasGcpProjectId : undefined;
            inputs["atlasVpcName"] = args ? args.atlasVpcName : undefined;
            inputs["awsAccountId"] = args ? args.awsAccountId : undefined;
            inputs["azureDirectoryId"] = args ? args.azureDirectoryId : undefined;
            inputs["azureSubscriptionId"] = args ? args.azureSubscriptionId : undefined;
            inputs["containerId"] = args ? args.containerId : undefined;
            inputs["gcpProjectId"] = args ? args.gcpProjectId : undefined;
            inputs["networkName"] = args ? args.networkName : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["providerName"] = args ? args.providerName : undefined;
            inputs["resourceGroupName"] = args ? args.resourceGroupName : undefined;
            inputs["routeTableCidrBlock"] = args ? args.routeTableCidrBlock : undefined;
            inputs["vnetName"] = args ? args.vnetName : undefined;
            inputs["vpcId"] = args ? args.vpcId : undefined;
            inputs["atlasId"] = undefined /*out*/;
            inputs["connectionId"] = undefined /*out*/;
            inputs["errorMessage"] = undefined /*out*/;
            inputs["errorState"] = undefined /*out*/;
            inputs["errorStateName"] = undefined /*out*/;
            inputs["peerId"] = undefined /*out*/;
            inputs["status"] = undefined /*out*/;
            inputs["statusName"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(NetworkPeering.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering NetworkPeering resources.
 */
export interface NetworkPeeringState {
    /**
     * Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
     */
    readonly accepterRegionName?: pulumi.Input<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    readonly atlasCidrBlock?: pulumi.Input<string>;
    /**
     * The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
     */
    readonly atlasGcpProjectId?: pulumi.Input<string>;
    readonly atlasId?: pulumi.Input<string>;
    /**
     * The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
     */
    readonly atlasVpcName?: pulumi.Input<string>;
    /**
     * Account ID of the owner of the peer VPC.
     */
    readonly awsAccountId?: pulumi.Input<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    readonly azureDirectoryId?: pulumi.Input<string>;
    /**
     * Unique identifer of the Azure subscription in which the VNet resides.
     */
    readonly azureSubscriptionId?: pulumi.Input<string>;
    /**
     * Unique identifier for the peering connection.
     */
    readonly connectionId?: pulumi.Input<string>;
    /**
     * Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
     */
    readonly containerId?: pulumi.Input<string>;
    /**
     * When `"status" : "FAILED"`, Atlas provides a description of the error.
     */
    readonly errorMessage?: pulumi.Input<string>;
    /**
     * Description of the Atlas error when `status` is `Failed`, Otherwise, Atlas returns `null`.
     */
    readonly errorState?: pulumi.Input<string>;
    /**
     * Error state, if any. The VPC peering connection error state value can be one of the following: `REJECTED`, `EXPIRED`, `INVALID_ARGUMENT`.
     */
    readonly errorStateName?: pulumi.Input<string>;
    /**
     * GCP project ID of the owner of the network peer.
     */
    readonly gcpProjectId?: pulumi.Input<string>;
    /**
     * Name of the network peer to which Atlas connects.
     */
    readonly networkName?: pulumi.Input<string>;
    /**
     * The Network Peering Container ID.
     */
    readonly peerId?: pulumi.Input<string>;
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
     */
    readonly providerName?: pulumi.Input<string>;
    /**
     * Name of your Azure resource group.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Peer VPC CIDR block or subnet.
     */
    readonly routeTableCidrBlock?: pulumi.Input<string>;
    /**
     * (Azure/GCP Only) Status of the Atlas network peering connection.  Azure/GCP: `ADDING_PEER`, `AVAILABLE`, `FAILED`, `DELETING` GCP Only:  `WAITING_FOR_USER`.
     */
    readonly status?: pulumi.Input<string>;
    /**
     * (AWS Only) The VPC peering connection status value can be one of the following: `INITIATING`, `PENDING_ACCEPTANCE`, `FAILED`, `FINALIZING`, `AVAILABLE`, `TERMINATING`.
     */
    readonly statusName?: pulumi.Input<string>;
    /**
     * Name of your Azure VNet.
     */
    readonly vnetName?: pulumi.Input<string>;
    /**
     * Unique identifier of the peer VPC.
     */
    readonly vpcId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a NetworkPeering resource.
 */
export interface NetworkPeeringArgs {
    /**
     * Specifies the region where the peer VPC resides. For complete lists of supported regions, see [Amazon Web Services](https://docs.atlas.mongodb.com/reference/amazon-aws/).
     */
    readonly accepterRegionName?: pulumi.Input<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    readonly atlasCidrBlock?: pulumi.Input<string>;
    /**
     * The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.
     */
    readonly atlasGcpProjectId?: pulumi.Input<string>;
    /**
     * The Atlas VPC Name is used by your atlas clister that it is need to set up the reciprocal connection.
     */
    readonly atlasVpcName?: pulumi.Input<string>;
    /**
     * Account ID of the owner of the peer VPC.
     */
    readonly awsAccountId?: pulumi.Input<string>;
    /**
     * Unique identifier for an Azure AD directory.
     */
    readonly azureDirectoryId?: pulumi.Input<string>;
    /**
     * Unique identifer of the Azure subscription in which the VNet resides.
     */
    readonly azureSubscriptionId?: pulumi.Input<string>;
    /**
     * Unique identifier of the Atlas VPC container for the region. You can create an Atlas VPC container using the Create Container endpoint. You cannot create more than one container per region. To retrieve a list of container IDs, use the Get list of VPC containers endpoint.
     */
    readonly containerId: pulumi.Input<string>;
    /**
     * GCP project ID of the owner of the network peer.
     */
    readonly gcpProjectId?: pulumi.Input<string>;
    /**
     * Name of the network peer to which Atlas connects.
     */
    readonly networkName?: pulumi.Input<string>;
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Cloud provider for this VPC peering connection. (Possible Values `AWS`, `AZURE`, `GCP`).
     */
    readonly providerName: pulumi.Input<string>;
    /**
     * Name of your Azure resource group.
     */
    readonly resourceGroupName?: pulumi.Input<string>;
    /**
     * Peer VPC CIDR block or subnet.
     */
    readonly routeTableCidrBlock?: pulumi.Input<string>;
    /**
     * Name of your Azure VNet.
     */
    readonly vnetName?: pulumi.Input<string>;
    /**
     * Unique identifier of the peer VPC.
     */
    readonly vpcId?: pulumi.Input<string>;
}
