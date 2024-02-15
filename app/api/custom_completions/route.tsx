import OpenAI from "openai";
import {
  AIStream,
  StreamingTextResponse,
  type AIStreamCallbacksAndOptions,
} from "ai";

export const runtime = "edge";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY!,
});

export async function POST(req: Request) {
  // Extract the `prompt` from the body of the request
  const { prompt: text } = await req.json();
  let payload = {};
  if (text.startsWith("http")) {
    payload = { article_url: text };
  } else {
    payload = { article_text: text };
  }

  // Request the OpenAI API for the response based on the prompt
  console.log("printed")
  console.log({env: process.env?.BACKEND_HOST})
  const response = await fetch(
    `${process.env.BACKEND_HOST}/api/stream_episode_create_task`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // note this has to adhere to the Openapi spec
      body: JSON.stringify(payload),
    }
  );
  const customStream = CustomStream(response);

  return new StreamingTextResponse(customStream);
}

function parseCustomStream() {
  let previous = "";
  return (data: any) => {
    previous = data;
    return previous;
  };
}

function CustomStream(
  res: Response,
  cb?: AIStreamCallbacksAndOptions
): ReadableStream {
  return AIStream(res, parseCustomStream(), cb);
}
