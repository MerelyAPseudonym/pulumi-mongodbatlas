// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * `mongodbatlas..Auditing` provides an Auditing resource. This allows auditing to be created.
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as mongodbatlas from "@pulumi/mongodbatlas";
 * 
 * const test = new mongodbatlas.Auditing("test", {
 *     auditAuthorizationSuccess: false,
 *     auditFilter: "{ 'atype': 'authenticate', 'param': {   'user': 'auditAdmin',   'db': 'admin',   'mechanism': 'SCRAM-SHA-1' }}",
 *     enabled: true,
 *     projectId: "<project-id>",
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-mongodbatlas/blob/master/website/docs/r/auditing.html.markdown.
 */
export class Auditing extends pulumi.CustomResource {
    /**
     * Get an existing Auditing resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AuditingState, opts?: pulumi.CustomResourceOptions): Auditing {
        return new Auditing(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'mongodbatlas:index/auditing:Auditing';

    /**
     * Returns true if the given object is an instance of Auditing.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Auditing {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Auditing.__pulumiType;
    }

    /**
     * JSON-formatted audit filter used by the project
     */
    public readonly auditAuthorizationSuccess!: pulumi.Output<boolean>;
    /**
     * Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
     */
    public readonly auditFilter!: pulumi.Output<string>;
    /**
     * Denotes the configuration method for the audit filter. Possible values are: 
     * * NONE - auditing not configured for the project.
     * * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
     * * FILTER_JSON - auditing configured via Atlas custom filter or API.
     */
    public /*out*/ readonly configurationType!: pulumi.Output<string>;
    /**
     * Denotes whether or not the project associated with the {project_id} has database auditing enabled.
     */
    public readonly enabled!: pulumi.Output<boolean>;
    /**
     * The unique ID for the project to configure auditing.
     */
    public readonly projectId!: pulumi.Output<string>;

    /**
     * Create a Auditing resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AuditingArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AuditingArgs | AuditingState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AuditingState | undefined;
            inputs["auditAuthorizationSuccess"] = state ? state.auditAuthorizationSuccess : undefined;
            inputs["auditFilter"] = state ? state.auditFilter : undefined;
            inputs["configurationType"] = state ? state.configurationType : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
        } else {
            const args = argsOrState as AuditingArgs | undefined;
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["auditAuthorizationSuccess"] = args ? args.auditAuthorizationSuccess : undefined;
            inputs["auditFilter"] = args ? args.auditFilter : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["configurationType"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Auditing.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Auditing resources.
 */
export interface AuditingState {
    /**
     * JSON-formatted audit filter used by the project
     */
    readonly auditAuthorizationSuccess?: pulumi.Input<boolean>;
    /**
     * Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
     */
    readonly auditFilter?: pulumi.Input<string>;
    /**
     * Denotes the configuration method for the audit filter. Possible values are: 
     * * NONE - auditing not configured for the project.
     * * FILTER_BUILDER - auditing configured via Atlas UI filter builder.
     * * FILTER_JSON - auditing configured via Atlas custom filter or API.
     */
    readonly configurationType?: pulumi.Input<string>;
    /**
     * Denotes whether or not the project associated with the {project_id} has database auditing enabled.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The unique ID for the project to configure auditing.
     */
    readonly projectId?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Auditing resource.
 */
export interface AuditingArgs {
    /**
     * JSON-formatted audit filter used by the project
     */
    readonly auditAuthorizationSuccess?: pulumi.Input<boolean>;
    /**
     * Indicates whether the auditing system captures successful authentication attempts for audit filters using the "atype" : "authCheck" auditing event. For more information, see auditAuthorizationSuccess
     */
    readonly auditFilter?: pulumi.Input<string>;
    /**
     * Denotes whether or not the project associated with the {project_id} has database auditing enabled.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The unique ID for the project to configure auditing.
     */
    readonly projectId: pulumi.Input<string>;
}
