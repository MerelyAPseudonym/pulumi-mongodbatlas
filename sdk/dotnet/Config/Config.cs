// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;

namespace Pulumi.Mongodbatlas
{
    public static class Config
    {
        private static readonly Pulumi.Config __config = new Pulumi.Config("mongodbatlas");
        /// <summary>
        /// MongoDB Atlas Programmatic Private Key
        /// </summary>
        public static string? PrivateKey { get; set; } = __config.Get("privateKey") ?? Utilities.GetEnv("MONGODB_ATLAS_PRIVATE_KEY");

        /// <summary>
        /// MongoDB Atlas Programmatic Public Key
        /// </summary>
        public static string? PublicKey { get; set; } = __config.Get("publicKey") ?? Utilities.GetEnv("MONGODB_ATLAS_PUBLIC_KEY");

    }
}
