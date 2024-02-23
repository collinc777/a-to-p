"use server";
import { RedirectType, redirect } from "next/navigation";
import { backendClient } from "./clients";
import { UpdateEpisodeInput } from "./types";
export async function createEpisode(formData: FormData) {
  const text = formData.get("inputText") as string;
  let payload = {};
  if (text.startsWith("http")) {
    payload = { article_url: text };
  } else {
    payload = { article_text: text };
  }
  const response = await backendClient.POST("/api/episode_create_task", {
    body: payload,
  });
  const id = response.data?.id
  if (id) {
    redirect(`/episode/${id}`, RedirectType.push)
  }
}

export async function updateEpisode(id: string, payload: UpdateEpisodeInput) {
  console.log("updateEpisode", id, payload);
  const result = await backendClient.PATCH(`/api/episode/{id}`, {
    params: {
      path: {
        id,
      },
    },
    body: payload,
  });
  console.log("updateEpisode result", result.error);
}