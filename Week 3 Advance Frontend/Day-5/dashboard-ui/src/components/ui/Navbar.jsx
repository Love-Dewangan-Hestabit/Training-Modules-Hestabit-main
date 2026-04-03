import Button from "./Button";
import Input from "./Input";
import Image from "next/image";

export default function Navbar({ toggleSidebar }) {
  return (
    <header className="h-16 bg-black text-white flex items-center justify-between px-6">
      <div className="flex items-center gap-4">
        <Button onClick={toggleSidebar} variant="hamBurger">
          ☰
        </Button>

        <div className="flex gap-1">
          <Image
            src="/running.png"
            alt="Fitbit Logo"
            width={25}
            height={25}
            className="invert"
          />

          <a href="/" className="font-bold font-sans text-xl">
            FITBIT
          </a>
        </div>
        {/* <span href="/app" className="font-semibold text-lg">
          Fitbit
        </span> */}
      </div>

      <div className="flex items-center">
        <Input
          type="text"
          placeholder="Search..."
          variant="search"
          className="px-3 py-2 text-sm rounded-l text-gray-600"
        />
        <Button variant="search">
          <Image
            src="/magnifying-glass-solid-full.svg"
            alt="Search Logo"
            width={20}
            height={20}
          />
        </Button>
      </div>
    </header>
  );
}
