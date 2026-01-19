export default function Navbar({ toggleSidebar }) {
  return (
    <header className="h-14 bg-gray-800 text-white flex items-center justify-between px-6">
      <div className="flex items-center gap-4">
        <button onClick={toggleSidebar} className="text-xl focus:outline-none">
          ☰
        </button>

        <span className="font-semibold text-lg">Start Bootstrap</span>
      </div>

      <div className="flex items-center">
        <input
          type="text"
          placeholder="Search..."
          className="px-3 py-2 bg-white rounded-l text-black text-sm"
        />
        <button className="bg-blue-600 px-3 py-2 rounded-r text-sm">🔍</button>
      </div>
    </header>
  );
}
