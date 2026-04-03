"use client";

import Button from "@/components/ui/Button";

export default function Footer() {
  return (
    <footer className="bg-black text-white px-6 md:px-16 py-16">
      <div className="flex flex-col md:flex-row justify-between gap-16 border-b border-white/20 pb-16">
        <div className="flex flex-col gap-4 max-w-md">
          <h2 className="text-3xl font-extrabold font-sans tracking-wide">
            FITBIT
          </h2>
          <p className="text-white/70 font-sans">
            Your daily motivation to wake up, train hard, and conquer your
            goals. Never miss a workout.
          </p>
        </div>

        <div className="grid grid-cols-2 md:grid-cols-3 gap-12 text-sm font-sans">
          <div className="flex flex-col gap-3">
            <h3 className="font-bold">Product</h3>
            <a href="#" className="text-white/70 hover:text-white">
              Workouts
            </a>
            <a href="#" className="text-white/70 hover:text-white">
              Programs
            </a>
            <a href="#" className="text-white/70 hover:text-white">
              Pricing
            </a>
          </div>

          <div className="flex flex-col gap-3">
            <h3 className="font-bold">Company</h3>
            <a href="#" className="text-white/70 hover:text-white">
              About
            </a>
            <a href="#" className="text-white/70 hover:text-white">
              Careers
            </a>
            <a href="#" className="text-white/70 hover:text-white">
              Contact
            </a>
          </div>

          <div className="flex flex-col gap-3">
            <h3 className="font-bold">Legal</h3>
            <a href="#" className="text-white/70 hover:text-white">
              Privacy Policy
            </a>
            <a href="#" className="text-white/70 hover:text-white">
              Terms
            </a>
          </div>
        </div>
      </div>

      <div className="flex flex-col md:flex-row justify-between items-center pt-8 text-xs text-white/50 font-sans">
        <p>© {new Date().getFullYear()} FITBIT. All rights reserved.</p>
        <p>Built for athletes. Designed for results.</p>
      </div>
    </footer>
  );
}
