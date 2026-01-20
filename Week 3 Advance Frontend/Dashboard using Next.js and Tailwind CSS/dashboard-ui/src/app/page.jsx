"use client";

import { useState } from "react";
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

export default function Dashboard() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div>
      <div className="mb-4">
        <h1 className="pb-4 text-2xl font-bold text-gray-800">Dashboard</h1>
        <p className="p-4 bg-gray-200 text-gray-800 text-sm">Dashboard</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        <Card
          title="Primary Card"
          variant="blue"
          footer={
            <>
              <span>View Details</span>
              <span> {">"} </span>
            </>
          }
        />
        <Card
          title="Warning Card"
          variant="yellow"
          footer={
            <>
              <span>View Details</span>
              <span> {">"} </span>
            </>
          }
        />
        <Card
          title="Success Card"
          variant="green"
          footer={
            <>
              <span>View Details</span>
              <span> {">"} </span>
            </>
          }
        />
        <Card
          title="Danger Card"
          variant="red"
          footer={
            <>
              <span>View Details</span>
              <span> {">"} </span>
            </>
          }
        />
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-lg">📊</span>
            <h3 className="font-semibold text-gray-800">Area Chart</h3>
          </div>

          <div className="h-64 text-gray-800">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={chartData}>
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Area dataKey="value" fill="#3b82f6" stroke="#3b82f6" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-lg">📊</span>
            <h3 className="font-semibold text-gray-800">Bar Chart</h3>
          </div>

          <div className="h-64 text-gray-600">
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

      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center gap-2 mb-4">
          <span className="text-lg">🗂️</span>
          <h3 className="font-semibold text-gray-800">Data Table</h3>
        </div>

        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">Show</span>
            <select className="border border-gray-300 rounded px-2 py-1 text-sm text-gray-600">
              <option>10</option>
              <option>25</option>
              <option>50</option>
            </select>
            <span className="text-sm text-gray-600">entries</span>
          </div>

          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">Search:</span>
            <Input
              type="text"
              placeholder="Search..."
              variant="search"
              className="border border-gray-300 rounded px-3 py-1 text-sm text-gray-600"
            />
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left text-gray-600">
            <thead className="bg-gray-50 border-b">
              <tr>
                <th className="px-4 py-3 font-medium">Name</th>
                <th className="px-4 py-3 font-medium">Position</th>
                <th className="px-4 py-3 font-medium">Office</th>
                <th className="px-4 py-3 font-medium">Age</th>
                <th className="px-4 py-3 font-medium">Start Date</th>
                <th className="px-4 py-3 font-medium">Salary</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b hover:bg-gray-50">
                <td className="px-4 py-3">James </td>
                <td className="px-4 py-3">Architect</td>
                <td className="px-4 py-3">Scotland</td>
                <td className="px-4 py-3">54</td>
                <td className="px-4 py-3">2003/04/26</td>
                <td className="px-4 py-3">$128,800</td>
              </tr>
              <tr className="border-b hover:bg-gray-50">
                <td className="px-4 py-3">Brock</td>
                <td className="px-4 py-3">Charted Accountant</td>
                <td className="px-4 py-3">Germany</td>
                <td className="px-4 py-3">56</td>
                <td className="px-4 py-3">2003/02/23</td>
                <td className="px-4 py-3">$200,600</td>
              </tr>
              <tr className="border-b hover:bg-gray-50">
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

      <div className="mt-6">
        <Button onClick={() => setIsModalOpen(true)}>Open Modal Demo</Button>
      </div>

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
          This modal for testing this function will update this later
        </p>
      </Modal>
    </div>
  );
}
