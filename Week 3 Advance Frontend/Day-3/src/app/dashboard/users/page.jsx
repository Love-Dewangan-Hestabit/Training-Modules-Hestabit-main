"use client";

import { useState } from "react";
import Navbar from "@/components/ui/Navbar";
import Sidebar from "@/components/ui/Sidebar";
import Input from "@/components/ui/Input";
import Button from "@/components/ui/Button";

/* ------------------ DUMMY USERS ------------------ */
const mockUsers = [
  {
    id: 1,
    name: "John Carter",
    email: "john.carter@gmail.com",
    role: "Admin",
    status: "Active",
    joinDate: "2024-01-05",
    workouts: 54,
  },
  {
    id: 2,
    name: "Emily Johnson",
    email: "emily.johnson@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-01-10",
    workouts: 21,
  },
  {
    id: 3,
    name: "Michael Brown",
    email: "michael.brown@yahoo.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-01-12",
    workouts: 68,
  },
  {
    id: 4,
    name: "Sarah Wilson",
    email: "sarah.wilson@gmail.com",
    role: "Member",
    status: "Inactive",
    joinDate: "2023-12-28",
    workouts: 14,
  },
  {
    id: 5,
    name: "David Miller",
    email: "david.miller@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-01",
    workouts: 37,
  },
  {
    id: 6,
    name: "Olivia Davis",
    email: "olivia.davis@yahoo.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-02-03",
    workouts: 59,
  },
  {
    id: 7,
    name: "Daniel Anderson",
    email: "daniel.anderson@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-06",
    workouts: 26,
  },
  {
    id: 8,
    name: "Sophia Martinez",
    email: "sophia.martinez@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-10",
    workouts: 31,
  },
  {
    id: 9,
    name: "James Taylor",
    email: "james.taylor@gmail.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-02-14",
    workouts: 72,
  },
  {
    id: 10,
    name: "Emma Thomas",
    email: "emma.thomas@yahoo.com",
    role: "Member",
    status: "Inactive",
    joinDate: "2024-02-18",
    workouts: 9,
  },
  {
    id: 11,
    name: "William Moore",
    email: "william.moore@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-20",
    workouts: 43,
  },
  {
    id: 12,
    name: "Ava Jackson",
    email: "ava.jackson@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-02-22",
    workouts: 34,
  },
  {
    id: 13,
    name: "Benjamin White",
    email: "ben.white@yahoo.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-02-25",
    workouts: 61,
  },
  {
    id: 14,
    name: "Isabella Harris",
    email: "isabella.harris@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-01",
    workouts: 29,
  },
  {
    id: 15,
    name: "Lucas Martin",
    email: "lucas.martin@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-04",
    workouts: 18,
  },
  {
    id: 16,
    name: "Mia Thompson",
    email: "mia.thompson@yahoo.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-03-07",
    workouts: 66,
  },
  {
    id: 17,
    name: "Henry Garcia",
    email: "henry.garcia@gmail.com",
    role: "Member",
    status: "Inactive",
    joinDate: "2024-03-10",
    workouts: 11,
  },
  {
    id: 18,
    name: "Charlotte Martinez",
    email: "charlotte.m@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-12",
    workouts: 24,
  },
  {
    id: 19,
    name: "Alexander Robinson",
    email: "alex.robinson@gmail.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-03-15",
    workouts: 70,
  },
  {
    id: 20,
    name: "Amelia Clark",
    email: "amelia.clark@yahoo.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-18",
    workouts: 33,
  },
  {
    id: 21,
    name: "Ethan Rodriguez",
    email: "ethan.rodriguez@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-20",
    workouts: 27,
  },
  {
    id: 22,
    name: "Harper Lewis",
    email: "harper.lewis@gmail.com",
    role: "Member",
    status: "Inactive",
    joinDate: "2024-03-22",
    workouts: 7,
  },
  {
    id: 23,
    name: "Samuel Lee",
    email: "samuel.lee@yahoo.com",
    role: "Trainer",
    status: "Active",
    joinDate: "2024-03-25",
    workouts: 64,
  },
  {
    id: 24,
    name: "Ella Walker",
    email: "ella.walker@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-27",
    workouts: 36,
  },
  {
    id: 25,
    name: "Noah Hall",
    email: "noah.hall@gmail.com",
    role: "Member",
    status: "Active",
    joinDate: "2024-03-30",
    workouts: 41,
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

      <div className="flex min-h-screen bg-gray-100 text-black">
        {isSidebarOpen && <Sidebar />}

        <main className="flex-1 p-6">
          <h1 className="text-2xl font-sans font-bold mb-4">
            Users Management
          </h1>

          <div className="bg-white rounded shadow p-4">
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-xl font-sans font-bold">Users</h2>
              <Button
                variant="addUser"
                className="bg-black rounded text-white text-sm"
              >
                Add User
              </Button>
            </div>

            <div className="flex justify-between items-center mb-3 text-sm">
              <div className="flex items-center gap-2">
                <span>Show</span>
                <select
                  className="border px-2 py-1"
                  value={entriesPerPage}
                  onChange={(e) => setEntriesPerPage(Number(e.target.value))}
                >
                  <option value={5}>5</option>
                  <option value={10}>10</option>
                  <option value={25}>25</option>
                </select>
              </div>

              <Input
                variant="search"
                className="border border-black p-3 rounded"
                placeholder="Search users..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
              />
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-sm border">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="p-2 text-left font-semibold">ID</th>
                    <th className="p-2 text-left font-semibold">Name</th>
                    <th className="p-2 text-left font-semibold">Email</th>
                    <th className="p-2 text-left font-semibold">Role</th>
                    <th className="p-2 text-left font-semibold">Status</th>
                    <th className="p-2 text-left font-semibold">Joined</th>
                    <th className="p-2 text-left font-semibold">Workouts</th>
                    <th className="p-2 text-left font-semibold">Actions</th>
                  </tr>
                </thead>

                <tbody>
                  {filteredUsers.slice(0, entriesPerPage).map((user) => (
                    <tr key={user.id} className="border-t hover:bg-gray-100">
                      <td className="p-2">{user.id}</td>
                      <td className="p-2 font-medium">{user.name}</td>
                      <td className="p-2">{user.email}</td>
                      <td className="p-2">{user.role}</td>
                      <td className="p-2">{user.status}</td>
                      <td className="p-2">{user.joinDate}</td>
                      <td className="p-2">{user.workouts}</td>
                      <td className="p-2 flex gap-3">
                        <button className="hover:underline">Edit</button>
                        <button className="hover:underline">Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            <div className="mt-3 text-sm">
              Showing {Math.min(entriesPerPage, filteredUsers.length)} of{" "}
              {filteredUsers.length} users
            </div>
          </div>
        </main>
      </div>
    </>
  );
}
