"use client";

import Image from "next/image";

export default function Testimonials() {
  return (
    <section className="bg-black py-16 md:py-32 px-6 md:px-12">
      <h2 className="text-center text-white font-extrabold text-4xl md:text-6xl mb-20 font-sans">
        WHAT THEY SAY
      </h2>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-12 ">
        <div className="bg-white text-black p-10 flex flex-col gap-6 hover:scale-[1.02] transition-transform">
          <div className="flex items-center gap-4">
            <Image
              src="/p1.jpg"
              alt="Alex Morgan"
              width={60}
              height={60}
              className="rounded-full"
            />

            <div>
              <p className="font-bold">Alex Morgan</p>
              <p className="text-sm text-gray-600 font-semibold">
                Marathon Runner
              </p>
            </div>
          </div>

          <p className="text-lg font-semibold font-sans">
            “This platform completely changed my routine. I feel stronger,
            faster, and more disciplined than ever.”
          </p>
        </div>

        <div className="bg-white text-black p-10 flex flex-col gap-6 hover:scale-[1.02] transition-transform">
          <div className="flex items-center gap-4">
            <Image
              src="/p4.jpg"
              alt="Jordan Lee"
              width={60}
              height={60}
              className="rounded-full"
            />

            <div>
              <p className="font-bold">Jordan Lee</p>
              <p className="text-sm text-gray-600 font-semibold">
                Fitness Enthusiast
              </p>
            </div>
          </div>

          <p className="text-lg font-semibold font-sans">
            “The workouts are intense, structured, and motivating. I never miss
            a workout anymore.”
          </p>
        </div>

        <div className="bg-white text-black p-10 flex flex-col gap-6 hover:scale-[1.02] transition-transform">
          <div className="flex items-center gap-4">
            <Image
              src="/p3.jpg"
              alt="Samantha Cruz"
              width={60}
              height={60}
              className="rounded-full"
            />

            <div>
              <p className="font-bold">Samantha Cruz</p>
              <p className="text-sm text-gray-600 font-semibold">
                Personal Trainer
              </p>
            </div>
          </div>

          <p className="text-lg font-semibold font-sans">
            “Perfect balance of strength and conditioning. I recommend it to all
            my clients.”
          </p>
        </div>
      </div>
    </section>
  );
}
