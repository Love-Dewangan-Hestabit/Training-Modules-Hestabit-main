"use client";

import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";

export default function DashboardLayout({ children }) {
  return (
    <>
      <main className="flex-1  bg-gray-100">{children}</main>
    </>
  );
}
