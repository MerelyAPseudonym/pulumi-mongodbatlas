// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * `mongodbatlas.CustomDbRole` describe a Custom DB Role. This represents a custom db role.
 *
 * > **NOTE:** Groups and projects are synonymous terms. You may find groupId in the official documentation.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 *
 * const testRole = new mongodbatlas.CustomDbRole("test_role", {
 *     actions: [
 *         {
 *             action: "UPDATE",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *         {
 *             action: "INSERT",
 *             resources: [{
 *                 collectionName: "",
 *                 databaseName: "anyDatabase",
 *             }],
 *         },
 *     ],
 *     projectId: "<PROJECT-ID>",
 *     roleName: "myCustomRole",
 * });
 * const test = pulumi.all([testRole.projectId, testRole.roleName]).apply(([projectId, roleName]) => mongodbatlas.getCustomDbRole({
 *     projectId: projectId,
 *     roleName: roleName,
 * }, { async: true }));
 * ```
 */
export function getCustomDbRole(args: GetCustomDbRoleArgs, opts?: pulumi.InvokeOptions): Promise<GetCustomDbRoleResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("mongodbatlas:index/getCustomDbRole:getCustomDbRole", {
        "inheritedRoles": args.inheritedRoles,
        "projectId": args.projectId,
        "roleName": args.roleName,
    }, opts);
}

/**
 * A collection of arguments for invoking getCustomDbRole.
 */
export interface GetCustomDbRoleArgs {
    readonly inheritedRoles?: inputs.GetCustomDbRoleInheritedRole[];
    /**
     * The unique ID for the project to create the database user.
     */
    readonly projectId: string;
    /**
     * Name of the custom role.
     */
    readonly roleName: string;
}

/**
 * A collection of values returned by getCustomDbRole.
 */
export interface GetCustomDbRoleResult {
    readonly actions: outputs.GetCustomDbRoleAction[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly inheritedRoles?: outputs.GetCustomDbRoleInheritedRole[];
    readonly projectId: string;
    readonly roleName: string;
}
