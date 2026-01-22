"use client";

import NavbarHome from "@/components/ui/Navbar_Home";
import Footer from "@/components/ui/Footer";
import Testimonials from "@/components/ui/Testimonial";
import Button from "@/components/ui/Button";
import Image from "next/image";

export default function HomePage() {
  return (
    <>
      <NavbarHome />

      <main className="pt-20 min-h-screen bg-white  overflow-hidden">
        <div className="relative">
          <Image
            src="/hero.png"
            alt="Running"
            width={1920}
            height={1600}
            className="px-2 pt-2"
          />

          <div className="absolute inset-0 bg-black/40" />

          <h1 className="absolute bottom-20 sm:bottom-24 md:bottom-32 left-4 sm:left-6 md:left-16 font-sans text-2xl sm:text-3xl md:text-6xl text-white font-extrabold leading-tight">
            YOUR JOURNEY TO <br /> FITNESS STARTS HERE.
          </h1>

          <div className="flex absolute bottom-4 sm:bottom-6 md:bottom-10 left-4 sm:left-6 md:left-16 items-start md:items-center gap-4">
            <Button
              variant="tryForFree"
              size="lg"
              className="text-black font-sans font-semibold hover:bg-black hover:text-white"
            >
              Get Started
            </Button>

            <p className="text-white font-semibold font-sans text-xs sm:text-sm md:text-base">
              Get 7 Days Free Trial <br /> then $59.99/month thereafter
            </p>
          </div>
        </div>

        <div className="w-full overflow-hidden whitespace-nowrap">
          <div className="flex w-max animate-marquee bg-black text-white text-xl md:text-3xl font-semibold font-sans">
            <span className="shrink-0 pr-8">
              Never Miss A Workout. Never Miss A Workout. Never Miss A Workout.
              Never Miss A Workout. Never Miss A Workout. Never Miss A Workout.
              Never Miss A Workout. Never Miss A Workout.
            </span>
            <span className="shrink-0 pr-8">
              Never Miss A Workout. Never Miss A Workout. Never Miss A Workout.
              Never Miss A Workout. Never Miss A Workout. Never Miss A Workout.
              Never Miss A Workout. Never Miss A Workout.
            </span>
          </div>
        </div>

        <div className="p-6 md:p-24 bg-black flex flex-col gap-24">
          <div className="flex flex-col md:flex-row items-center gap-8">
            <div className="relative">
              <Image src="/fit.jpg" alt="Running" width={500} height={500} />
              <div className="absolute inset-0 bg-black/20" />
            </div>
            <h1 className="flex-1 font-sans text-center text-4xl md:text-8xl text-white font-extrabold">
              WAKE.
            </h1>
          </div>

          <div className="flex flex-col md:flex-row-reverse items-center gap-8">
            <div className="relative">
              <Image src="/fit5.jpg" alt="Running" width={500} height={500} />
              <div className="absolute inset-0 bg-black/20" />
            </div>
            <h1 className="flex-1 font-sans text-center text-4xl md:text-8xl text-white font-extrabold">
              TRAIN.
            </h1>
          </div>

          <div className="flex flex-col md:flex-row items-center gap-8">
            <div className="relative">
              <Image src="/fit3.jpeg" alt="Running" width={500} height={500} />
              <div className="absolute inset-0 bg-black/20" />
            </div>
            <h1 className="flex-1 font-sans text-center text-4xl md:text-8xl text-white font-extrabold">
              CONQUER.
            </h1>
          </div>

          <div className="flex flex-col md:flex-row-reverse items-center gap-8">
            <div className="relative">
              <Image src="/fit1.jpg" alt="Running" width={500} height={500} />
              <div className="absolute inset-0 bg-black/20" />
            </div>
            <h1 className="flex-1 font-sans text-center text-4xl md:text-8xl text-white font-extrabold">
              REPEAT.
            </h1>
          </div>
        </div>

        <Testimonials />

        <div className="relative">
          <Image src="/banner3.png" alt="Running" width={1920} height={500} />
          <div className="absolute inset-0 bg-black/40" />

          <div className="absolute inset-0 flex flex-col md:flex-row items-start md:items-center px-6 md:px-40 gap-8 md:gap-40">
            <div>
              <h1 className="font-sanstext-xl md:text-3xl text-white font-bold">
                FIND YOUR FIT
              </h1>
              <p className="font-sans font-semibold text-white mt-2">
                Ready to improve your mind, body and spirit? Find your fitness
                <br />
                community today.
              </p>
            </div>

            <Button
              variant="joinToday"
              className=" text-black font-semibold font-sans "
            >
              JOIN TODAY
            </Button>
          </div>
        </div>
      </main>

      <Footer />
    </>
  );
}
