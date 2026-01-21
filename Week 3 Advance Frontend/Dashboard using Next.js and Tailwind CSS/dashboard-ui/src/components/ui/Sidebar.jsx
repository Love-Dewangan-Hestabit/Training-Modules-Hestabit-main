import Link from "next/link";

export default function Sidebar() {
  return (
    <aside className="w-64 bg-gray-900 text-gray-300 min-h-screen p-4">
      <nav className="space-y-4">
        <p className="text-xs uppercase text-gray-500">Core</p>

        <Link
          href="/dashboard"
          className="block px-2 py-2 rounded hover:bg-gray-800 text-white"
        >
          Dashboard
        </Link>

        <p className="text-xs uppercase text-gray-500 mt-6">Interface</p>

        <a href="#" className="block px-2 py-2 rounded hover:bg-gray-800">
          Layouts
        </a>
        <Link
          href="/dashboard/profile"
          className="block px-2 py-2 rounded hover:bg-gray-800"
        >
          Profile
        </Link>

        <p className="text-xs uppercase text-gray-500 mt-6">Addons</p>

        <a href="#" className="block px-2 py-2 rounded hover:bg-gray-800">
          Charts
        </a>
        <a href="#" className="block px-2 py-2 rounded hover:bg-gray-800">
          Tables
        </a>
      </nav>
    </aside>
  );
}
