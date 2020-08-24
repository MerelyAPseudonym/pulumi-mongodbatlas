// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

let __config = new pulumi.Config("mongodbatlas");

/**
 * MongoDB Atlas Programmatic Private Key
 */
export let privateKey: string | undefined = __config.get("privateKey") || utilities.getEnv("MONGODB_ATLAS_PRIVATE_KEY");
/**
 * MongoDB Atlas Programmatic Public Key
 */
export let publicKey: string | undefined = __config.get("publicKey") || utilities.getEnv("MONGODB_ATLAS_PUBLIC_KEY");
