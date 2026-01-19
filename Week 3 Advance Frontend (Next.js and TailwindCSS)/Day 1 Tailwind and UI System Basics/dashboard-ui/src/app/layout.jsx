"use client";

import "./globals.css";
import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";

export default function RootLayout({ children }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <html lang="en">
      <body>
        <Navbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

        <div className="flex">
          {isSidebarOpen && <Sidebar />}

          <main className="flex-1 p-6 bg-gray-100">{children}</main>
        </div>
      </body>
    </html>
  );
}
