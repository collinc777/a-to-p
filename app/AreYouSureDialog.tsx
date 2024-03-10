import { Button } from "@/components/ui/button";
import {
  DialogClose,
  DialogContent,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/dialog";

export function AreYouSureDialog({
  onSuccess,
  idx,
}: {
  idx: number;
  onSuccess: (id: number) => Promise<void>;
}) {
  return (
    <DialogContent className="sm:max-w-[425px]">
      <DialogHeader>
        <DialogTitle>Are You Sure?</DialogTitle>
      </DialogHeader>
      <div className="flex flex-row justify-between">
        <DialogClose asChild>
          <Button
            variant={"destructive"}
            onClick={async () => {
              console.log("does this work");
              await onSuccess(idx);
            }}
          >
            Yes
          </Button>
        </DialogClose>
        <DialogClose asChild>
          <Button>Cancel</Button>
        </DialogClose>
      </div>
    </DialogContent>
  );
}
