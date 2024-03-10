"use client";
import { Button } from "@/components/ui/button";
import React from "react";

export default function DownloadButton({ url }: { url: string }) {
  return (
    <a href={url} download={"file"}>
      Download
    </a>
  );
}
