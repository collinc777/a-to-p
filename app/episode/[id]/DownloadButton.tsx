"use client";
import { Button } from "@/components/ui/button";
import Link from "next/link";
import React from "react";

export default function DownloadButton({ url }: { url: string }) {
  const episodeId = url.split("/").pop();
  return (
    <Button asChild>
      <a href={`/episode_audio/${episodeId}`} download={"file"}>
        Download
      </a>
    </Button>
  );
}
