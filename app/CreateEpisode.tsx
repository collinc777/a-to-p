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

const podcastFormats = [
  { displayValue: "Monologue (Solo)", value: "monologue" },
  { displayValue: "Co-hosted (Dialogue)", value: "dialogue" },
  { displayValue: "Interview", value: "interview" },
  { displayValue: "Panel", value: "panel" },
  { displayValue: "Narrative", value: "narrative" },
  { displayValue: "Other", value: "other" },
];

export function CreateEpisode() {
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
          <Select>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Podcast Format..." />
            </SelectTrigger>
            <SelectContent>
              {podcastFormats.map((format) => (
                <SelectItem key={format.value} value={format.value}>
                  {format.displayValue}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          <FormButton />
        </form>
      </div>
    </main>
  );
}
