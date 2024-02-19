import {
  S3Client,
  ListBucketsCommand,
  GetObjectCommand,
} from "@aws-sdk/client-s3";
import { NextApiHandler, NextApiRequest } from "next";
import { NextRequest } from "next/server";

export const GET = async (request: NextRequest) => {
  const searchParams = request.nextUrl.searchParams;
  const fileName = searchParams.get("fileName") as string;
  const s3 = new S3Client({
    endpoint: process.env.BUCKET_URL,
    credentials: {
      accessKeyId: process.env.BUCKET_ACCESS_KEY_ID as string,
      secretAccessKey: process.env.BUCKET_SECRET_ACCESS_KEY as string,
    },
  });
  const bucketName = "a-to-p";

  try {
    const file = await s3.send(
      new GetObjectCommand({
        Bucket: bucketName,
        Key: fileName,
      })
    );
    const response = new Response(file.Body?.transformToWebStream());
    response.headers.set("Content-Type", file.ContentType as string);
    response.headers.set(
      "Content-Disposition",
      `attachment; filename=${fileName}`
    );
    return response;
  } catch (error) {
    console.error("Failed to download file:", error);
  }
};
