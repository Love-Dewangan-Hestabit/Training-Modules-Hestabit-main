"use client";

import { useState } from "react";

import Sidebar from "@/components/ui/Sidebar";
import NavbarHome from "@/components/ui/Navbar_Home";

export default function LayoutClient({ children }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false); // hidden initially

  return (
    <>
      <NavbarHome toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

      <div className="flex">
        {isSidebarOpen && <Sidebar />}

        <main className="flex-1 min-h-screen p-6 bg-white">{children}</main>
      </div>
    </>
  );
}
