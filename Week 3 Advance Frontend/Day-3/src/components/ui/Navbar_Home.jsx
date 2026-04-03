"use client";

import { useState } from "react";
import Button from "./Button";
import Image from "next/image";
import LoginModal from "@/components/ui/Login";

export default function NavbarHome() {
  const [loginOpen, setLoginOpen] = useState(false);

  return (
    <>
      <header
        className="
        fixed top-0 left-0 right-0
        h-20
        bg-black/70
        text-white
        z-50
        flex items-center justify-between px-6
      "
      >
        <div className="flex gap-2">
          <Image
            src="/running.png"
            alt="Fitbit Logo"
            width={40}
            height={30}
            className="invert"
          />
          <span className="font-extrabold font-sans text-3xl">FITBIT</span>
        </div>

        <div className="hidden md:flex absolute left-1/2 -translate-x-1/2 gap-8 text-white font-sans font-semibold">
          <a href="/about" className="hover:text-gray-300">
            ABOUT
          </a>
          <a href="/dashboard" className="hover:text-gray-300">
            DASHBOARD
          </a>
          <a href="#" className="hover:text-gray-300">
            FIND A GYM
          </a>
          <a href="#" className="hover:text-gray-300">
            TRAINING
          </a>
          <a href="#" className="hover:text-gray-300">
            BLOG
          </a>
          <a href="#" className="hover:text-gray-300">
            CAREERS
          </a>
        </div>

        <div className="flex items-center">
          <Button
            variant="signUpFree"
            onClick={() => setLoginOpen(true)}
            className="text-white font-sans font-semibold hover:text-black hover:bg-white"
          >
            Sign Up Free
          </Button>
        </div>
      </header>

      <LoginModal isOpen={loginOpen} onClose={() => setLoginOpen(false)} />
    </>
  );
}
