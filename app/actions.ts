"use server";
import { RedirectType, redirect } from "next/navigation";
import { backendClient } from "./clients";
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
