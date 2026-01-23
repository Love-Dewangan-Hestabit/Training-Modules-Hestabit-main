"use client";

import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";
import Input from "@/components/ui/Input";

import {
  AreaChart,
  Area,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const chartData = [
  { name: "Mon", value: 45 },
  { name: "Tue", value: 52 },
  { name: "Wed", value: 38 },
  { name: "Thu", value: 65 },
  { name: "Fri", value: 58 },
];

export default function DashboardPage() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <>
      <Navbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

      <div className="flex min-h-screen bg-gray-100">
        {isSidebarOpen && <Sidebar />}

        <main className="flex-1 p-6 overflow-y-auto">
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-2">Dashboard</h1>
            <div className="bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded">
              Dashboard
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <Card
              title="Workouts This Week"
              variant="gray1"
              footer="View Details >"
            />
            <Card
              title="Calories Burned"
              variant="gray2"
              footer="View Details >"
            />
            <Card title="Active Days" variant="gray3" footer="View Details >" />
            <Card
              title="Weight Progress"
              variant="gray4"
              footer="View Details >"
            />
          </div>

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="font-semibold text-gray-800 mb-4">
                📊 Workout Minutes
              </h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip contentStyle={{ color: "#000" }} />
                    <Area dataKey="value" stroke="#000000" fill="#808080" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="font-semibold text-gray-800 mb-4">
                📊 Calories Burned
              </h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip contentStyle={{ color: "#000" }} />
                    <Bar dataKey="value" fill="#808080" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>

          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <h3 className="font-semibold text-gray-800 mb-4">
              🗂️ Workout History
            </h3>

            <div className="flex justify-between items-center mb-4">
              <div className="flex items-center gap-2 text-sm text-gray-600">
                <span>Show</span>
                <select className="border rounded px-2 py-1">
                  <option>10</option>
                  <option>25</option>
                  <option>50</option>
                </select>
                <span>entries</span>
              </div>

              <div className="flex items-center gap-2 text-sm text-gray-600">
                <span>Search:</span>
                <Input placeholder="Search..." variant="search" />
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-sm text-left text-gray-600">
                <thead className="border-b bg-gray-50">
                  <tr>
                    <th className="px-4 py-3">Date</th>
                    <th className="px-4 py-3">Exercise</th>
                    <th className="px-4 py-3">Duration</th>
                    <th className="px-4 py-3">Sets</th>
                    <th className="px-4 py-3">Reps</th>
                    <th className="px-4 py-3">Calories</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b hover:bg-gray-50">
                    <td className="px-4 py-3">2025/01/20</td>
                    <td className="px-4 py-3">Bench Press</td>
                    <td className="px-4 py-3">45 mins</td>
                    <td className="px-4 py-3">4</td>
                    <td className="px-4 py-3">12</td>
                    <td className="px-4 py-3">320</td>
                  </tr>
                  <tr className="border-b hover:bg-gray-50">
                    <td className="px-4 py-3">2025/01/19</td>
                    <td className="px-4 py-3">Running</td>
                    <td className="px-4 py-3">30 mins</td>
                    <td className="px-4 py-3">-</td>
                    <td className="px-4 py-3">-</td>
                    <td className="px-4 py-3">280</td>
                  </tr>
                  <tr className="hover:bg-gray-50">
                    <td className="px-4 py-3">2025/01/18</td>
                    <td className="px-4 py-3">Deadlift</td>
                    <td className="px-4 py-3">50 mins</td>
                    <td className="px-4 py-3">5</td>
                    <td className="px-4 py-3">8</td>
                    <td className="px-4 py-3">400</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}
