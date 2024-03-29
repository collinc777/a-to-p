import "./globals.css";
import { Inter } from "next/font/google";
import { PHProvider } from "./providers";
import dynamic from "next/dynamic";
import { ApolloWrapper } from "./ApolloWrapper";
import Link from "next/link";
import { buttonVariants } from "@/components/ui/button";
import { Toaster } from "@/components/ui/sonner";

const inter = Inter({ subsets: ["latin"] });
const PostHogPageView = dynamic(() => import("./PostHogPageView"), {
  ssr: false,
});

export const metadata = {
  title: "Article to Podcast",
  description: "Convert any article to a podcast episode",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <PHProvider>
        <ApolloWrapper>
          <body className={inter.className}>
            <PostHogPageView />
            <div className="flex flex-col min-h-screen bg-primary text-primary-foreground">
              <header className="w-full py-6 px-4 border-b ">
                <div className="container mx-auto flex items-center justify-between">
                  <Link
                    href={"/"}
                    className={buttonVariants({ variant: "link" })}
                  >
                    <h1 className="text-2xl font-bold text-gray-900 dark:text-gray-100">
                      Article to Podcast
                    </h1>
                  </Link>
                </div>
              </header>
              {children}
            </div>
            <Toaster />
          </body>
        </ApolloWrapper>
      </PHProvider>
    </html>
  );
}
