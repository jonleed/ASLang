/** @type {import('next').NextConfig} */
const isGitHubPagesBuild = process.env.GITHUB_ACTIONS === "true";

const nextConfig = {
    output: isGitHubPagesBuild ? "export" : undefined,
    basePath: isGitHubPagesBuild ? "/ASLang" : undefined,
    images: {
      unoptimized: isGitHubPagesBuild,
    },
  };

module.exports = isGitHubPagesBuild
  ? nextConfig
  : {
      ...nextConfig,
      async rewrites() {
        return [
          {
            source: "/hello/:path*",
            destination: "http://localhost:5000/hello/:path*",
          },
        ];
      },
    };
