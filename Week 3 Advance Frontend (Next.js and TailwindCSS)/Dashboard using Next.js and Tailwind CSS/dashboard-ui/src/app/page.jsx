"use client";

import { useState } from "react";
import Card from "@/components/ui/Card";
import Button from "@/components/ui/Button";
import Modal from "@/components/ui/Modal";

export default function Dashboard() {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div>
      {/* Breadcrumb */}
      <div className="mb-4">
        <h1 className="text-2xl font-bold text-gray-800">Dashboard</h1>
        <p className="text-gray-600 text-sm">Dashboard</p>
      </div>

      {/* Cards Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-6">
        <Card
          title="Primary Card"
          variant="primary"
          footer={
            <>
              <span>View Details</span>
              <span>→</span>
            </>
          }
        >
          <p className="text-gray-700">This is a primary card component.</p>
        </Card>

        <Card
          title="Warning Card"
          variant="warning"
          footer={
            <>
              <span>View Details</span>
              <span>→</span>
            </>
          }
        >
          <p className="text-gray-700">This is a warning card component.</p>
        </Card>

        <Card
          title="Success Card"
          variant="success"
          footer={
            <>
              <span>View Details</span>
              <span>→</span>
            </>
          }
        >
          <p className="text-gray-700">This is a success card component.</p>
        </Card>

        <Card
          title="Danger Card"
          variant="danger"
          footer={
            <>
              <span>View Details</span>
              <span>→</span>
            </>
          }
        >
          <p className="text-gray-700">This is a danger card component.</p>
        </Card>
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
        {/* Area Chart */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-lg">📊</span>
            <h3 className="font-semibold text-gray-800">Area Chart Example</h3>
          </div>
          <div className="h-64 bg-blue-50 rounded flex items-end justify-around p-4"></div>
        </div>

        {/* Bar Chart */}
        <div className="bg-white rounded-lg shadow-md p-6">
          <div className="flex items-center gap-2 mb-4">
            <span className="text-lg">📊</span>
            <h3 className="font-semibold text-gray-800">Bar Chart Example</h3>
          </div>
        </div>
      </div>

      {/* Datatable Section */}
      <div className="bg-white rounded-lg shadow-md p-6">
        <div className="flex items-center gap-2 mb-4">
          <span className="text-lg">🗂️</span>
          <h3 className="font-semibold text-gray-800">Datatable Example</h3>
        </div>

        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">Show</span>
            <select className="border border-gray-300 rounded px-2 py-1 text-sm">
              <option>10</option>
              <option>25</option>
              <option>50</option>
            </select>
            <span className="text-sm text-gray-600">entries</span>
          </div>

          <div className="flex items-center gap-2">
            <span className="text-sm text-gray-600">Search:</span>
            <input
              type="text"
              className="border border-gray-300 rounded px-3 py-1 text-sm"
            />
          </div>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="bg-gray-50 border-b">
              <tr>
                <th className="px-4 py-3 font-medium text-gray-700">Name</th>
                <th className="px-4 py-3 font-medium text-gray-700">
                  Position
                </th>
                <th className="px-4 py-3 font-medium text-gray-700">Office</th>
                <th className="px-4 py-3 font-medium text-gray-700">Age</th>
                <th className="px-4 py-3 font-medium text-gray-700">
                  Start Date
                </th>
                <th className="px-4 py-3 font-medium text-gray-700">Salary</th>
              </tr>
            </thead>
            <tbody>
              <tr className="border-b hover:bg-gray-50">
                <td className="px-4 py-3">Tiger Nixon</td>
                <td className="px-4 py-3">System Architect</td>
                <td className="px-4 py-3">Edinburgh</td>
                <td className="px-4 py-3">61</td>
                <td className="px-4 py-3">2011/04/25</td>
                <td className="px-4 py-3">$320,800</td>
              </tr>
              <tr className="border-b hover:bg-gray-50">
                <td className="px-4 py-3">Garrett Winters</td>
                <td className="px-4 py-3">Accountant</td>
                <td className="px-4 py-3">Tokyo</td>
                <td className="px-4 py-3">63</td>
                <td className="px-4 py-3">2011/07/25</td>
                <td className="px-4 py-3">$170,750</td>
              </tr>
              <tr className="border-b hover:bg-gray-50">
                <td className="px-4 py-3">Ashton Cox</td>
                <td className="px-4 py-3">Junior Technical Author</td>
                <td className="px-4 py-3">San Francisco</td>
                <td className="px-4 py-3">66</td>
                <td className="px-4 py-3">2009/01/12</td>
                <td className="px-4 py-3">$86,000</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      {/* Demo Button for Modal */}
      <div className="mt-6">
        <Button onClick={() => setIsModalOpen(true)}>Open Modal Demo</Button>
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
          This is an example modal dialog. You can put any content here
          including forms, messages, or confirmations.
        </p>
      </Modal>
    </div>
  );
}
