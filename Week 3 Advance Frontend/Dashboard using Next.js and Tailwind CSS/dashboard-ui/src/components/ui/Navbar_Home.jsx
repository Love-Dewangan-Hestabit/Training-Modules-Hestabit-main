import Button from "./Button";
import Input from "./Input";

export default function NavbarHome() {
  return (
    <header
      className="
      fixed top-0 left-0 right-0
      h-20
      bg-black/70
      text-white
      z-50
      flex items-center justify-between px-6
    "
    >
      <span className="font-semibold font-sans text-2xl">Fitbit</span>

      <div className="absolute left-1/2 -translate-x-1/2 flex gap-8 text-white font-sans font-semibold">
        <a href="/about" className="hover:text-gray-300">
          ABOUT
        </a>
        <a href="/dashboard" className="hover:text-gray-300">
          DASHBOARD
        </a>
        <a href="#" className="hover:text-gray-300">
          FIND A GYM
        </a>
        <a href="#" className="hover:text-gray-300">
          TRAINING
        </a>
        <a href="#" className="hover:text-gray-300">
          BLOG
        </a>
        <a href="#" className="hover:text-gray-300">
          CAREERS
        </a>
      </div>

      <div className="flex items-center">
        <Button
          variant="tryForFree"
          className=" text-white font-sans font-extrabold hover:text-black/50"
        >
          Try Us For Free
        </Button>
      </div>
    </header>
  );
}
