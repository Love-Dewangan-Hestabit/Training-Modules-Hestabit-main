"use client";

import Navbar from "@/components/ui/Navbar";

export default function ProfilePage() {
  return (
    <>
      {/* Navbar */}
      <Navbar />

      {/* Page Content */}
      <main className="p-6 bg-gray-100 min-h-screen">
        <h1 className="text-gray-700 text-2xl font-bold mb-2">Profile</h1>
        <p className="text-gray-700">This page intentionally has no sidebar.</p>
      </main>
    </>
  );
}
