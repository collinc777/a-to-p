"use client";
import { usePostHog } from "posthog-js/react";

export const AudioPlayer = ({ url }: { url: string }) => {
  const posthog = usePostHog();
  return (
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
  );
};
