/** @type {import('next').NextConfig} */
const nextConfig = {
  rewrites: async () => {
    return [
      {
        source: "/episode_audio/:path*",
        destination: "https://pub-8de223ddcc7d42b1b0db7486fcb8c437.r2.dev/episode/:path*"
      },
      {
        source: "/graphql",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/graphql"
            : `${process.env.PROD_API_ENDPOINT}/graphql`,
      },
      {
        source: "/api/:path*",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://127.0.0.1:8000/api/:path*"
            : `${process.env.PROD_API_ENDPOINT}/api/:path*`,
      },
      {
        source: "/docs",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://localhost:8000/docs"
            : `${process.env.PROD_API_ENDPOINT}/api/docs`,
      },
      {
        source: "/openapi.json",
        destination:
          process.env.NODE_ENV === "development"
            ? "http://localhost:8000/openapi.json"
            : `${process.env.PROD_API_ENDPOINT}/api/openapi.json`,
      },
      {
        source: "/ingest/:path*",
        destination: "https://app.posthog.com/:path*",
      },
    ];
  },
};

module.exports = nextConfig;
