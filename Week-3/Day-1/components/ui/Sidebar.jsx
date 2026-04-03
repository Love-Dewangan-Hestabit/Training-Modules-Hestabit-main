import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-black/90 text-gray-300 min-h-screen p-4">
      <nav className="space-y-4">
        <p className="text-xs uppercase text-gray-500">Core</p>

        <Link
          href="/dashboard"
          className="block px-2 py-2 rounded hover:bg-gray-800 text-white"
        >
          Dashboard
        </Link>

        <Link
          href="/dashboard/users"
          className="block px-2 py-2 rounded hover:bg-gray-800 text-white"
        >
          Users
        </Link>

        <Link
          href="/dashboard/profile"
          className="block px-2 py-2 rounded hover:bg-gray-800"
        >
          Profile
        </Link>

        <Link
          href="/dashboard"
          className="block px-2 py-2 rounded hover:bg-gray-800"
        >
          Charts
        </Link>

        <Link
          href="/dashboard"
          className="block px-2 py-2 rounded hover:bg-gray-800"
        >
          Tables
        </Link>
      </nav>
    </aside>
  );
}
