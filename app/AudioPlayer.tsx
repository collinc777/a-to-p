"use client";
import { usePostHog } from "posthog-js/react";
import DownloadButton from "./episode/[id]/DownloadButton";

export const AudioPlayer = ({ url }: { url: string }) => {
  const posthog = usePostHog();
  return (
    <div className="flex flex-row items-center space-x-3 flex-wrap space-y-3">
      <div>
        <audio
          autoFocus
          controls
          src={url}
          onPlay={() => {
            posthog.capture("played");
          }}
        />
      </div>
      <DownloadButton url={url} />
    </div>
  );
};
