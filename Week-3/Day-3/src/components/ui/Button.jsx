export default function Button({
  children,
  variant = "primary",
  size = "md",
  onClick,
  className = "",
}) {
  const baseStyles =
    "transition-colors duration-200 flex items-center justify-center";

  const variants = {
    primary: "rounded bg-blue-600 text-white hover:bg-blue-700",

    search:
      "rounded bg-gray-400 px-3 py-2 text-sm rounded-l-none rounded-r hover:bg-blue-600",

    hamBurger: "text-xl hover:bg-gray-600 rounded",

    tryForFree: "rounded-full bg-white px-6 sm:px-10 md:px-12 py-3 md:py-4",

    signUpFree:
      "rounded-md bg-black px-6 sm:px-10 md:px-12 py-3 md:py-4 hover:bg-gray-700",

    joinToday:
      "bg-white px-10 sm:px-24 md:px-64 py-3 md:py-4 hover:bg-black hover:text-white hover:border-1 border-white",

    editProfile: "rounded bg-black text-white hover:bg-gray-500",
  };

  const sizes = {
    sm: "px-3 py-1 text-sm",
    md: "px-4 py-2 text-base",
    lg: "px-6 py-3 text-lg",
  };

  return (
    <button
      onClick={onClick}
      className={`${baseStyles} ${variants[variant]} ${sizes[size]} ${className}`}
    >
      {children}
    </button>
  );
}
