import "./globals.css";
import { Inter } from "next/font/google";
import { PHProvider } from "./providers";
import dynamic from "next/dynamic";

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
        <body className={inter.className}>
          <PostHogPageView />
          {children}
        </body>
      </PHProvider>
    </html>
  );
}
