"use client";

import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";

export default function ProfilePage() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <>
      <Navbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

      <div className="flex min-h-screen bg-gray-100">
        {isSidebarOpen && <Sidebar />}

        <main className="flex-1 p-6 overflow-y-auto">
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-2">Profile</h1>
            <div className="bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded">
              Dashboard / Profile
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <div className="flex flex-col md:flex-row gap-6">
              <img
                src="/p3.jpg"
                alt="Profile"
                className="w-32 h-32 rounded-full object-cover border-4 border-black shadow"
              />

              <div className="flex-1">
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h2 className="text-xl font-semibold text-gray-800">
                      James Washington
                    </h2>
                    <p className="text-sm text-gray-500">
                      Intermediate Fitness Enthusiast
                    </p>
                  </div>
                  <Button variant="editProfile">Edit Profile</Button>
                </div>

                <p className="text-sm text-gray-600 leading-relaxed mb-4">
                  James is focused on building strength, improving endurance,
                  and maintaining a balanced fitness routine through structured
                  weekly training and recovery sessions.
                </p>

                <p className="text-sm text-gray-600 leading-relaxed mb-6">
                  Her long-term goal is sustainable health improvement while
                  gradually increasing workout intensity and maintaining
                  consistency.
                </p>

                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
                  <div>
                    <span className="text-gray-500">Email</span>
                    <p className="font-medium text-gray-800">
                      nina.valentine@example.com
                    </p>
                  </div>
                  <div>
                    <span className="text-gray-500">Location</span>
                    <p className="font-medium text-gray-800">San Diego, CA</p>
                  </div>
                  <div>
                    <span className="text-gray-500">Joined</span>
                    <p className="font-medium text-gray-800">January 2024</p>
                  </div>
                  <div>
                    <span className="text-gray-500">Primary Goal</span>
                    <p className="font-medium text-gray-800">
                      Strength & Endurance
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <Card
              title="Total Workouts"
              value="128"
              variant="gray1"
              footer="Avg. 5 workouts per week"
            />

            <Card
              title="Calories Burned"
              value="24,580"
              variant="gray2"
              footer="410 calories per workout"
            />

            <Card
              title="Active Days"
              value="86"
              variant="gray3"
              footer="Best streak: 9 days"
            />
          </div>
        </main>
      </div>
    </>
  );
}
