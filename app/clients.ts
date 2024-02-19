import { Path } from "./types";
import createClient from "openapi-fetch";

export const backendClient = createClient<Path>({
  baseUrl: `${process.env.BACKEND_HOST}`,
});

export const frontendClient = createClient<Path>();