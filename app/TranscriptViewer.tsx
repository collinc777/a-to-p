import { Key } from "react";

export default function TranscriptViewer({
  transcriptJsonString,
}: {
  transcriptJsonString: string;
}) {
  // check to see if trasncript is parseable
  if (!transcriptJsonString) {
    return null;
  }
  const transcript = JSON.parse(transcriptJsonString);
  const transcriptLines = transcript?.transcript?.transcript_lines;
  return (
    <div className="space-y-3">
      {transcriptLines?.map((line: any, idx: Key | null | undefined) => {
        const speaker = line.speaker;
        const text = line.text;
        return (
          <div className="flex space-x-3" key={idx}>
            <SpeakerBadge speaker={speaker} />
            <div>{text}</div>
          </div>
        );
      })}
    </div>
  );
}

export const SpeakerBadge = ({ speaker }: { speaker: string }) => {
  const className = () => {
    if (speaker === "Jake") {
      return "w-12 rounded-md bg-yellow-50 px-2 py-1 text-xs font-medium text-yellow-800 ring-1 ring-inset ring-yellow-600/20";
    } else {
      return "w-12 rounded-md bg-purple-50 px-2 py-1 text-xs font-medium text-purple-700 ring-1 ring-inset ring-purple-700/10";
    }
  };
  return <span className={className()}>{speaker}</span>;
};
