"use client";

import Navbar from "@/components/ui/Navbar";

export default function AboutPage() {
  return (
    <>
      {/* Navbar */}
      <Navbar />

      {/* Page Content */}
      <main className="min-h-screen bg-white px-6 md:px-24 py-16 font-sans">
        {/* Hero Section */}
        <section className="max-w-4xl mx-auto text-center">
          <h1 className="text-4xl md:text-6xl font-extrabold text-black">
            About Us
          </h1>
          <p className="mt-4 text-gray-700 text-lg">
            We’re here to help you build a stronger body, a sharper mind, and
            unstoppable discipline.
          </p>
        </section>

        {/* Divider */}
        <div className="max-w-4xl mx-auto my-12 h-px bg-black/10" />

        {/* Content Section */}
        <section className="max-w-4xl mx-auto space-y-8 text-gray-700">
          <p>
            Our platform was built with one goal in mind to make fitness
            accessible, motivating, and sustainable for everyone. Whether you’re
            just starting out or pushing for peak performance, we’re here to
            support your journey.
          </p>

          <p>
            We believe fitness is more than workouts. It’s about consistency,
            mindset, and community. That’s why we combine expert-led training,
            structured programs, and a supportive environment to help you stay
            on track.
          </p>

          <p>
            From strength training and conditioning to recovery and mindset,
            everything we build is designed to help you show up every day and
            give your best.
          </p>
        </section>

        {/* Highlight Section */}
        <section className="max-w-4xl mx-auto mt-16 bg-black text-white rounded-2xl p-8 md:p-12">
          <h2 className="text-2xl md:text-3xl font-bold">Our Mission</h2>
          <p className="mt-4 text-white/80">
            To empower people to take control of their health through structured
            training, accountability, and a mindset built for long-term success.
          </p>
        </section>
      </main>
    </>
  );
}
