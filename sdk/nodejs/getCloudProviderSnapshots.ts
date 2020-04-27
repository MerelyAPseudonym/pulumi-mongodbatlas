// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * `mongodbatlas..getCloudProviderSnapshots` provides an Cloud Provider Snapshot entry datasource. Atlas Cloud Provider Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service provider.
 * 
 * > **NOTE:** Groups and projects are synonymous terms. You may find `groupId` in the official documentation.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const testMongodbatlasCloudProviderSnapshots = new mongodbatlas.CloudProviderSnapshots("test", {
 *     clusterName: "MyClusterTest",
 *     description: "SomeDescription",
 *     groupId: "5d0f1f73cf09a29120e173cf",
 *     retentionInDays: 1,
 * });
 * const testCloudProviderSnapshots = pulumi.all([testMongodbatlasCloudProviderSnapshots.clusterName, testMongodbatlasCloudProviderSnapshots.groupId]).apply(([clusterName, groupId]) => mongodbatlas.getCloudProviderSnapshots({
 *     clusterName: clusterName,
 *     groupId: groupId,
 * }, { async: true }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-mongodbatlas/blob/master/website/docs/d/cloud_provider_snapshots.html.markdown.
 */
export function getCloudProviderSnapshots(args: GetCloudProviderSnapshotsArgs, opts?: pulumi.InvokeOptions): Promise<GetCloudProviderSnapshotsResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("mongodbatlas:index/getCloudProviderSnapshots:getCloudProviderSnapshots", {
        "clusterName": args.clusterName,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getCloudProviderSnapshots.
 */
export interface GetCloudProviderSnapshotsArgs {
    /**
     * The name of the Atlas cluster that contains the snapshot you want to retrieve.
     */
    readonly clusterName: string;
    readonly projectId: string;
}

/**
 * A collection of values returned by getCloudProviderSnapshots.
 */
export interface GetCloudProviderSnapshotsResult {
    readonly clusterName: string;
    readonly projectId: string;
    /**
     * Includes cloudProviderSnapshot object for each item detailed in the results array section.
     */
    readonly results: outputs.GetCloudProviderSnapshotsResult[];
    readonly totalCount: number;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
