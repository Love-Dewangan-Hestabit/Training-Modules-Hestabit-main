export default function Button({
  children,
  variant = "primary",
  size = "md",
  onClick,
  className = "",
}) {
  const baseStyles =
    "rounded transition-colors duration-200 flex items-center justify-between";

  const variants = {
    primary: "bg-blue-600 text-white hover:bg-blue-700",
    search:
      "bg-blue-600 px-3 py-2 text-sm rounded-l-none rounded-r hover:bg-blue-700",
    hamBurger: "text-xl hover:bg-gray-600",
    tryForFree:
      "rounded-full bg-orange-500/70 text-white px-12 py-4 hover:bg-orange-600/70",
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
