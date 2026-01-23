"use client";

import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";
import Input from "@/components/ui/Input";
import Button from "@/components/ui/Button";

const mockUsers = [
  {
    id: 1,
    name: "John Doe",
    email: "john.doe@example.com",
    role: "Admin",
    status: "Active",
    joinDate: "2024-01-15",
    workouts: 45,
  },
  {
    id: 2,
    name: "Jane Smith",
    email: "jane.smith@example.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-20",
    workouts: 32,
  },
  {
    id: 3,
    name: "Mike Johnson",
    email: "mike.j@example.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-10",
    workouts: 28,
  },
  {
    id: 4,
    name: "Sarah Williams",
    email: "sarah.w@example.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-01-05",
    workouts: 67,
  },
  {
    id: 5,
    name: "David Brown",
    email: "david.b@example.com",
    role: "Member",
    status: "Inactive",
    joinDate: "2023-11-12",
    workouts: 15,
  },
  {
    id: 6,
    name: "Emily Davis",
    email: "emily.d@example.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-04-01",
    workouts: 41,
  },
  {
    id: 7,
    name: "Chris Wilson",
    email: "chris.w@example.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-02-14",
    workouts: 53,
  },
  {
    id: 8,
    name: "Lisa Anderson",
    email: "lisa.a@example.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-22",
    workouts: 22,
  },
];

export default function UsersPage() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [entriesPerPage, setEntriesPerPage] = useState(10);

  const filteredUsers = mockUsers.filter(
    (user) =>
      user.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.email.toLowerCase().includes(searchTerm.toLowerCase()) ||
      user.role.toLowerCase().includes(searchTerm.toLowerCase()),
  );

  return (
    <>
      <Navbar toggleSidebar={() => setIsSidebarOpen(!isSidebarOpen)} />

      <div className="flex min-h-screen bg-gray-100">
        {isSidebarOpen && <Sidebar />}

        <main className="flex-1 p-6 overflow-y-auto">
          <div className="mb-6">
            <h1 className="text-2xl font-bold text-gray-800 mb-2">
              Users Management
            </h1>
            <div className="bg-gray-200 text-gray-700 text-sm px-4 py-2 rounded">
              Dashboard / Users
            </div>
          </div>

          {/* Stats Cards */}
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
            <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-blue-500">
              <p className="text-gray-600 text-sm font-semibold mb-1">
                Total Users
              </p>
              <p className="text-3xl font-bold text-gray-800">
                {mockUsers.length}
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-green-500">
              <p className="text-gray-600 text-sm font-semibold mb-1">
                Active Users
              </p>
              <p className="text-3xl font-bold text-gray-800">
                {mockUsers.filter((u) => u.status === "Active").length}
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-yellow-500">
              <p className="text-gray-600 text-sm font-semibold mb-1">
                Trainers
              </p>
              <p className="text-3xl font-bold text-gray-800">
                {mockUsers.filter((u) => u.role === "Trainer").length}
              </p>
            </div>
            <div className="bg-white rounded-lg shadow-md p-6 border-l-4 border-red-500">
              <p className="text-gray-600 text-sm font-semibold mb-1">
                Members
              </p>
              <p className="text-3xl font-bold text-gray-800">
                {mockUsers.filter((u) => u.role === "Member").length}
              </p>
            </div>
          </div>

          {/* Users Table */}
          <div className="bg-white rounded-lg shadow-md p-6">
            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4">
              <h3 className="font-semibold text-gray-800 text-lg">
                👥 All Users
              </h3>
              <Button variant="primary" className="bg-black hover:bg-gray-800">
                + Add New User
              </Button>
            </div>

            <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-4 gap-4">
              <div className="flex items-center gap-2 text-sm text-gray-600">
                <span>Show</span>
                <select
                  className="border rounded px-2 py-1"
                  value={entriesPerPage}
                  onChange={(e) => setEntriesPerPage(Number(e.target.value))}
                >
                  <option value={5}>5</option>
                  <option value={10}>10</option>
                  <option value={25}>25</option>
                  <option value={50}>50</option>
                </select>
                <span>entries</span>
              </div>

              <div className="flex items-center gap-2 text-sm text-gray-600">
                <span>Search:</span>
                <Input
                  placeholder="Search users..."
                  variant="search"
                  value={searchTerm}
                  onChange={(e) => setSearchTerm(e.target.value)}
                />
              </div>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-sm text-left text-gray-600">
                <thead className="border-b-2 bg-gray-50">
                  <tr>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      ID
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Name
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Email
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Role
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Status
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Join Date
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Workouts
                    </th>
                    <th className="px-4 py-3 font-semibold text-gray-700">
                      Actions
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {filteredUsers.slice(0, entriesPerPage).map((user) => (
                    <tr
                      key={user.id}
                      className="border-b hover:bg-gray-50 transition"
                    >
                      <td className="px-4 py-3 font-medium text-gray-900">
                        {user.id}
                      </td>
                      <td className="px-4 py-3">
                        <div className="flex items-center gap-3">
                          <div className="w-8 h-8 rounded-full bg-gray-800 text-white flex items-center justify-center font-semibold">
                            {user.name.charAt(0)}
                          </div>
                          <span className="font-medium">{user.name}</span>
                        </div>
                      </td>
                      <td className="px-4 py-3">{user.email}</td>
                      <td className="px-4 py-3">
                        <span
                          className={`px-2 py-1 rounded text-xs font-semibold ${
                            user.role === "Admin"
                              ? "bg-purple-100 text-purple-700"
                              : user.role === "Trainer"
                                ? "bg-blue-100 text-blue-700"
                                : "bg-gray-100 text-gray-700"
                          }`}
                        >
                          {user.role}
                        </span>
                      </td>
                      <td className="px-4 py-3">
                        <span
                          className={`px-2 py-1 rounded text-xs font-semibold ${
                            user.status === "Active"
                              ? "bg-green-100 text-green-700"
                              : "bg-red-100 text-red-700"
                          }`}
                        >
                          {user.status}
                        </span>
                      </td>
                      <td className="px-4 py-3">{user.joinDate}</td>
                      <td className="px-4 py-3 font-medium">{user.workouts}</td>
                      <td className="px-4 py-3">
                        <div className="flex gap-2">
                          <button className="text-blue-600 hover:text-blue-800 font-medium">
                            Edit
                          </button>
                          <button className="text-red-600 hover:text-red-800 font-medium">
                            Delete
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="flex flex-col md:flex-row justify-between items-center mt-4 text-sm text-gray-600 gap-4">
              <p>
                Showing {Math.min(entriesPerPage, filteredUsers.length)} of{" "}
                {filteredUsers.length} entries
              </p>
              <div className="flex gap-2">
                <button className="px-3 py-1 border rounded hover:bg-gray-100">
                  Previous
                </button>
                <button className="px-3 py-1 bg-black text-white rounded">
                  1
                </button>
                <button className="px-3 py-1 border rounded hover:bg-gray-100">
                  2
                </button>
                <button className="px-3 py-1 border rounded hover:bg-gray-100">
                  Next
                </button>
              </div>
            </div>
          </div>
        </main>
      </div>
    </>
  );
}
