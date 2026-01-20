import Button from "./Button";
import Input from "./Input";

export default function Navbar({ toggleSidebar }) {
  return (
    <header className="h-14 bg-gray-800 text-white flex items-center justify-between px-6">
      <div className="flex items-center gap-4">
        <Button onClick={toggleSidebar} variant="hamBurger">
          ☰
        </Button>

        <span className="font-semibold text-lg">Start Bootstrap</span>
      </div>

      <div className="flex items-center">
        <Input
          type="text"
          placeholder="Search..."
          variant="search"
          className="px-3 py-2 text-sm rounded-l text-gray-600"
        />
        <Button variant="search">🔍</Button>
      </div>
    </header>
  );
}
