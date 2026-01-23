"use client";

import Button from "@/components/ui/Button";

export default function Login({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      <div
        className="absolute inset-0 bg-black/60 backdrop-blur-sm"
        onClick={onClose}
      />

      <div
        className="relative z-50 w-[90%] max-w-md rounded-xl p-8 font-sans
                   bg-white/80 backdrop-blur-xl shadow-2xl border border-white/30"
        onClick={(e) => e.stopPropagation()}
      >
        <button
          onClick={onClose}
          className="absolute top-4 right-4 text-xl font-bold text-black hover:opacity-60"
        >
          ✕
        </button>

        <h2 className="text-3xl font-extrabold text-black">Welcome Back</h2>
        <p className="text-sm text-gray-700 mt-1">
          Log in to continue your fitness journey.
        </p>

        <form className="mt-8 flex flex-col gap-4">
          <input
            type="email"
            placeholder="Enter your email"
            className="w-full rounded-md px-4 py-3
                       bg-white/70 border border-gray-300
                       text-black placeholder-gray-500
                       focus:outline-none focus:border-black"
          />

          <input
            type="password"
            placeholder="Enter your password"
            className="w-full rounded-md px-4 py-3
                       bg-white/70 border border-gray-300
                       text-black placeholder-gray-500
                       focus:outline-none focus:border-black"
          />

          <Button
            variant="tryForFree"
            size="lg"
            className="mt-2 text-black font-semibold hover:bg-black hover:text-white"
          >
            Log In
          </Button>
        </form>
      </div>
    </div>
  );
}
