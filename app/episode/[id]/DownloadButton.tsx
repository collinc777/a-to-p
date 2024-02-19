import { Button, buttonVariants } from "@/components/ui/button";
import Link from "next/link";
import React from "react";

export default function DownloadButton({ url }: { url: string }) {
  const split = url.split("/");
  const last = split[split.length - 1];
  const newurl = `/api/download_mp3?fileName=${last}`;

  return (
    <Link
      prefetch={false}
      href={newurl}
      download={true}
      className={buttonVariants({})}
    >
      Download
    </Link>
  );
}
