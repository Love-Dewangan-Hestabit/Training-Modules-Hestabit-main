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
  { name: "Mon", value: 30 },
  { name: "Tue", value: 45 },
  { name: "Wed", value: 28 },
  { name: "Thu", value: 60 },
  { name: "Fri", value: 50 },
];

export default function DashboardPage() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <>
      {/* Top Navbar */}
      <Navbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

      {/* Layout Wrapper */}
      <div className="flex min-h-screen bg-gray-100">
        {/* Sidebar */}
        {isSidebarOpen && <Sidebar />}

        {/* Main Content */}
        <main className="flex-1 p-6 overflow-y-auto">
          {/* Page Header */}
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-2">Dashboard</h1>
            <div className="bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded">
              Dashboard
            </div>
          </div>

          {/* Cards */}
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
            <Card title="Primary Card" variant="blue" footer="View Details >" />
            <Card
              title="Warning Card"
              variant="yellow"
              footer="View Details >"
            />
            <Card
              title="Success Card"
              variant="green"
              footer="View Details >"
            />
            <Card title="Danger Card" variant="red" footer="View Details >" />
          </div>

          {/* Charts */}
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
            {/* Area Chart */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="font-semibold text-gray-800 mb-4">
                📊 Area Chart
              </h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <AreaChart data={chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Area dataKey="value" stroke="#3b82f6" fill="#93c5fd" />
                  </AreaChart>
                </ResponsiveContainer>
              </div>
            </div>

            {/* Bar Chart */}
            <div className="bg-white rounded-lg shadow-md p-6">
              <h3 className="font-semibold text-gray-800 mb-4">📊 Bar Chart</h3>
              <div className="h-64">
                <ResponsiveContainer width="100%" height="100%">
                  <BarChart data={chartData}>
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="value" fill="#22c55e" />
                  </BarChart>
                </ResponsiveContainer>
              </div>
            </div>
          </div>

          {/* Data Table */}
          <div className="bg-white rounded-lg shadow-md p-6 mb-6">
            <h3 className="font-semibold text-gray-800 mb-4">🗂️ Data Table</h3>

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
                    <th className="px-4 py-3">Name</th>
                    <th className="px-4 py-3">Position</th>
                    <th className="px-4 py-3">Office</th>
                    <th className="px-4 py-3">Age</th>
                    <th className="px-4 py-3">Start Date</th>
                    <th className="px-4 py-3">Salary</th>
                  </tr>
                </thead>
                <tbody>
                  <tr className="border-b hover:bg-gray-50">
                    <td className="px-4 py-3">James</td>
                    <td className="px-4 py-3">Architect</td>
                    <td className="px-4 py-3">Scotland</td>
                    <td className="px-4 py-3">54</td>
                    <td className="px-4 py-3">2003/04/26</td>
                    <td className="px-4 py-3">$128,800</td>
                  </tr>
                  <tr className="border-b hover:bg-gray-50">
                    <td className="px-4 py-3">Brock</td>
                    <td className="px-4 py-3">Chartered Accountant</td>
                    <td className="px-4 py-3">Germany</td>
                    <td className="px-4 py-3">56</td>
                    <td className="px-4 py-3">2003/02/23</td>
                    <td className="px-4 py-3">$200,600</td>
                  </tr>
                  <tr className="hover:bg-gray-50">
                    <td className="px-4 py-3">Daniel</td>
                    <td className="px-4 py-3">Software Engineer</td>
                    <td className="px-4 py-3">Texas</td>
                    <td className="px-4 py-3">60</td>
                    <td className="px-4 py-3">2006/04/11</td>
                    <td className="px-4 py-3">$78,000</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          {/* Modal Demo */}
          <Button onClick={() => setIsModalOpen(true)}>Open Modal Demo</Button>
        </main>
      </div>

      {/* Modal */}
      <Modal
        isOpen={isModalOpen}
        onClose={() => setIsModalOpen(false)}
        title="Example Modal"
        footer={
          <>
            <Button variant="danger" onClick={() => setIsModalOpen(false)}>
              Close
            </Button>
            <Button variant="primary" onClick={() => setIsModalOpen(false)}>
              Save Changes
            </Button>
          </>
        }
      >
        <p className="text-gray-700">
          This modal for testing this function will update this later.
        </p>
      </Modal>
    </>
  );
}
