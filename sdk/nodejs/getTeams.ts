// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getTeams(args: GetTeamsArgs, opts?: pulumi.InvokeOptions): Promise<GetTeamsResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("mongodbatlas:index/getTeams:getTeams", {
        "orgId": args.orgId,
        "teamId": args.teamId,
    }, opts);
}

/**
 * A collection of arguments for invoking getTeams.
 */
export interface GetTeamsArgs {
    readonly orgId: string;
    readonly teamId: string;
}

/**
 * A collection of values returned by getTeams.
 */
export interface GetTeamsResult {
    readonly name: string;
    readonly orgId: string;
    readonly teamId: string;
    readonly usernames: string[];
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
