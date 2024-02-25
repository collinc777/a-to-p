"use client";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { FormButton } from "./FormButton";
import { createEpisode } from "./actions";
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
          <FormButton />
        </form>
      </div>
    </main>
  );
}
