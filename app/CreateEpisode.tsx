"use client";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FormButton } from "./FormButton";
import { createEpisode } from "./actions";
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select";
import { ResultOf, graphql, readFragment } from "./graphql";
import { useSuspenseQuery } from "@apollo/experimental-nextjs-app-support/ssr";
import { usePostHog } from "posthog-js/react";

const EpisodeFormatChoiceFragment = graphql(`
  fragment EpisodeFormatChoice on EpisodeFormatChoice {
    value
    displayName
    isReady
  }
`);

const EpisodeFormatChoicesQuery = graphql(
  `
    query EpisodeFormatChoicesQuery {
      episodeFormatChoices {
        ...EpisodeFormatChoice
      }
    }
  `,
  [EpisodeFormatChoiceFragment]
);

export function CreateEpisode() {
  const { data } = useSuspenseQuery(EpisodeFormatChoicesQuery);
  const ph = usePostHog();
  const episodeFormatChoices = readFragment(
    EpisodeFormatChoiceFragment,
    data?.episodeFormatChoices
  );
  return (
    <main className="flex-1 py-8 px-4">
      <div className="container mx-auto">
        <form
          className="w-full max-w-lg mx-auto space-y-4"
          action={createEpisode}
        >
          <Label htmlFor="inputText">
            Paste an article URL or some text to generate a podcast from it
          </Label>
          <Input
            name="inputText"
            className="w-full"
            placeholder="Paste your text or URL here"
            type="text"
          />
          <Select
            name="podcastFormatSelector"
            onValueChange={(e) => {
              ph.capture("Podcast Format Selected", {
                podcastFormat: e,
              });
              const selectedFormat = episodeFormatChoices.find(
                (format) => format.value === e
              );
              if (!selectedFormat?.isReady) {
              }
            }}
          >
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Podcast Format..." />
            </SelectTrigger>
            <SelectContent>
              {episodeFormatChoices.map((format) => (
                <SelectItem
                  key={format.value}
                  value={format.value}
                  disabled={!format.isReady}
                >
                  {format.displayName}
                </SelectItem>
              ))}
              <SelectItem value="other">Other</SelectItem>
            </SelectContent>
          </Select>
          <FormButton />
        </form>
        <EpisodeFormatVoter
          formatsToVoteOn={episodeFormatChoices.filter((val) => !val.isReady)}
        />
      </div>
    </main>
  );
}

export function EpisodeFormatVoter({
  formatsToVoteOn,
}: {
  formatsToVoteOn: ResultOf<typeof EpisodeFormatChoiceFragment>[];
}) {
  return (
    <div className="flex flex-col items-center space-y-4">
      <h2 className="text-2xl font-bold">Vote for the next format</h2>
      <p className="text-gray-600">
        We are constantly adding new formats to the platform. If you don&apos;t
        see the format you want, vote for it here.
      </p>
      <ul className="flex flex-col space-y-4">
        {formatsToVoteOn.map((format) => (
          <li key={format.value} className="flex items-center space-x-4">
            <span>{format.displayName}</span>
            <button
              className="text-blue-500"
              onClick={() => {
                // vote for the format
              }}
            >
              Vote
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
