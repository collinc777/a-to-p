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
  const { prompt } = await req.json();

  // Request the OpenAI API for the response based on the prompt
  const response = await fetch("http://127.0.0.1:8000/api/test_stream", {
    method: "POST",
  });
  const customStream = CustomStream(response);

  return new StreamingTextResponse(customStream);
}

function parseCustomStream() {
  let previous = "";
  return (data: any) => {
    console.log({ data });
    previous = data;
    return previous;
  };
}

export function CustomStream(
  res: Response,
  cb?: AIStreamCallbacksAndOptions
): ReadableStream {
  return AIStream(res, parseCustomStream(), cb);
}
