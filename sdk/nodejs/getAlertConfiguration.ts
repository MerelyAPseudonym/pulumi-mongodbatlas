// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * `mongodbatlas..AlertConfiguration` describes an Alert Configuration.
 *
 * > **NOTE:** Groups and projects are synonymous terms. You may find **group_id** in the official documentation.
 *
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 *
 * const testMongodbatlasAlertConfiguration = new mongodbatlas.AlertConfiguration("test", {
 *     enabled: true,
 *     eventType: "OUTSIDE_METRIC_THRESHOLD",
 *     matchers: [{
 *         fieldName: "HOSTNAME_AND_PORT",
 *         operator: "EQUALS",
 *         value: "SECONDARY",
 *     }],
 *     metricThreshold: {
 *         metric_name: "ASSERT_REGULAR",
 *         mode: "AVERAGE",
 *         operator: "LESS_THAN",
 *         threshold: 99,
 *         units: "RAW",
 *     },
 *     notifications: [{
 *         delayMin: 0,
 *         emailEnabled: true,
 *         intervalMin: 5,
 *         smsEnabled: false,
 *         typeName: "GROUP",
 *     }],
 *     projectId: "<PROJECT-ID>",
 * });
 * const testAlertConfiguration = pulumi.all([testMongodbatlasAlertConfiguration.alertConfigurationId, testMongodbatlasAlertConfiguration.projectId]).apply(([alertConfigurationId, projectId]) => mongodbatlas.getAlertConfiguration({
 *     alertConfigurationId: alertConfigurationId,
 *     projectId: projectId,
 * }, { async: true }));
 * ```
 */
export function getAlertConfiguration(args: GetAlertConfigurationArgs, opts?: pulumi.InvokeOptions): Promise<GetAlertConfigurationResult> {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("mongodbatlas:index/getAlertConfiguration:getAlertConfiguration", {
        "alertConfigurationId": args.alertConfigurationId,
        "projectId": args.projectId,
    }, opts);
}

/**
 * A collection of arguments for invoking getAlertConfiguration.
 */
export interface GetAlertConfigurationArgs {
    /**
     * Unique identifier for the alert configuration.
     */
    readonly alertConfigurationId: string;
    /**
     * The ID of the project where the alert configuration will create.
     */
    readonly projectId: string;
}

/**
 * A collection of values returned by getAlertConfiguration.
 */
export interface GetAlertConfigurationResult {
    readonly alertConfigurationId: string;
    /**
     * Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.
     */
    readonly created: string;
    /**
     * If set to true, the alert configuration is enabled. If enabled is not exported it is set to false.
     */
    readonly enabled: boolean;
    /**
     * The type of event that will trigger an alert.
     * Alert type. Possible values:
     * - Host
     * - `OUTSIDE_METRIC_THRESHOLD`
     * - `HOST_RESTARTED`
     * - `HOST_UPGRADED`
     * - `HOST_NOW_SECONDARY`
     * - `HOST_NOW_PRIMARY`
     * - Replica set
     * - `NO_PRIMARY`
     * - `TOO_MANY_ELECTIONS`
     * Sharded cluster
     * - `CLUSTER_MONGOS_IS_MISSING`
     * - `User`
     * - `JOINED_GROUP`
     * - `REMOVED_FROM_GROUP`
     * - `USER_ROLES_CHANGED_AUDIT`
     * - Project
     * - `USERS_AWAITING_APPROVAL`
     * - `USERS_WITHOUT_MULTI_FACTOR_AUTH`
     * - `GROUP_CREATED`
     * - Team
     * - `JOINED_TEAM`
     * - `REMOVED_FROM_TEAM`
     * - Organization
     * - `INVITED_TO_ORG`
     * - `JOINED_ORG`
     * - Data Explorer
     * - `DATA_EXPLORER`
     * - `DATA_EXPLORER_CRUD`
     * - Billing
     * - `CREDIT_CARD_ABOUT_TO_EXPIRE`
     * - `CHARGE_SUCCEEDED`
     * - `INVOICE_CLOSED`
     */
    readonly eventType: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly matchers: outputs.GetAlertConfigurationMatcher[];
    readonly metricThreshold: outputs.GetAlertConfigurationMetricThreshold;
    readonly notifications: outputs.GetAlertConfigurationNotification[];
    readonly projectId: string;
    /**
     * Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.
     */
    readonly updated: string;
}
