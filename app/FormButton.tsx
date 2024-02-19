"use client";
import { Button } from "@/components/ui/button";
// @ts-ignore
import { useFormStatus } from "react-dom";

export const FormButton = () => {
  const { pending } = useFormStatus();
  return (
    <Button className="w-full" type="submit" disabled={pending}>
      Generate Podcast Episode
    </Button>
  );
};
